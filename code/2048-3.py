import random
import os
import sys

# 跨平台获取单个字符输入


def getch():
    try:
        # Windows系统
        import msvcrt
        return msvcrt.getch().decode()
    except ImportError:
        # Unix/Linux/MacOS系统
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# 处理方向键输入
def get_key():
    key = getch()

    # Windows方向键处理
    if os.name == 'nt':
        if key == '\x00' or key == '\xe0':
            next_key = getch()
            if next_key == 'H':
                return 'up'
            elif next_key == 'P':
                return 'down'
            elif next_key == 'K':
                return 'left'
            elif next_key == 'M':
                return 'right'
        return key

    # Unix/Linux/MacOS方向键处理
    else:
        if key == '\x1b':
            next1 = getch()
            if next1 == '[':
                next2 = getch()
                if next2 == 'A':
                    return 'up'
                elif next2 == 'B':
                    return 'down'
                elif next2 == 'C':
                    return 'right'
                elif next2 == 'D':
                    return 'left'
        return key


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_board():
    board = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
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
    print("\n控制: ↑(上) ↓(下) ←(左) →(右) Q(退出)")


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

    # 映射按键到移动方向
    key_mapping = {
        'up': 'up',
        'down': 'down',
        'left': 'left',
        'right': 'right',
        'q': 'quit'
    }

    while True:
        # 获取按键输入
        key = get_key().lower()

        if key not in key_mapping:
            continue

        move = key_mapping[key]

        if move == 'quit':
            print("游戏已退出。")
            break

        old_board = [row.copy() for row in board]

        if move == 'left':
            board = move_left(board)
        elif move == 'right':
            board = move_right(board)
        elif move == 'up':
            board = move_up(board)
        elif move == 'down':
            board = move_down(board)

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
            # 轻微的反馈，让用户知道按键被捕获但移动无效
            print("\a", end="", flush=True)


if __name__ == "__main__":
    game_2048()
