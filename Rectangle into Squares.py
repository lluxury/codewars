def sqInRect(lng, wdth):
    if lng !=wdth:
        sqrs = []
        while lng and wdth:
            if wdth > lng:
                lng,wdth = wdth ,lng
            sqrs.append(wdth)
            lng -=wdth
        return sqrs

# 写法类似 while循环,小值互换
# 自减的用法和不返回表示None值的做法值得学习