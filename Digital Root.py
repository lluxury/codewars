def digital_root(n):
    '''
    >>> digital_root(942)
    15
    '''
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n

# 返回结果可以用sum处理掉,省略j和开关判断
# 这个还是用n做判断条件了,复用
# for返回的集合由函数处理
# return n%9 or n and 9
# 这个属于吊人写的, 9进制运算, 优先级为%,and,or
# and 是为了除尽准备的, 数字运算,or取前, and取后

