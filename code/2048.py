import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_board():
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board


def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4)
                   for j in range(4) if board[i][j] == 0]
    if not empty_cells:
        return False

    i, j = random.choice(empty_cells)
    board[i][j] = 2 if random.random() < 0.9 else 4
    return True


def print_board(board):
    clear_screen()
    print("2048 游戏")
    print("-" * 21)
    for row in board:
        print("|", end="")
        for cell in row:
            print(f"{cell:^4}|", end="")
        print("\n" + "-" * 21)


def transpose(board):
    return [[board[j][i] for j in range(4)] for i in range(4)]


def reverse(board):
    return [row[::-1] for row in board]


def merge_left(row):
    merged = [0] * 4
    j = 0
    for cell in row:
        if cell != 0:
            if merged[j] == 0:
                merged[j] = cell
            elif merged[j] == cell:
                merged[j] *= 2
                j += 1
            else:
                j += 1
                merged[j] = cell
    return merged


def move_left(board):
    return [merge_left(row) for row in board]


def move_right(board):
    return reverse(move_left(reverse(board)))


def move_up(board):
    return transpose(move_left(transpose(board)))


def move_down(board):
    return transpose(move_right(transpose(board)))


def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True


def has_won(board):
    for row in board:
        if 2048 in row:
            return True
    return False


def game_2048():
    board = initialize_board()
    print_board(board)

    while True:
        move = input("请输入移动方向 (w:上, s:下, a:左, d:右, q:退出): ").lower()

        if move == 'q':
            print("游戏已退出。")
            break

        old_board = [row.copy() for row in board]

        if move == 'a':
            board = move_left(board)
        elif move == 'd':
            board = move_right(board)
        elif move == 'w':
            board = move_up(board)
        elif move == 's':
            board = move_down(board)
        else:
            print("无效输入，请重试。")
            continue

        if old_board != board:
            add_new_tile(board)
            print_board(board)

            if has_won(board):
                print("恭喜你获胜！")
                break

            if is_game_over(board):
                print("游戏结束，没有可移动的位置了！")
                break
        else:
            print("无法向该方向移动！")


if __name__ == "__main__":
    game_2048()
