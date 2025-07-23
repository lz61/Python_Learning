def compressList(list):
    i = 0
    j = 3
    # 开始循环
    while i < j:
        if list[i] == 0:
            k = i
            while k < j:
                list[k] = list[k+1]
                k += 1
            list[j] = 0
            j -= 1
        elif list[i] == list[i+1]:
            list[i] *= 2
            list[i+1] = 0
            i += 1
        else:
            i += 1


list = [0, 0, 0, 2]
compressList(list)
assert list == [2, 0, 0, 0]

list = [0, 0, 2, 4]
compressList(list)
assert list == [2, 4, 0, 0]

list = [0, 0, 2, 2]
compressList(list)
assert list == [4, 0, 0, 0]

list = [2, 2, 4, 4]
compressList(list)
assert list == [4, 8, 0, 0]

list = [2, 4, 4, 0]
compressList(list)
assert list == [2, 8, 0, 0]

'''
start: 0 0 0 2
end:   2 0 0 0 

start: 0 0 2 4
end:   2 4 0 0

start: 0 0 2 2
end:   4 0 0 0


start: 2 2 4 4
end:   4 8 0 0

start: 2 4 4 0
end:   2 8 0 0

'''
