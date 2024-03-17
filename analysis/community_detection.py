import pandas as pd
import numpy as np
from loguru import logger
from tabulate import tabulate
from tqdm import tqdm
import igraph as ig
import matplotlib.pyplot as plt
from configs import neuron_cc_config
from scripts import constants
import plotly.graph_objs as go
import colorsys

class CommunityDetection:
    def __init__(self, graph, plot=False):
          self.data_graph = graph
          self.plot = plot


    def _vis(self):
         # Create a layout for the graph (3D)
            layout = self.data_graph.layout_fruchterman_reingold(dim=3)

            # Define a color mapping function
            def generate_color(idx):
                hue = idx / len(self.communities)
                saturation = 0.7
                value = 0.9
                rgb = colorsys.hsv_to_rgb(hue, saturation, value)
                color = f"rgb({int(rgb[0] * 255)}, {int(rgb[1] * 255)}, {int(rgb[2] * 255)})"
                return color

            # Create traces for each community
            traces = []
            for idx, community in enumerate(self.communities):
                node_indices = community
                trace = go.Scatter3d(
                    x=[layout[k][0] for k in node_indices],
                    y=[layout[k][1] for k in node_indices],
                    z=[layout[k][2] for k in node_indices],
                    mode="markers",
                    marker=dict(size=5, color=generate_color(idx), opacity=0.7, line=dict(color="rgb(0,0,0)", width=0.5)),
                    name=f"Community {idx+1}"
                )
                traces.append(trace)

            # Create layout for the plot
            plot_layout = go.Layout(
                title="Communities in 3D",
                showlegend=True
            )

            # Create figure
            fig = go.Figure(data=traces, layout=plot_layout)

            # Show the interactive plot
            fig.show()

    def community_detection(self):
            self.communities = self.data_graph.community_multilevel()
            for idx, community in enumerate(self.communities):
                print(f"Community {idx+1}: {community}")
            if self.plot:
                self._vis()