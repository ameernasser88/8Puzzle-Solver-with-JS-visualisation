
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


class PuzzleBoard:
    def __init__(self, state, direction, parent, cost=0):
        self.state = state
        self.direction = direction
        self.parent = parent
        self.cost = cost


    def __eq__(self, other_puzzle_board):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] != other_puzzle_board.state[i][j]:
                    return False
        return True

    def __lt__(self, other_puzzle_board):
        return True

    def zeroTilePosition(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    return [i, j]

    def build_children(self):

        i = self.zeroTilePosition()[0]
        j = self.zeroTilePosition()[1]

        children = []

        # case 1: move up
        if i != 0:
            # print("up")
            new_state = [list(elem) for elem in self.state]
            temp = new_state[i - 1][j]
            new_state[i - 1][j] = 0
            new_state[i][j] = temp
            tuple_2d = tuple(tuple(i) for i in new_state)
            children.append(PuzzleBoard(tuple_2d, "up", self, self.cost + 1))

        # case 2: move down
        if i != 2:
            # print("down")
            new_state = [list(elem) for elem in self.state]
            # print("*"*10)
            # print(new_state)
            temp = new_state[i + 1][j]
            new_state[i + 1][j] = 0
            new_state[i][j] = temp
            tuple_2d = tuple(tuple(i) for i in new_state)
            children.append(PuzzleBoard(tuple_2d, "down", self, self.cost + 1))

        # case 3: move left
        if j != 0:
            # print("left")
            new_state = [list(elem) for elem in self.state]
            temp = new_state[i][j - 1]
            new_state[i][j - 1] = 0
            new_state[i][j] = temp
            tuple_2d = tuple(tuple(i) for i in new_state)
            children.append(PuzzleBoard(tuple_2d, "left", self, self.cost + 1))
        # case 4: move right
        if j != 2:
            # print("right")
            new_state = [list(elem) for elem in self.state]
            temp = new_state[i][j + 1]
            new_state[i][j + 1] = 0
            new_state[i][j] = temp
            tuple_2d = tuple(tuple(i) for i in new_state)
            children.append(PuzzleBoard(tuple_2d, "right", self, self.cost + 1))

        return children



    def distance(self, goalPuzzleBoard , distance_formula):
        distance = 0
        goal_puzzle_board_state = [list(elem) for elem in goalPuzzleBoard.state]

        for i in range(0, 3):
            for j in range(0, 3):
                goal_i, goal_j = index_2d(goal_puzzle_board_state, self.state[i][j])
                if distance_formula == "manhattan":
                    distance = distance + (abs(i - goal_i) + abs(j - goal_j))
                else:
                    distance = distance + (pow(pow(i - goal_i, 2) + pow(j - goal_j, 2), 0.5))
        return distance


