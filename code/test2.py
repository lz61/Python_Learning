def compressList(lst):
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


# 测试用例
test = [0, 2, 0, 2]
compressList(test)
print(test)  # 输出: [4, 0, 0, 0]


def test():
    x = 2
    if x == 1:
        print(1)
        return 0
    else:
        print(2)
        return 1
