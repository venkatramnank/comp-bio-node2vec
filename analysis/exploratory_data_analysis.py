import pandas as pd
import numpy as np
from loguru import logger
from tabulate import tabulate
from tqdm import tqdm
import igraph as ig
import matplotlib.pyplot as plt
from configs import neuron_cc_config
from scripts import constants
import plotly.graph_objs as go
import colorsys

class GraphEDA:
    """Class for performing exploratory data analysis (EDA) on a graph."""

    def __init__(self, data_graph):
        """
        Initialize the GraphEDA object.

        Parameters:
        - data_graph (igraph.Graph): The graph object.

        """
        self.data_graph = data_graph

    def graph_stats(self):
        """
        Print basic statistics about the graph.

        """
        # Basic graph statistics
        print("Basic Graph Statistics:")
        print("Number of nodes:", self.data_graph.vcount())
        print("Number of edges:", self.data_graph.ecount())
        # ratio of the number of edges |E| with respect to the maximum possible edges
        print("Density:", self.data_graph.density())

    def degree_dist(self):
        """
        Degree Distribution of graph
        """
        # Get the degree sequence of the graph
        degree_sequence = self.data_graph.degree()

        # Plot the histogram
        plt.figure(figsize=(8, 6))
        plt.hist(degree_sequence, bins=range(min(degree_sequence), max(degree_sequence) + 2, 1), color='blue', edgecolor='black', alpha=0.7)
        plt.title('Degree Distribution Histogram')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def clustering_coeff(self):
        """
        Clusetering coeff
        """
        print("\nClustering Coefficient:")
        print("Average clustering coefficient:", self.data_graph.transitivity_avglocal_undirected())

    def centrality_measures(self):
        """
        Centrality measures
        """
        print("\nCentrality Measures:")
        print("Degree centrality:", self.data_graph.degree())
        print("Betweenness centrality:", self.data_graph.betweenness())
        print("Closeness centrality:", self.data_graph.closeness())
        print("Eigenvector centrality:", self.data_graph.evcent())

    