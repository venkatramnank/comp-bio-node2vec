import igraph as ig
import plotly.graph_objects as go


def visualize_3d(graph): 
    layt = graph.layout('kk', dim=3)  # Kamada-Kawai layout in 3D

    # Extract coordinates for plotly
    Xn = [layt[k][0] for k in range(len(layt))]
    Yn = [layt[k][1] for k in range(len(layt))]
    Zn = [layt[k][2] for k in range(len(layt))]
    Xe = []
    Ye = []
    Ze = []
    for e in graph.get_edgelist():
        Xe += [layt[e[0]][0], layt[e[1]][0], None]
        Ye += [layt[e[0]][1], layt[e[1]][1], None]
        Ze += [layt[e[0]][2], layt[e[1]][2], None]
    
    # Get node names
    if "name" in graph.vs.attributes():
        node_names = [str(node) for node in graph.vs["name"]]
    else:
        node_names = [str(node) for node in range(len(graph.vs))]

    # Create nodes and edges traces
    trace_nodes = go.Scatter3d(x=Xn,
                               y=Yn,
                               z=Zn,
                               mode='markers+text',
                               marker=dict(size=5, color='rgba(0,240,0,0.6)'),
                               text=node_names,
                               hoverinfo='text',
                               textposition="bottom center")

    trace_edges = go.Scatter3d(x=Xe,
                               y=Ye,
                               z=Ze,
                               mode='lines',
                               line=dict(width=0.5, color='rgb(25,25,25)'),
                               hoverinfo='none')

    # Plot
    plotly_layout = go.Layout(title='Interactive 3D Graph Plot',
                              titlefont=dict(size=16),
                              showlegend=False,
                              hovermode='closest',
                              margin=dict(b=20,l=5,r=5,t=40),
                              scene=dict(xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                         zaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    fig = go.Figure(data=[trace_edges, trace_nodes], layout=plotly_layout)
    fig.show()