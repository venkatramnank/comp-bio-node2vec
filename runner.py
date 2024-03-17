from graph.graph_loader import GraphLoader
from analysis.exploratory_data_analysis import GraphEDA
from configs.brain_cat import config
from visualizer.visualizer_plotly import visualize

def main():
    # Load data and build graph
    graph_loader = GraphLoader(file_location=config.FILE_LOCATION, file_type=config.FILE_TYPE, show_head=False)
    data_graph = graph_loader.load_graph()

    # Perform exploratory data analysis
    eda = GraphEDA(data_graph=data_graph)
    eda.graph_stats()

    visualize(data_graph)

if __name__ == "__main__":
    main()
