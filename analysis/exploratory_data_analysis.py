import pandas as pd
import numpy as np
from loguru import logger
from tabulate import tabulate
from tqdm import tqdm
import igraph as ig

from configs import neuron_cc_config
from scripts import constants


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
        print("\nDegree Distribution:")
        print("Average degree:", sum(self.data_graph.degree()) / self.data_graph.vcount())
        print("Degree histogram:", self.data_graph.degree_distribution().bins())

    def clustering_coeff(self):
        """
        Clusetering coeff
        """
        print("\nClustering Coefficient:")
        print("Average clustering coefficient:", self.data_graph.transitivity_avglocal_undirected())
    
