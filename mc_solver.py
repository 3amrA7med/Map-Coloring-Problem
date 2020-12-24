import click
from algorithms import backtracking, min_conflicts, backtracking_with_forward_checking, backtracking_with_mac
from utils import generate_random_graph, plot_graph


@click.command()
@click.option('-a', '--algorithm', type=click.Choice(['mc', 'bt', 'bt-fc', 'bt-mac']),
              help='Algorithm type.', required=True, default='bt')
@click.option('-k', '--k_coloring', required=True,  type=click.types.INT,
              help='Number of colors to solve this problem(only 3 and 4).', default=3)
@click.option('-n', '--number_of_nodes', default=6,
              help='Number of nodes used in the map coloring', type=click.types.INT, required=True)
def solver(algorithm, k_coloring, number_of_nodes):
    """Solver to map coloring problem"""

    print("Solving for these parameters: ", "Algorithm:=", algorithm, ", Number of colors=", k_coloring,
          ", Number of nodes=", number_of_nodes)

    # Generate a random graph.
    graph, pos, edges = generate_random_graph(number_of_nodes)
    # Plot the graph
    plot_graph(pos, edges, number_of_nodes, False, k_coloring, [])

    # Choose an algorithm to solve the graph
    if algorithm == "bt":
        solution_exits, answer = backtracking(number_of_nodes, graph, k_coloring)
        if solution_exits:
            print(answer)
            plot_graph(pos, edges, number_of_nodes, True, k_coloring, answer)
        else:
            print("No Solution exits.")
    elif algorithm == "mc":
        answer = min_conflicts(graph, number_of_nodes, k_coloring, 40)
        if answer:
            print(answer)
        else:
            print("No Solution exits.")
    elif algorithm == "bt-fc":
        solution_exits, answer = backtracking_with_forward_checking(number_of_nodes, graph, k_coloring)
        if solution_exits:
            print(answer)
        else:
            print("No Solution exits.")
    elif algorithm == "bt-mac":
        solution_exits, answer = backtracking_with_mac(number_of_nodes, graph, k_coloring)
        if solution_exits:
            print(answer)
        else:
            print("No Solution exits.")


if __name__ == '__main__':
    solver()
