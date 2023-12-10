from queue import PriorityQueue
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_goal(board):
    return board == goal_state

def generate_successors(board):
    successors = []
    row, col = find_blank(board)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_board = [list(row) for row in board]
            new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
            successors.append(new_board)

    return successors


def astar_search(initial_state):
    visited = set()
    priority_queue = PriorityQueue()
    initial_state_tuple = tuple(map(tuple, initial_state)) 
    priority_queue.put((0 + heuristic(initial_state), 0, initial_state_tuple))
    came_from = {}

    while not priority_queue.empty():
        _, steps, current_state_tuple = priority_queue.get()
        current_state = [list(row) for row in current_state_tuple]  

        if is_goal(current_state):
            path = []
            while current_state_tuple != tuple(map(tuple, initial_state)):
                path.append(current_state)
                current_state_tuple = came_from[current_state_tuple]
            path.append(initial_state)
            path.reverse()
            return path, steps

        visited.add(current_state_tuple)
        for successor in generate_successors(current_state):
            successor_tuple = tuple(map(tuple, successor))  
            if successor_tuple not in visited:
                priority = steps + 1 + heuristic(successor)
                priority_queue.put((priority, steps + 1, successor_tuple))
                came_from[successor_tuple] = current_state_tuple

    return None, 0

def heuristic(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                row, col = divmod(board[i][j] - 1, 3)
                distance += abs(i - row) + abs(j - col)
    return distance

initial_state = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
# initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
# initial_state = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
# initial_state = [[4, 1, 3], [0, 2, 6], [7, 5, 8]]

path, steps = astar_search(initial_state)

if path:
    print("Solution found in", steps, "steps!")
    for step, state in enumerate(path):
        print("Step", step + 1)
        for row in state:
            print(row)
else:
    print("No solution found.")



