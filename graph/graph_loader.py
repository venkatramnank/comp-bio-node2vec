import pandas as pd
from loguru import logger
from tabulate import tabulate
import igraph as ig
import networkx as nx
from scripts import constants
from scipy.io import mmread

class GraphLoader:
    """Class for loading data and building a graph."""

    def __init__(self, file_location, file_type, show_head=False):
        """
        Initialize the GraphLoader object.

        Parameters:
        - file_location (str): The path to the input file.
        - file_type (str): The type of the input file (e.g., 'csv', 'tsv').
        - show_head (bool): Whether to display the head of the DataFrame.

        """
        self.file_location = file_location
        self.file_type = file_type
        self.show_head = show_head
        

    def load_graph(self):
        """
        Load data from the input file and build a graph.

        Returns:
        - g (igraph.Graph): The constructed graph.

        """
        if self.file_type in constants.file_seperator.keys():
            data = self._read_data_pandas()
            g = self._build_graph_pandas(data)
        elif self.file_type == 'graphml':
            g = self._read_data_graphml()
        elif self.file_type == 'mtx':
            g = self._read_data_mtx()
        elif self.file_type == 'edgelist':
            g = self._read_data_edgelist()
            
        return g

    def _read_data_pandas(self):
        """
        Read data from the input file and return it as a DataFrame.

        Returns:
        - dataframe (pd.DataFrame): The DataFrame containing the data.

        """
        logger.debug('Reading File content')
        dataframe = pd.read_csv(self.file_location, sep=constants.file_seperator[self.file_type])
        if self.show_head:
            print(tabulate(dataframe.head(), tablefmt='fancy_grid'))
        return dataframe
    
    def _read_data_graphml(self):
        logger.debug('Reading File content')
        data = ig.Graph.Read_GraphML(self.file_location)
        print(data.summary())
        return data

    def _read_data_mtx(self):
        logger.debug('Reading File content')
        data = mmread(self.file_location)
        g = nx.Graph(data)
        g = ig.Graph.from_networkx(g)
        print(g.summary())
        return g
    
    def _read_data_edgelist(self):
        logger.debug('Reading File content')
        g = nx.read_edgelist(self.file_location)
        g = ig.Graph.from_networkx(g)
        print(g.summary())
        return g

    def _build_graph_pandas(self, data_df):
        """
        Build a graph from the DataFrame.

        Parameters:
        - data_df (pd.DataFrame): The DataFrame containing the data.

        Returns:
        - g (igraph.Graph): The constructed graph.

        """
        logger.debug('Building graph')
        g = ig.Graph.TupleList(data_df.itertuples(index=False), directed=False)
        print(g.summary())
        return g