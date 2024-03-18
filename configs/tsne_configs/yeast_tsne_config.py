class config:
    # Paths
    EDGELIST_PATH = './data/yeast_snap/S-cerevisiae.txt'

    # Embedding configuration
    EMBEDDING_DIMENSIONS = 64
    WALK_LENGTH = 30
    NUM_WALKS = 200
    WORKERS = 4
    EMBEDDING_FILENAME = 'node_embeddings.txt'

    # TSNE configuration
    TSNE_VIS_COMPONENTS = 2  # Change to 3 for 3D visualization
