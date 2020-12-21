import click
from algorithms import backtracking


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

    solution_exits, answer = backtracking(6, graph, k_coloring)
    print(solution_exits, answer)


if __name__ == '__main__':
    solver()
