函数编程题:

### **1. 打招呼函数**

- **要求**：定义函数`say_hello`，接受一个名字参数（如`"Alice"`），返回问候语`"Hello, Alice!"`。

- 示例:

  ```python
  print(say_hello("Bob"))  # 输出: Hello, Bob!
  ```

  

### **2. 计算矩形面积**

- **要求**：定义函数`rectangle_area`，接受长和宽两个参数，返回矩形的面积。

- 示例:

  ```python
  print(rectangle_area(5, 3))  # 输出: 15
  ```

### **3. 判断奇数偶数**

- **要求**：定义函数`is_even`，接受一个整数参数，若是偶数返回`True`，否则返回`False`。

- 示例：

  ```python
  print(is_even(4))  # 输出: True
  print(is_even(7))  # 输出: False
  ```

### **4. 字符串反转**

- **要求**：定义函数`reverse_string`，接受一个字符串参数，返回它的反转结果。

- 示例：

  ```python
  print(reverse_string("abc"))  # 输出: cba
  ```

### **5. 计算列表平均值**

- **要求**：定义函数`average`，接受一个数字列表，返回列表中所有元素的平均值。

- 示例：

  ```python
  print(average([1, 2, 3, 4]))  # 输出: 2.5
  ```

- 提示:

  函数len(list)可以得到列表的长度.

### **6. 判断素数**

- **要求**：定义函数`is_prime`，接受一个整数参数，判断它是否为素数（只能被 1 和自身整除）。

- 示例：

  ```python
  print(is_prime(7))  # 输出: True
  print(is_prime(4))  # 输出: False
  ```

### **7. 摄氏度转华氏度**

- **要求**：定义函数`celsius_to_fahrenheit`，接受摄氏度温度，返回对应的华氏度温度（公式：`F = C * 1.8 + 32`）。

- 示例：

  ```python
  print(celsius_to_fahrenheit(20))  # 输出: 68.0
  ```

### **8. 统计列表中的偶数数量**

- **要求**：定义函数`count_evens`，接受一个整数列表，返回其中偶数的个数。

- 示例：

  ```python
  print(count_evens([1, 2, 3, 4, 5, 6]))  # 输出: 3
  ```

### **9. 生成斐波那契数列**

- **要求**：定义函数`fibonacci`，接受一个正整数`n`，返回前`n`个斐波那契数列（如`n=5`时返回`[0, 1, 1, 2, 3]`）。

- 示例：

  ```python
  print(fibonacci(5))  # 输出: [0, 1, 1, 2, 3]
  ```

### **10. 检查字符串是否回文**

- **要求**：定义函数`is_palindrome`，接受一个字符串，判断它是否为回文（正读和反读相同，如`"radar"`）。

- 示例：

  ```python
  print(is_palindrome("radar"))  # 输出: True
  print(is_palindrome("hello"))  # 输出: False
  ```

  