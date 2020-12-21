def backtracking(number_of_nodes, graph, k_coloring):
    """Backtracking algorithm base function"""
    # -1 means unassigned.
    color_assignment = [-1 for x in range(number_of_nodes)]
    # Start with the first node
    return backtracking_rec(0, number_of_nodes, graph, color_assignment, k_coloring)


def backtracking_rec(index, number_of_nodes, graph, color_assignment, k_coloring):
    """Implements backtracking algorithm using recursion."""
    if index == number_of_nodes:
        return True, color_assignment
    for color in range(k_coloring):
        # Check colors one by one and if safe assign to the node and move to next node
        if is_safe_assignment(index, graph, color, color_assignment):
            # Assign the color the node
            color_assignment[index] = color
            # Move to next nodes
            solution_found, color_assignment = backtracking_rec(index+1, number_of_nodes
                                                                , graph, color_assignment, k_coloring)
            # if solution found return it
            if solution_found:
                return True, color_assignment
    # This means that there is no solution exists
    return False, color_assignment


def is_safe_assignment(index_of_the_node, graph, color_assigned_to_node, color_assignment):
    """Implements function is safe that make sure that the current assignment is safe to be assigned"""
    # Loop on all neighbors of the node assigned and check if the value assigned to the neighbor
    # is similar to the value assigned to the node, if so return false
    for neighbor in graph[index_of_the_node]:
        if color_assignment[neighbor] == color_assigned_to_node:
            return False
    return True
