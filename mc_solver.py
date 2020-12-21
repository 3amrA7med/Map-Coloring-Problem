import click
from algorithms import backtracking
from algorithms import min_conflicts


@click.command()
@click.option('-a', '--algorithm', type=click.Choice(['mc', 'bt', 'bt-fc', 'bc-mac']),
              help='Algorithm type.', required=True, default='bt')
@click.option('-k', '--k_coloring', required=True,  type=click.types.INT,
              help='Number of colors to solve this problem(only 3 and 4).', default=3)
@click.option('-n', '--number_of_nodes', default=7,
              help='Number of nodes used in the map coloring', type=click.types.INT, required=True)
def solver(algorithm, k_coloring, number_of_nodes):
    """Solver to map coloring problem"""
    print("Solving for these parameters: ", "Algorithm:=", algorithm, ", Number of colors=", k_coloring,
          ", Number of nodes=", number_of_nodes)

    # Define adjacency list graph to test it
    graph = [
        [1, 2],
        [0, 2, 3],
        [0, 1, 3, 4, 5],
        [1, 2, 4],
        [2, 3, 5],
        [2, 4]
    ]
    if algorithm == "bt":
        solution_exits, answer = backtracking(6, graph, k_coloring)
        if solution_exits:
            print(answer)
        else:
            print("No Solution exits.")
    elif algorithm == "mc":
        answer = min_conflicts(graph, 6, k_coloring, 40)
        if answer:
            print(answer)
        else:
            print("No Solution exits.")
    elif algorithm == "bt-fc":
        pass


if __name__ == '__main__':
    solver()
