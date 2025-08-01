# 四件事:
# 第一件事：创建board
# 第二件事: 给board添加两个数字
# 第三件事: 输出board
# 第四件事: 响应用户输入

# 最后几件事:
# 1.判断用户输入是否有效
# 2.判断游戏失败
def initializeBoard():
    return [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

# 给board创建数字的函数
def addNumToBoard(board):
    # 随机寻找1个位置,生成两个2,4: 由随机数决定
    import random
    # 函数是什么? y=f(x)
    # 编程语言的复杂性: 放进去一个x,经过函数之后出来y
    # 可以放进去的变量可以是多个,出来的变量也可以是多个
    # random()
    # 函数格式: 函数名()
    x = random.random() # 输入: 什么都没有 输出: 0-1 中间随机的一个数
    num = 0
    # 控制判断: if 和 else
    if x<0.8:
        num = 2
    else:
        num = 4

    # board[0][0] - board[3][3]
    # 记住的下标是: [1,0],[1,1],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[3,3]
    # [i,j]: board[i][j] == 0
    # 怎么判断一个数等等于0?
    list = []
    for i in range(4):
        for j in range(4):
            if board[i][j]==0:
                # 构建一个列表，把[i,j]放进去
                list.append([i,j])
    # random.choice(): 从列表中随机选出一个元素
    # 输入:一个列表
    # 输出:列表中的随机一个元素
    # t=[随机的i,随机的j]
    # t[0]: i
    # t[1]: j
    # 最好在起名的时候： 不要起一些随便的名字
    index=random.choice(list)
    board[index[0]][index[1]]=num

def outputBoard(board):
    # 循环套循环:
    print("2048 游戏")
    print("---------------------")

    # i: 0-3
    # j: 0-3
    for i in range(4):
        for j in range(4):
            print("|",board[i][j],end="  ")
        print("|")
        print("---------------------")

def userInput():
    # 响应用户输入
    x=input()
    return x
    # if-else,新关键字: elif(else if)
    # if x=="W":
    #     # do W thing:
    #     print("W")
    # elif x=="A":
    #     print("A")
    # elif x=="S":
    #     print("S")
    # elif x=="D":
    #     print("D")
    # elif x=="Q":
    #     print("Q")

# 给出一个列表,全体往左压缩
def compressListLeft(lst):
    i = 0
    j = len(lst) - 1  # 修改：使用列表长度计算j
    
    while i < j:
        if lst[i] == 0:
            # 原有的前导零处理逻辑
            k = i
            while k < j:
                lst[k] = lst[k+1]
                k += 1
            lst[j] = 0
            j -= 1
        else:
            # 改进：查找下一个非零元素并合并
            next_non_zero = None
            for m in range(i+1, len(lst)):
                if lst[m] != 0:
                    next_non_zero = m
                    break
            
            if next_non_zero is not None and lst[i] == lst[next_non_zero]:
                # 合并当前元素和下一个非零元素
                lst[i] *= 2
                # 将后续元素前移
                for k in range(next_non_zero, len(lst)-1):
                    lst[k] = lst[k+1]
                lst[-1] = 0  # 末尾补零
                j -= 1  # 更新j，因为合并后列表有效长度减少
            i += 1  # 无论是否合并，i都要递增

def leftMoveBoard(board):
    for i in range(len(board)):
        compressListLeft(board[i])

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
    return new_board

# 未经测试的函数
def isSameBoard(board,new_board):
    for i in range(4):
        for j in range(4):
            if board[i][j]!=new_board[i][j]:
                return False
    return True

board=initializeBoard()
addNumToBoard(board)
addNumToBoard(board)
outputBoard(board)

# 设计；
# while循环:
# 让用户输入WASD以及Q中的任意一个字符,如果输入的是Q,退出循环,游戏结束
# 假设用户输入的就是这五个字符中的一个
key = userInput()

while key!="Q" and key!="q":
    # 执行循环
    if key == "A" or key == 'a':
        # Left move the board
        leftMoveBoard(board)
        # 新生成一个元素
        addNumToBoard(board)
        outputBoard(board)

    # downside
    elif key== "S" or key== 's':
        board = rotateRight90(board)
        leftMoveBoard(board)
        board = rotateRight90(board)
        board = rotateRight90(board)
        board = rotateRight90(board)
        addNumToBoard(board)
        outputBoard(board)
        # rotateRight90(board)

    elif key == "D" or key == "d":
        board = rotateRight90(board)
        board = rotateRight90(board)
        leftMoveBoard(board)
        board = rotateRight90(board)
        board = rotateRight90(board)
        addNumToBoard(board)
        outputBoard(board)
        
    elif key == "W" or key == "w":
        board = rotateRight90(board)
        board = rotateRight90(board)
        board = rotateRight90(board)
        leftMoveBoard(board)
        board = rotateRight90(board)
        addNumToBoard(board)
        outputBoard(board)     

    key = userInput()
