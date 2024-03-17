from graph.graph_loader import GraphLoader
from analysis.exploratory_data_analysis import GraphEDA
from analysis.community_detection import CommunityDetection
from visualizer.visualizer_plotly import visualize
from visualizer.visualize_plotly_3d import visualize_3d

def main(config):
    # Load data and build graph
    graph_loader = GraphLoader(file_location=config.FILE_LOCATION, file_type=config.FILE_TYPE, show_head=False)
    data_graph = graph_loader.load_graph()

    # Perform exploratory data analysis if enabled
    if config.RUN_EDA:
        eda = GraphEDA(data_graph=data_graph)
        eda.graph_stats()
        if config.RUN_DEGREE_DIST:
            eda.degree_dist()
        if config.RUN_CLUSTERING_COEFF:
            eda.clustering_coeff()
        if config.CENTRALITY:
            eda.centrality_measures()

    # Perform community detection if enabled
    if config.RUN_COMMUNITY_DETECTION:
        if config.RUN_COMMUNITY_DETECTION_PLOT:
            comm_det = CommunityDetection(data_graph,plot=True)
        else:
            comm_det = CommunityDetection(data_graph,plot=False)
        comm_det.community_detection()

    # Visualize in 3D if enabled
    if config.RUN_3D_VISUALIZATION:
        visualize_3d(data_graph)

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--config", type=str, help="Path to the config file", required=True)
    args = parser.parse_args()

    if args.config:
        # Load config dynamically
        config_module = __import__(args.config, fromlist=["Config"])
        config = config_module.Config
        main(config)
   
