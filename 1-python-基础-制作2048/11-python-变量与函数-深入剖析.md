1.为什么有时候函数能改变变量的值,有时候又不能?

是不是出了什么问题?

2.回顾: 什么时候能改变变量的值?什么时候又不能?

实例代码:

代码1: 通过函数访问来修改一些变量的值:

```
mat = [1,2,3,4]
def changeMat(matrix):
    matrix[0] = 2
    return matrix

changeMat(mat)
print(mat)
```

okay!



代码2: 修改所有mat的值:

```
mat = [1,2,3,4]
def changeMat(matrix):
    matrix = [1,2,3,5]
    return matrix

changeMat(mat)
print(mat)
```

不行? 输入的mat没有改变?



3.python变量的机制

在python内部,每个变量是一个标签,变量会贴给对应的某个值.

例:

```
x=[1,2] # x指向某个[1,2]的列表,x其实是列表首个元素的地址,而不是列表本身
x="123" # x指向某个"123"的字符串
x=123   # x指向某个数字
```





4.python函数的机制: 实参与形参

函数内的参数称为形参,函数外传入的参数称为实参.

例:

```
def test(x):
 	return x
test(1) #1是实参,x是形参
```

实参和形参只是名称问题,我们为了区分传入函数的变量和函数内部的变量而设立的而已.



5.参数是怎么传入函数的?

函数内部会复制一个形参,让其指向的内容和x指向的内容一致.



6.区分两个函数的实参和形参.



7.通过实参和形参与变量和常量的地址来解释实例代码的两个例子.

