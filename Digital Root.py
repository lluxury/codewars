def digital_root(n, j=0,s=1):
    print(str(n))
    while s:
        #for i in '0123456789':
        for i in str(n):
            #if i in str(n):
            j+=int(i)
            #print(j)
        if j<10:
            s=0
        n=j
        j=0
    return n
#print(digital_root(93))


# 犯了3个错误
# 遍历选错了对象,0-9中遍历是无穷无尽的,只在区分字母和数字时使用
# j 没有置0 ,导致小量结果正确,大量失败
# 不应该用n做判断,应该用开关
# 此外还有题意理解偏差,逻辑正确但变量处理错误