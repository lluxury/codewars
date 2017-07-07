def in_array(array1, array2):
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res

# 总算接近正常答案了,不容易
# 学到了同时对目标和结果判断的去重方式