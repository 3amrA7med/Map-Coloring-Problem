import click


@click.command()
@click.option('-a', '--algorithm', type=click.Choice(['mc', 'bt', 'bt-fc', 'bc-mac']),
              help='Algorithm type.', required=True, default='mc')
@click.option('-k', '--k_coloring', required=True,  type=click.types.INT,
              help='Number of colors to solve this problem(only 3 and 4).', default=3)
@click.option('-n', '--number_of_nodes', default=7,
              help='Number of nodes used in the map coloring', type=click.types.INT, required=True)
def solver(algorithm, k_coloring, number_of_nodes):
    """Solver to map coloring problem"""
    if k_coloring == 3:
        pass
    else:
        pass
    print(algorithm, k_coloring)


if __name__ == '__main__':
    solver()
