from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *

from .puzzlesolver import PuzzleBoard, Search_algorithms


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            request.session['initial_state'] = form.cleaned_data['initial_state']
            request.session['search_algorithm'] = form.cleaned_data['search_algorithm']
            return redirect('solve')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = HomeForm()
    return render(request, 'home.html', {'form': form})


def solve(request):
    input_list = request.session.get('initial_state').split(",")
    goal_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    input_list_2D = [[0 for x in range(3)] for y in range(3)]
    goal_list_2D = [[0 for x in range(3)] for y in range(3)]

    for i in range(0, 3):
        for j in range(0, 3):
            input_list_2D[i][j] = int(input_list[(i * 3) + j])
            goal_list_2D[i][j] = int(goal_list[(i * 3) + j])

    input_tuple_2d = tuple(tuple(i) for i in input_list_2D)
    goal_tuple_2d = tuple(tuple(i) for i in goal_list_2D)

    initial_puzzle_board = PuzzleBoard.PuzzleBoard(input_tuple_2d, "initial", None, 0)
    goal_puzzle_board = PuzzleBoard.PuzzleBoard(goal_tuple_2d, None, None, 0)

    search_algorithm = request.session.get('search_algorithm')
    algorithm_name = None
    goal = None
    cost = None
    path = None
    time = None
    nodes_expanded = None
    depth = None
    states = None

    if str(search_algorithm) == "1":
        algorithm_name = "BFS"
        goal, cost, path, time, nodes_expanded, depth, states = Search_algorithms.bfs_search(initial_puzzle_board,
                                                                                             goal_puzzle_board)
    elif str(search_algorithm) == "2":
        algorithm_name = "DFS"
        goal, cost, path, time, nodes_expanded, depth, states = Search_algorithms.dfs_search(initial_puzzle_board,
                                                                                             goal_puzzle_board)
    elif str(search_algorithm) == "3":
        algorithm_name = "A* - Manhattan"
        goal, cost, path, time, nodes_expanded, depth, states = Search_algorithms.A_star_search(initial_puzzle_board,
                                                                                                goal_puzzle_board,
                                                                                                "manhattan")
    elif str(search_algorithm) == "4":
        algorithm_name = "A* - Euclidean"
        goal, cost, path, time, nodes_expanded, depth, states = Search_algorithms.A_star_search(initial_puzzle_board,
                                                                                                goal_puzzle_board,
                                                                                                "euclidean")

    context = {
        "initial_state":input_list,
        "name": algorithm_name,
        "cost": cost,
        "path": path,
        "time": time,
        "nodes_expanded": nodes_expanded,
        "depth": depth,
        "states": states
    }
    return render(request, 'solve.html', context)
