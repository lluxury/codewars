def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res


# 题没有理解,确实是不停的长宽想减,但是在不相等的条件下考虑
# 结尾处考虑不到, 过度考虑面积与大数优先,没注意图例
# 2个参数大小变化后互换,想到了, while函数想到了,但是还不足
# 思考方向错了,基于遍历乘积考虑的,没注意更简便的方法