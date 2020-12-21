def backtracking_with_forward_checking(number_of_nodes, graph, k_coloring):
    """Backtracking with forward checking algorithm base function"""
    # Define domain for each node with all possible colors at first.
    color_assignment = [[x for x in range(k_coloring)]] * number_of_nodes
    # Start with the first node
    return backtracking_with_forward_checking_rec(0, number_of_nodes, graph, color_assignment, k_coloring)


def backtracking_with_forward_checking_rec(index, number_of_nodes, graph, color_assignment, k_coloring):
    """Implements backtracking with forward checking algorithm using recursion."""
    # Base case: if finished all nodes return success
    if index == number_of_nodes:
        return True, color_assignment

    color_domain_of_this_node = color_assignment[index].copy()
    for color in color_assignment[index]:
        # Check colors one by one and if safe assign to the node and move to next node
        if is_safe_assignment(index, graph, color, color_assignment):
            # Assign the color the node
            color_assignment[index] = [color]
            # Forward checking step
            inferences, fc_color_assignment = forward_checking(index, graph, color, color_assignment)
            if inferences:
                # Set the new color assignment to the values obtained from forward checking
                color_assignment = fc_color_assignment
                # Move to next nodes
                solution_found, bt_color_assignment = \
                    backtracking_with_forward_checking_rec(index+1, number_of_nodes, graph, color_assignment,
                                                           k_coloring)
                # If solution found return it
                if solution_found:
                    return True, bt_color_assignment
                else:
                    color_assignment[index] = color_domain_of_this_node.copy()
    # This means that there is no solution exists
    return False, color_assignment


def forward_checking(index_of_the_node, graph, color_assigned_to_node, color_assignment):
    for neighbor in graph[index_of_the_node]:
        # Check if this color is in the neighbor domain then remove it
        if color_assigned_to_node in color_assignment[neighbor]:
            # Remove color from the domain
            temp_color_domain = color_assignment[neighbor].copy()
            temp_color_domain.remove(color_assigned_to_node)
            color_assignment[neighbor] = temp_color_domain
            # If no colors left in the domain of the neighbor then return false.
            if len(color_assignment[neighbor]) == 0:
                return False, []
    # All neighbors have colors left in their domains.
    return True, color_assignment


def is_safe_assignment(index_of_the_node, graph, color_assigned_to_node, color_assignment):
    """Implements function is safe that make sure that the current assignment is safe(free of conflicts)"""
    # Loop on all neighbors of the node assigned and check if the value assigned to the neighbor
    # is similar to the value assigned to the node, if so return false
    for neighbor in graph[index_of_the_node]:
        # Check if my neighbor already assigned to this color
        if len(color_assignment[neighbor]) == 1:
            if color_assignment[neighbor][0] == color_assigned_to_node:
                return False
    return True
