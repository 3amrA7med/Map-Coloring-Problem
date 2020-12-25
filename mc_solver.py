import click
import time
from algorithms import backtracking, min_conflicts, backtracking_with_forward_checking, backtracking_with_mac
from utils import generate_random_graph, plot_graph


@click.command()
@click.option('-a', '--algorithm', type=click.Choice(['mc', 'bt', 'bt-fc', 'bt-mac']),
              help='Algorithm type.', required=True, default='bt')
@click.option('-k', '--k_coloring', required=True,  type=click.types.INT,
              help='Number of colors to solve this problem(only 3 and 4).', default=4)
@click.option('-ms', '--max_steps', required=True,  type=click.types.INT,
              help='Number of maximum steps used by min conflicts algorithm.', default=100)
@click.option('-nr', '--number_of_runs', required=True,  type=click.types.INT,
              help='Number of runs with the same parameters.', default=1)
@click.option('-n', '--number_of_nodes', default=6,
              help='Number of nodes used in the map coloring', type=click.types.INT, required=True)
def solver(algorithm, k_coloring, number_of_nodes, max_steps, number_of_runs):
    """Map coloring problem solver"""
    if k_coloring != 3 and k_coloring != 4:
        k_coloring = 4

    print("Solving for these parameters: ", "Algorithm=", algorithm, ", Number of colors=", k_coloring,
          ", Number of nodes=", number_of_nodes, "\nNumber of runs=", number_of_runs)
    if algorithm == "mc":
        print("Max Steps used by min-conflicts algorithm=", max_steps)

    # Variables used to gather statistics
    time_sum = 0
    solution_found_count = 0

    # Main loop for each run
    for i in range(number_of_runs):
        # Generate a random graph.
        graph, pos, edges = generate_random_graph(number_of_nodes)
        if number_of_runs == 1:
            # Plot the graph only if the number of runs is 1
            plot_graph(pos, edges, number_of_nodes, False, k_coloring, [])

        # Choose an algorithm to solve the graph
        # 1-Backtracking Algorithm
        if algorithm == "bt":
            start_time = time.monotonic()
            solution_exits, answer = backtracking(number_of_nodes, graph, k_coloring)
            end_time = time.monotonic()
            time_sum += (end_time - start_time)
            if solution_exits:
                solution_found_count += 1
                if number_of_runs == 1:
                    print("Color Assignment", answer)
                    plot_graph(pos, edges, number_of_nodes, True, k_coloring, answer)
            else:
                if number_of_runs == 1:
                    print("No Solution exists.")
        # 2-Min-conflicts Algorithm
        elif algorithm == "mc":
            start_time = time.monotonic()
            answer = min_conflicts(graph, number_of_nodes, k_coloring, max_steps)
            end_time = time.monotonic()
            time_sum += (end_time - start_time)
            if answer:
                solution_found_count += 1
                if number_of_runs == 1:
                    print("Color Assignment", answer)
                    plot_graph(pos, edges, number_of_nodes, True, k_coloring, answer)
            else:
                if number_of_runs == 1:
                    print("No Solution exists.")
        # 3-Backtracking with forward checking
        elif algorithm == "bt-fc":
            start_time = time.monotonic()
            solution_exits, answer = backtracking_with_forward_checking(number_of_nodes, graph, k_coloring)
            end_time = time.monotonic()
            time_sum += (end_time - start_time)
            if solution_exits:
                solution_found_count += 1
                answer = modify_answer_format(answer, number_of_nodes)
                if number_of_runs == 1:
                    print("Color Assignment", answer)
                    plot_graph(pos, edges, number_of_nodes, True, k_coloring, answer)
            else:
                if number_of_runs == 1:
                    print("No Solution exists.")
        # 4-Backtracking with mac
        elif algorithm == "bt-mac":
            start_time = time.monotonic()
            solution_exits, answer = backtracking_with_mac(number_of_nodes, graph, k_coloring)
            end_time = time.monotonic()
            time_sum += (end_time - start_time)
            if solution_exits:
                solution_found_count += 1
                answer = modify_answer_format(answer, number_of_nodes)
                if number_of_runs == 1:
                    print("Color Assignment", answer)
                    plot_graph(pos, edges, number_of_nodes, True, k_coloring, answer)
            else:
                if number_of_runs == 1:
                    print("No Solution exists.")

    # Display statistics if number of runs is more than one
    if number_of_runs > 1:
        avg_runtime = time_sum / number_of_runs
        percentage_of_finding_a_solution = solution_found_count / number_of_runs
        print("Average Run Time = ", avg_runtime, ", Percentage of finding a solution = ",
              percentage_of_finding_a_solution * 100, "%")
    if number_of_runs == 1:
        print("Run Time = ", time_sum)


def modify_answer_format(answer, n):
    """This function modifies the answer format returned from backtracking with forward checking and with mac"""
    modified_answer = []
    for i in range(n):
        modified_answer.append(answer[i][0])
    return modified_answer


if __name__ == '__main__':
    solver()
