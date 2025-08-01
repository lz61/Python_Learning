# 四件事:
# 第一件事：创建board
# 第二件事: 给board添加两个数字
# 第三件事: 输出board
# 第四件事: 响应用户输入
def initializeBoard():
    return [
    [0,0,0,2],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

#   After Rotating:
#   [2,2,0,0]

def rotateRight90(board):
    new_board=[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    for i in range(4):
        for j in range(4):
            new_board[j][3-i]=board[i][j]
    # board = new_board
    return new_board


board=initializeBoard()
rotateRight90(board)
# board=rotateRight90(board)
print(board)




