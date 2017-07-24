from collections import Counter

def fac(n):
    # print(n)
    maxq =int(n ** .5)
    d, q = 1, 2+n % 2
    while q <= maxq and n % q:
        q = 1+ d*4 - d//2*2
        d += 1
    res = Counter()
    if q <= maxq:
        res[q] = 1
        res += fac(n//q)
    else: res[n] = 1
    print(res)
    return res

def primeFactors(n):
    return ''.join(('({})' if m == 1 else '({}**{})')
        .format(p, m) for p, m in sorted(fac(n).items()))

# 导入collections模块使用记数器功能,我字典的思路还是对的
# q = 1+ d*4 - d//2*2 貌似是个算法,但是看不懂
# Counter返回的是个字典? Counter 最初Counter() .. Counter({17: 1, 11: 1})
# return的使用方法经典, 根据结果的不同,套用不同格式, 调用排序过的函数返回值组
# while的双重条件判断, fac的自身调用构成迭代 res += fac(n//q)
# if是独立的, 先过Counter(),primeFactors(30),fac(30),
# maxq=5,d=1,q=2,res,if判断,返回fec(15),产生新的maxq,d,q
# q>maxq 触发非迭代分支,开始有返回值,消除各fac()函数,返回值存Counter,迭代结果列表
# 使用for读取排序后的迭代结果列表

