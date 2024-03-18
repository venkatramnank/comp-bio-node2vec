class Config:
    FILE_LOCATION = './data/diseasesome.edgelist'
    FILE_TYPE = 'edgelist'

    # Flags to enable/disable functions
    RUN_EDA = True
    RUN_DEGREE_DIST = False
    RUN_CLUSTERING_COEFF = False
    RUN_COMMUNITY_DETECTION = True
    RUN_COMMUNITY_DETECTION_PLOT = True
    RUN_3D_VISUALIZATION = False
    CENTRALITY = False