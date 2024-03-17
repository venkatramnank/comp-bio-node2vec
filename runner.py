from graph.graph_loader import GraphLoader
from analysis.exploratory_data_analysis import GraphEDA
from analysis.community_detection import CommunityDetection
from configs.yeast_config import config
from visualizer.visualizer_plotly import visualize
from visualizer.visualize_plotly_3d import visualize_3d

def main():
    # Load data and build graph
    graph_loader = GraphLoader(file_location=config.FILE_LOCATION, file_type=config.FILE_TYPE, show_head=False)
    data_graph = graph_loader.load_graph()
    comm_det =  CommunityDetection(data_graph)
    # Perform exploratory data analysis
    eda = GraphEDA(data_graph=data_graph)
    eda.graph_stats()
    # eda.degree_dist()
    # eda.clustering_coeff()
    comm_det.community_detection()

    # visualize_3d(data_graph)

if __name__ == "__main__":
    main()
