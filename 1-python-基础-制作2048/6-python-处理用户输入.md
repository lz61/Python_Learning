1.现在我们将棋盘初始化成功,接下来的问题是:

如何处理用户输入并响应?



2.我们先来看判断用户输入的部分.

3.获取用户输入:

```
x=input()
```



4.python: 所谓"隐藏起来的数据类型"

python不仅有列表,还有数字、字符串的数据类型.

```
type(x): 得到x的类型
```



```
print(type(x)): 输出x的类型
```



5.使用选择肢作逻辑判断:

除了if-else以外,还有if-elif:

```
if 条件1:
	# do sth
elif 条件2:
	# do sth else
...
```



总和:

```
if x=="W":
	# do W th
	print("W")
elif x=="A":
	print("A")
elif x=="S":
	print("S")
elif x=="D":
	print("D")
```

