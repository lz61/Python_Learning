board=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# 随机寻找两个位置,生成两个2,4: 由随机数决定

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
