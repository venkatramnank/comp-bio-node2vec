import igraph as ig
import numpy as np
from loguru import logger

import igraph as ig
import plotly.graph_objects as go
from loguru import logger
import networkx as nx

def visualize(graph): 
    layt = graph.layout('kk')  # Kamada-Kawai layout

    # Extract coordinates for plotly
    Xn = [layt[k][0] for k in range(len(layt))]
    Yn = [layt[k][1] for k in range(len(layt))]
    Xe = []
    Ye = []
    for e in graph.get_edgelist():
        Xe += [layt[e[0]][0], layt[e[1]][0], None]
        Ye += [layt[e[0]][1], layt[e[1]][1], None]

    # Create nodes and edges traces
    trace_nodes = go.Scatter(x=Xn,
                            y=Yn,
                            mode='markers',
                            marker=dict(size=10, color='rgba(0,240,0,0.6)'),
                            text=[str(node) for node in range(len(graph.vs))],
                            hoverinfo='text')

    trace_edges = go.Scatter(x=Xe,
                            y=Ye,
                            mode='lines',
                            line=dict(width=0.5, color='rgb(25,25,25)'),
                            hoverinfo='none')

    # Plot
    plotly_layout = go.Layout(title='Interactive Graph Plot',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20,l=5,r=5,t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

    fig = go.Figure(data=[trace_edges, trace_nodes], layout=plotly_layout)
    fig.show()

