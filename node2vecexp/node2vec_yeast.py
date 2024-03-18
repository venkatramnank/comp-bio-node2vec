import networkx as nx
from node2vec import Node2Vec
import pandas as pd
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from argparse import ArgumentParser

def main(config):

    with open(config.EDGELIST_PATH, 'r') as f:
        lines = f.readlines()

    # Initialize an empty list to store edge data
    edges = []

    # Iterate over the lines and parse edge data
    for line in lines:
        # Skip comment lines and empty lines
        if line.startswith("#") or not line.strip():
            continue
        # Split the line by whitespace and extract edge data
        data = line.split()
        # Extract source, target, and sign from the line
        source = int(data[0])
        target = int(data[1])
        sign = int(data[2])
        # Append edge data as a tuple to the list
        edges.append((source, target, {"sign": sign}))

    # Create a directed graph using the edge data
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Print some information about the graph
    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())


    # Load names of operons from file
    # operon_names = pd.read_csv('/Users/venkatramnankalyanakumar/Desktop/OSU/winter2024/NetworksCompBio/project/comp-bio-project/data/yeast_snap/S-cerevisiae-names.csv')

    # Load coherent feedforward loops and functionality from file
    # ffl_data = pd.read_csv('/Users/venkatramnankalyanakumar/Desktop/OSU/winter2024/NetworksCompBio/project/comp-bio-project/data/yeast_snap/S-cerevisiae-coherent-FFLs.csv')

    # Node2Vec parameters
    dimensions = config.EMBEDDING_DIMENSIONS
    walk_length = config.WALK_LENGTH
    num_walks = config.NUM_WALKS
    workers = config.WORKERS

    # Precompute probabilities and generate walks
    node2vec = Node2Vec(G, dimensions=dimensions, walk_length=walk_length, num_walks=num_walks, workers=workers)

    # Embed nodes
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    # Save embeddings for later use
    EMBEDDING_FILENAME = config.EMBEDDING_FILENAME
    model.wv.save_word2vec_format(EMBEDDING_FILENAME)

    # Load learned embeddings
    embeddings = {}
    with open(EMBEDDING_FILENAME) as f:
        next(f)  # Skip header
        for line in f:
            values = line.strip().split()
            node_id = values[0]
            embedding = np.array(values[1:], dtype=np.float32)
            embeddings[node_id] = embedding

    # Extract node IDs and corresponding embeddings
    node_ids = list(embeddings.keys())
    embeddings_matrix = np.array([embeddings[node_id] for node_id in node_ids])

    # Compute pairwise cosine similarity between node embeddings
    similarity_matrix = cosine_similarity(embeddings_matrix)

    if config.TSNE_VIS_COMPONENTS == 2:
        # Reduce dimensionality using t-SNE
        tsne = TSNE(n_components=2, random_state=42)
        embeddings_tsne = tsne.fit_transform(embeddings_matrix)

        # Plot t-SNE visualization
        plt.figure(figsize=(12, 10))

        # Plot t-SNE visualization with node similarity
        plt.subplot(1, 2, 1)
        plt.scatter(embeddings_tsne[:, 0], embeddings_tsne[:, 1], alpha=0.5)
        plt.title('t-SNE Visualization of Node Embeddings')
        plt.xlabel('t-SNE Component 1')
        plt.ylabel('t-SNE Component 2')

        # Plot t-SNE visualization with node similarity
        plt.subplot(1, 2, 2)
        plt.scatter(embeddings_tsne[:, 0], embeddings_tsne[:, 1], c=np.mean(similarity_matrix, axis=1), cmap='viridis', alpha=0.5)
        plt.title('t-SNE Visualization with Node Similarity')
        plt.xlabel('t-SNE Component 1')
        plt.ylabel('t-SNE Component 2')
        plt.colorbar(label='Average Node Similarity')

        plt.tight_layout()
        plt.show()

    if config.TSNE_VIS_COMPONENTS == 3:
        from mpl_toolkits.mplot3d import Axes3D

        # Reduce dimensionality using t-SNE to 3 dimensions
        tsne = TSNE(n_components=3, random_state=42)
        embeddings_tsne_3d = tsne.fit_transform(embeddings_matrix)

        # Plot 3D t-SNE visualization
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')

        # Plot 3D scatter plot
        scatter = ax.scatter(embeddings_tsne_3d[:, 0], embeddings_tsne_3d[:, 1], embeddings_tsne_3d[:, 2], c=np.mean(similarity_matrix, axis=1), cmap='viridis', alpha=0.5)
        ax.set_title('3D t-SNE Visualization with Node Similarity')
        ax.set_xlabel('t-SNE Component 1')
        ax.set_ylabel('t-SNE Component 2')
        ax.set_zlabel('t-SNE Component 3')
        fig.colorbar(scatter, label='Average Node Similarity')

        plt.show()

if __name__ == "__main__":
    

    parser = ArgumentParser()
    parser.add_argument("--config", type=str, help="Path to the config file", required=True)
    args = parser.parse_args()

    if args.config:
        # Load config dynamically
        config_module = __import__(args.config, fromlist=["config"])
        config = config_module.config
        main(config)