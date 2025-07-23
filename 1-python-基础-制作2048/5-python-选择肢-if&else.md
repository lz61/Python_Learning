1.if-else选择肢:

```
num=0
if x<0.9:
	num=2
else:
	num=4
```

2.语法:

```
if 条件1:
	# do sth
else:
	# do sth else
(else的部分可省略)
```



3.random.choice(x): 随机挑选x中的一个元素

4.思考: 我们要怎么样给board中的元素赋值?

思路: 

A.遍历整个board中的元素,找到那些board中未空的下标.

B.基于未空的下标,对board中的内容进行随机赋值.



5.插入: python的比较运算符与赋值运算符:



5.构造列表(i,j),从列表中挑选出我们想赋值的那个值:

```
#假设已经构建好了board
list = []
for i in range(4):
	for j in range(4):
		if(board[i][j]==0):
			list.append( [i,j] )
index = random.choice(emptyList)
board[index[0]][index[1]]=num
```



6.有没有办法实时跟踪board?现在我们想知道有关board的一切,但是手动输出board又十分麻烦.

有没有简单地输出board的办法?

7.编写程序的人早就为我们准备好了"调试"这一武器.

8.使用调试查看程序内部变量.
