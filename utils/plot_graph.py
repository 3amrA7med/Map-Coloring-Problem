import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(pos, edges, number_of_nodes, colors_assigned, k_coloring, colors_assignment):
    """This function takes graph information and plot it"""
    # Initialize a graph
    g = nx.Graph()

    # Add nodes with their position to the graph
    for n in range(number_of_nodes):
        g.add_node(n, pos=(pos[n][0], pos[n][1]))

    # Add edges between nodes
    for e in edges:
        g.add_edge(e[0], e[1])

    # Add colors for nodes if colors are assigned
    color_map = []
    k3_coloring = ['red', 'blue', 'yellow']
    k4_coloring = ['red', 'blue', 'yellow', 'green']

    if colors_assigned:
        if k_coloring == 3:
            for n in range(number_of_nodes):
                color_map.append(k3_coloring[colors_assignment[n]])
        else:
            for n in range(number_of_nodes):
                color_map.append(k4_coloring[colors_assignment[n]])

    pos = nx.get_node_attributes(g, 'pos')

    # Draw graph
    if not colors_assigned:
        nx.draw(g, pos, with_labels=True)
    else:
        nx.draw(g, pos, with_labels=True, node_color=color_map)
    plt.show()
