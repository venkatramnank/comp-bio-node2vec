# Computational Networks in Biology (Project)

Exploratory data analysis of yeast data. Multilevel Community detection of Bio-yeast.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)


## About

- [ ] Graph Convolutional Prediction of Protein Interactions
- [x] Plotly visualization
- [x] Community detection and visualization
- [x] Graph analysis (Igraph/Networkx)
- [x] Clustering coefficient
- [x] Centrality and degree distribution

## Installation

It is recommended to install using conda and pip.

```bash
conda create -n bio
conda activate bio
conda install pip
pip install -r requirements.txt
```

While installing `pycairo` please follow https://pycairo.readthedocs.io/en/latest/getting_started.html.


## Usage

### Building your own config file
Build a `config.py` with the following information
```python
class Config:
    FILE_LOCATION = '' # location of dataset
    FILE_TYPE = '' # type of dataset : csv, tsv, txt, mtx, graphml

    # Flags to enable/disable functions
    RUN_EDA = True/False
    RUN_DEGREE_DIST =True/False
    RUN_CLUSTERING_COEFF = True/False
    RUN_COMMUNITY_DETECTION = True/False
    RUN_COMMUNITY_DETECTION_PLOT = True/False
    RUN_3D_VISUALIZATION = True/False
    CENTRALITY = True/False
```

### Using runner

```bash
python -m runner --config {config file}
```

## Some visualizations

Based on `bio-yeast` data and  `plotly`.

<p align="center">
  <img src="./images/vis.gif" alt="Visualization GIF" />
</p>
<p align="center">
  <em>Visualization for Yeast</em>
</p>

<p align="center">
  <img src="./images/community_det.gif" alt="Comm det GIF" />
</p>
<p align="center">
  <em>Community Detection for Yeast</em>
</p>

## Authors

- _Venkat Ramnan K_

- _Subramnanya Keshavamurthy_