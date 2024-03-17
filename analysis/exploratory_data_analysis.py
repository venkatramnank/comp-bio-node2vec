import pandas as pd
import numpy as np
from loguru import logger
from tabulate import tabulate
from tqdm import tqdm
import igraph as ig

from configs import neuron_cc_config
from scripts import constants

FILE_LOCATION = neuron_cc_config.FILE_LOCATION


class graphEDA():
    def __init__(self, file_location, file_type, show_head=False):
        self.file_location = file_location
        self.file_type = file_type
        self.show_head = show_head
        self.data_df = self.data_reader()
        self.data_graph = self.graph_builer()

    def data_reader(self):
        logger.debug('Reading File content')
        dataframe = pd.read_csv(self.file_location, sep=constants.file_seperator[self.file_type])
        if self.show_head:
            print(tabulate(dataframe.head(), tablefmt='fancy_grid'))
        return dataframe
    
    def graph_builer(self):
        logger.debug('Building graph')
        g = ig.Graph.TupleList(self.data_df.itertuples(index=False), directed=False)
        print(g.summary())
        return g

    
    def graph_stats(self):
        # Basic graph statistics
        print("Basic Graph Statistics:")
        print("Number of nodes:", self.data_graph.vcount())
        print("Number of edges:", self.data_graph.ecount())
        # ratio of the number of edges |E| with respect to the maximum possible edges
        print("Density:", self.data_graph.density())

    

if __name__ == "__main__":
    geda = graphEDA(file_location=FILE_LOCATION, file_type='tsv', show_head=False)
    geda.graph_stats()