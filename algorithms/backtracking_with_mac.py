from collections import deque


def backtracking_with_mac(number_of_nodes, graph, k_coloring):
    """Backtracking with forward checking algorithm base function"""
    # Define domain for each node with all possible colors at first.
    color_assignment = [[x for x in range(k_coloring)]] * number_of_nodes
    # Start with the first node
    return backtracking_with_mac_rec(0, number_of_nodes, graph, color_assignment, k_coloring)


def backtracking_with_mac_rec(index, number_of_nodes, graph, color_assignment, k_coloring):
    """Implements backtracking with forward checking algorithm using recursion."""
    # Base case: if all nodes finished return success
    if index == number_of_nodes:
        return True, color_assignment

    color_domain_of_this_node = color_assignment.copy()
    for color in color_assignment[index]:
        # Assign the color the node
        color_assignment[index] = [color]
        # Forward checking step
        inferences, mac_color_assignment = maintaining_arc_consistency(graph, color, color_assignment, number_of_nodes)
        if inferences:
            # Set the new color assignment to the values obtained from forward checking
            color_assignment = mac_color_assignment
            # Move to next nodes
            solution_found, bt_color_assignment = \
                backtracking_with_mac_rec(index+1, number_of_nodes, graph, color_assignment, k_coloring)
            # If solution found return it
            if solution_found:
                return True, bt_color_assignment
            else:
                color_assignment = color_domain_of_this_node.copy()
    # This means that there is no solution exists in this path.
    return False, color_assignment


def maintaining_arc_consistency(graph, color_assigned_to_node, color_assignment, number_of_nodes):
    """This function extracts every possible arc and add it to the queue and check it. """
    # Initializing a queue
    q = deque()
    # Extract all possible arc and them to queue
    for node in range(number_of_nodes):
        for neighbor in graph[node]:
            q.append([node, neighbor])

    # Loop on all arcs in the queue
    while q:
        # Extract first arc into head and tail
        arc = q.popleft()
        tail, head = arc[0], arc[1]
        revised, revised_color_assignment = revise(color_assignment, tail, head)
        # If no colors left in the tail of the arc.
        if len(revised_color_assignment[tail]) == 0:
            return False, []
        # If the arc has been revised then we should add all the arcs that have tail node as its head.
        if revised:
            color_assignment = revised_color_assignment
            # For all the neighbor of tail node add their arcs(in which neighbor is tail now and tail node is head)
            for neighbor in graph[tail]:
                # Don't add the head node as the tail
                if neighbor != head:
                    arc = [neighbor, tail]
                    q.append(arc)

    # All arcs are consistent
    return True, color_assignment


def revise(color_assignment, tail, head):
    """This function apply arc consistency for the given arc and return true if the tail node has been changed."""
    revised = False
    # Arc: node(Tail) -> neighbor(Head).

    # If neighbor has one color then I should remove it from tail color domain if tail also have it.
    if len(color_assignment[head]) == 1:
        if color_assignment[head][0] in color_assignment[tail]:
            # This means that the tail has the color in the head so we should remove it.
            # Remove color from the tail domain.
            temp_color_domain = color_assignment[tail].copy()
            temp_color_domain.remove(color_assignment[head][0])
            color_assignment[tail] = temp_color_domain
            revised = True
    return revised, color_assignment
