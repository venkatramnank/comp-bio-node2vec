class config:
    # Paths
    EDGELIST_PATH = './data/diseasesome.edgelist'
    LABELS_PATH = './data/disease.labels'

    # Embedding configuration
    EMBEDDING_DIMENSIONS = 32
    WALK_LENGTH = 30
    NUM_WALKS = 20
    WORKERS = 4
    EMBEDDING_FILENAME = 'diseasome.emb'

    # TSNE configuration
    TSNE_VIS_COMPONENTS = 2  # Change to 3 for 3D visualization
