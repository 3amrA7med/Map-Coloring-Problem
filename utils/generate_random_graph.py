import random
import math


def generate_random_graph(number_of_nodes):
    """This function generate random graph(test case) given the number of nodes"""
    # Add a seed to compare between algorithms with the same graphs
    # random.seed(1)
    nodes = []
    # Generate random points
    for i in range(number_of_nodes):
        x = random.random()
        y = random.random()
        # print("Point#", i, "=>(", x, ",", y, ")")
        nodes.append([x, y])

    # Generate list of lists, each list corresponds to a node holds the other nodes not checked yet
    nodes_not_checked = [[x for x in range(number_of_nodes)]] * number_of_nodes
    count = 0
    for n in range(number_of_nodes):
        temp = nodes_not_checked[n].copy()
        temp.remove(count)
        nodes_not_checked[n] = temp.copy()
        count += 1
    # Initialize empty edge list
    edges = []
    # Pick a random node and add an edge to it while we can add edges.
    while can_add_edge(nodes_not_checked, number_of_nodes):
        # Choose a random node
        random_node = random.randint(0, number_of_nodes - 1)
        edges, nodes_not_checked = add_edge(random_node, nodes_not_checked, nodes, edges)

    # Return graph in the form of adjacency list and the position of the nodes
    return prepare_adjacency_list(edges, number_of_nodes), nodes, edges


def prepare_adjacency_list(edges, number_of_nodes):
    """This function prepare adjacency list from the current info and return it"""
    graph = [[]]*number_of_nodes
    for e in edges:
        temp = graph[e[0]].copy()
        temp.append(e[1])
        graph[e[0]] = temp.copy()
        temp = graph[e[1]].copy()
        temp.append(e[0])
        graph[e[1]] = temp.copy()
    return graph


def can_add_edge(nodes_not_checked, number_of_nodes):
    """This function returns false if all nodes are checked(No elements in the given list of lists)"""
    for i in range(number_of_nodes):
        if len(nodes_not_checked[i]) != 0:
            return True
    return False


def add_edge(node_to_connect, list_of_nodes_not_checked, nodes, edges):
    """This function is responsible for adding edges in the graph."""
    # done variable tells me if I added an edge to this node or no edges can be added
    done = False

    while not done:
        # If no remaining possible values to a specific node end function.
        if len(list_of_nodes_not_checked[node_to_connect]) == 0:
            done = True
            continue
        # First computes minimum distance between current node and all other nodes not checked
        min_distance = math.inf
        min_node_number = -1
        for node in list_of_nodes_not_checked[node_to_connect]:
            # distance = sqrt((x1-x2)^2 + (y1-y2)^2)
            distance = math.sqrt((nodes[node_to_connect][0]-nodes[node][0])**2 +
                                 (nodes[node_to_connect][1]-nodes[node][1])**2)
            if min_distance > distance:
                min_distance = distance
                min_node_number = node

        # Remove chosen node from the list and remove node_to_connect from the chosen node list
        temp = list_of_nodes_not_checked[node_to_connect].copy()
        temp.remove(min_node_number)
        list_of_nodes_not_checked[node_to_connect] = temp.copy()

        temp = list_of_nodes_not_checked[min_node_number].copy()
        temp.remove(node_to_connect)
        list_of_nodes_not_checked[min_node_number] = temp.copy()

        # Create a temp edge variable and check if you can add it to the edges of the graph
        temp_edge = [node_to_connect, min_node_number]
        not_intersecting = True
        # Now see if the edge we are connecting is intersecting any other existing edge
        for e in edges:
            if not (e[0] in temp_edge) and not (e[1] in temp_edge):
                if do_intersect(nodes[temp_edge[0]], nodes[temp_edge[1]], nodes[e[0]], nodes[e[1]]):
                    not_intersecting = False
                    break
        # If not intersected with other edges add it
        if not_intersecting:
            done = True
            edges.append(temp_edge)
    return edges, list_of_nodes_not_checked


def do_intersect(p1, q1, p2, q2):
    """This function checks if 2 lines intersect """
    # Find all orientation
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case.
    if o1 != o2 and o3 != o4:
        return True

    # Special cases, If the points are co-linear.
    if o1 == 0 and on_segment(p1, q1, p2):
        return True
    if o2 == 0 and on_segment(p1, q1, q2):
        return True
    if o3 == 0 and on_segment(p2, q2, p1):
        return True
    if o4 == 0 and on_segment(p2, q2, q1):
        return True

    # No intersection
    return False


def orientation(p, q, r):
    """This function checks orientation and return 0/1/-1 for co-linear/clockwise/counterclockwise"""
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def on_segment(p, q, r):
    """This function check if r is in the range of p and q"""
    if max(p[0], q[0]) >= r[0] >= min(p[0], q[0]) and max(p[1], q[1]) >= r[1] >= min(p[1], q[1]):
        return True
    return False
