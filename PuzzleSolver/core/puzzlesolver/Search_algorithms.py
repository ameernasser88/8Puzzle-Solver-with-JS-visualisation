from collections import deque
from queue import PriorityQueue
from time import time


def metrics(puzzle_board, running_time, nodes_expanded):
    temp = puzzle_board
    path = []
    states = []
    depth = 0
    while True:
        path.append(temp.direction)
        temp_state = [list(elem) for elem in temp.state]
        temp_state = sum(temp_state, [])
        states.append(temp_state)
        temp = temp.parent
        depth += 1
        if temp is None:
            break
    depth -= 1
    path = list(reversed(path))[1:]
    states = list(reversed(states))[1:]

    return puzzle_board.state, puzzle_board.cost, path, running_time, nodes_expanded, depth, states


def bfs_search(initial_puzzle_board, goal_puzzle_board):
    nodes_expanded = 0
    starttime = time()
    frontier = deque()
    frontier.append(initial_puzzle_board)
    explored = set()
    while len(frontier) != 0:
        current_puzzle_board = frontier.popleft()

        if current_puzzle_board.__eq__(goal_puzzle_board):
            endtime = time()
            running_time = endtime - starttime
            return metrics(current_puzzle_board, running_time, nodes_expanded)

        if current_puzzle_board.state in explored:  # skip the puzzleboard with state explored before
            continue

        else:
            explored.add(current_puzzle_board.state)
            nodes_expanded += 1
            for child in current_puzzle_board.build_children():
                # if (child.state not in explored) and (if child not in frontier):  UNION
                # if not (child.state in explored):
                frontier.append(child)
    return False


def dfs_search(initial_puzzle_board, goal_puzzle_board):
    nodes_expanded = 0
    starttime = time()
    frontier = [initial_puzzle_board]
    explored = set()
    while len(frontier) != 0:
        current_puzzle_board = frontier.pop()
        if current_puzzle_board.__eq__(goal_puzzle_board):
            endtime = time()
            running_time = endtime - starttime
            return metrics(current_puzzle_board, running_time, nodes_expanded)
        if current_puzzle_board.state in explored:  # skip the puzzleboard with state explored before
            continue
        else:
            explored.add(current_puzzle_board.state)
            nodes_expanded += 1
            for child in current_puzzle_board.build_children():
                # if not (child in frontier) and not (child.state in explored):   UNION
                # if not (child.state in explored):
                frontier.append(child)
    return False


def A_star_search(initial_puzzle_board, goal_puzzle_board, distance_formula):
    nodes_expanded = 0
    starttime = time()
    frontier = PriorityQueue()
    explored = set()
    queueStates = set()
    board_info = (initial_puzzle_board.distance(goal_puzzle_board, distance_formula), initial_puzzle_board)
    frontier.put_nowait(board_info)

    while not (frontier.__sizeof__() == 0):
        current_puzzle_board = (frontier.get_nowait())[1]
        if current_puzzle_board.__eq__(goal_puzzle_board):
            endtime = time()
            running_time = endtime - starttime
            return metrics(current_puzzle_board, running_time, nodes_expanded)

        if current_puzzle_board.state in explored:
            continue
        else:
            if current_puzzle_board.state in queueStates:
                for queueTuple in frontier.queue:
                    if queueTuple[1].state == current_puzzle_board.state:
                        heuristic = queueTuple[1].distance(goal_puzzle_board, distance_formula)
                        if queueTuple[0] > (current_puzzle_board.cost + heuristic):
                            queueTuple[0] = (current_puzzle_board.cost + heuristic)
            explored.add(current_puzzle_board.state)
            queueStates.add(current_puzzle_board.state)
            nodes_expanded += 1

            for child in current_puzzle_board.build_children():
                frontier.put((child.distance(goal_puzzle_board, distance_formula) + child.cost, child))

    return False
