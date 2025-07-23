1.为什么有时候函数能改变变量的值,有时候又不能?

是不是出了什么问题?

2.实例代码:

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

不行?



