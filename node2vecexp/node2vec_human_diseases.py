# Importing necessary libraries
import csv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn import manifold
import networkx as nx
from node2vec import Node2Vec
from argparse import ArgumentParser

def main(config):

    graph = nx.read_edgelist(config.EDGELIST_PATH)
    
    # Precompute probabilities and generate walks
    node2vec = Node2Vec(graph, dimensions=config.EMBEDDING_DIMENSIONS, walk_length=config.WALK_LENGTH, num_walks=config.NUM_WALKS, workers=config.WORKERS)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    # Saving embeddings for later use
    model.wv.save_word2vec_format(config.EMBEDDING_FILENAME)

    
    node2emb = {}
    with open(config.EMBEDDING_FILENAME) as fin:
        fin.readline()
        for line in fin:
            node_emb = line.strip().split()
            node2emb[node_emb[0]] = list(map(float, node_emb[1:]))

    nodes, embs = zip(*node2emb.items())
    embs = np.array(embs)
    node2name_label = {}
    with open(config.LABELS_PATH) as fin:
        fin.readline()
        csvreader = csv.reader(fin)
        for line in csvreader:
            nid, name, label = line
            node2name_label[nid] = name, label

    labels = [node2name_label[nid][1] for nid in nodes]
    all_labels = list(set(labels))

    if config.TSNE_VIS_COMPONENTS == 2:
        tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
        proj = tsne.fit_transform(embs)

        
        df = pd.DataFrame(dict(x=proj[:, 0], y=proj[:, 1], label=labels))
        groups = df.groupby('label')

        nr, nc = 4, 5
        ii = 0
        fig, axes = plt.subplots(nr, nc, figsize=(13, 17))
        for r in range(nr):
            for c in range(nc):
                for name, group in groups:
                    col, z, a = ('red', 10, 1) if name == all_labels[ii] else ('black', 1, 0.4)
                    axes[r, c].plot(group.x, group.y, marker='o', linestyle='', ms=5, color=col, zorder=z, alpha=a)
                axes[r, c].set_title(all_labels[ii])
                ii += 1

        plt.tight_layout()
        plt.show()


    elif config.TSNE_VIS_COMPONENTS==3:
        from mpl_toolkits.mplot3d import Axes3D

        # Step 4: Using t-SNE algorithm to give each disease a location in a three-dimensional map based on the disease embedding
        tsne = manifold.TSNE(n_components=3, init='pca', random_state=0)
        proj = tsne.fit_transform(embs)

        # Step 5: Visualizing disease embeddings in a series of scatter plots
        df = pd.DataFrame(dict(x=proj[:, 0], y=proj[:, 1], z=proj[:, 2], label=labels))
        groups = df.groupby('label')

        nr, nc = 4, 5
        ii = 0
        fig = plt.figure(figsize=(20, 15))
        for r in range(nr):
            for c in range(nc):
                ax = fig.add_subplot(nr, nc, ii+1, projection='3d')
                for name, group in groups:
                    col, a = ('red', 1) if name == all_labels[ii] else ('black', 0.4)
                    ax.scatter(group.x, group.y, group.z, marker='o', color=col, alpha=a)
                ax.set_title(all_labels[ii])
                ii += 1

        plt.tight_layout()
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