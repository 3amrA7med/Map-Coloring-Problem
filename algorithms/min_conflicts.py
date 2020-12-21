import random
import math


def min_conflicts(graph, number_of_nodes, k_coloring, max_step):
    """Min-Conflicts algorithm function"""
    # Assign random colors to every node in the graph
    color_assignment = [random.randint(0, k_coloring-1) for x in range(number_of_nodes)]

    for i in range(max_step):
        if current_assignment_is_a_solution(number_of_nodes, graph, color_assignment):
            return color_assignment
        index = choose_a_conflicted_node(number_of_nodes, graph, color_assignment)
        value = minimize_conflicts(index, graph, color_assignment, k_coloring)
        color_assignment[index] = value

    return False


def current_assignment_is_a_solution(number_of_nodes, graph, color_assignment):
    """
    Check if their is a conflict with a neighbor, if so return False
    , if not check the next neighbor until all nodes are finished then return True
    """
    for node in range(number_of_nodes):
        for neighbor in graph[node]:
            # If there is a conflict return false
            if color_assignment[neighbor] == color_assignment[node]:
                return False
    # If we reached this line it means that there is no conflicts
    return True


def choose_a_conflicted_node(number_of_nodes, graph, color_assignment):
    """
    This function choose a random conflicted node to return it, if all randomly chosen nodes
    have no conflicts in a certain max steps then try them one by one(not random).
    """
    # This step to prevent it from choosing randomly forever
    max_steps = 20
    for step in range(max_steps):
        # Choose a random node
        randomly_chosen_node = random.randint(0, number_of_nodes-1)
        # Check if this node has conflicts, if not choose another one randomly
        for neighbor in graph[randomly_chosen_node]:
            # Check if their is a conflict with a neighbor, if so return this chosen node
            # , if not check the next neighbor
            if color_assignment[neighbor] == color_assignment[randomly_chosen_node]:
                return randomly_chosen_node

    # If randomly chosen nodes has no conflicts then choose one by checking them sequential
    print("min_conflicts sequential selection")
    for node in range(number_of_nodes):
        for neighbor in graph[node]:
            # Check if their is a conflict with a neighbor, if so return this chosen node
            # , if not check the next neighbor
            if color_assignment[neighbor] == color_assignment[node]:
                return node


def minimize_conflicts(index_of_node, graph, color_assignment, k_coloring):
    """Given a certain variable(node) this function return the color which minimizes the conflicts"""
    # Initialize it with a
    min_number_of_conflicts = math.inf
    min_conflict_color = color_assignment[index_of_node]
    for color in range(k_coloring):
        conflicts = 0
        for neighbor in graph[index_of_node]:
            # Check if their is a conflict with a neighbor, if so inc conflicts
            # , if not check the next neighbor
            if color_assignment[neighbor] == color:
                conflicts += 1
        # This means that assigning the above color resulted in lesser conflicts.
        if conflicts < min_number_of_conflicts:
            min_conflict_color = color
            min_number_of_conflicts = conflicts
    # Return the color that resulted in min conflicts in the graph.
    return min_conflict_color
