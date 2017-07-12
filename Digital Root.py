from functools import reduce
def digital_root(n):
    '''
    >>> digital_root(942)
    15
    '''
    if n < 10:
        return n
        
    mylist = list(str(n))
    sum = reduce(lambda x, y: int(x)+int(y), mylist)    
    return digital_root(sum)

# reduce 不再是基本函数,需要导入
# map 接收函数,序列,反回数列 map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# reduce 接受函数,序列, reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 在函数内部不能调用自己,用了lambda ,把mylist的值分解相加
# return 可以调自己, 再判断一次,<10 或处理
# lambda x,y :int(x)+int(y) 是第一个参数,mylist是第二个
# 这个架子很好,可以后续抄用