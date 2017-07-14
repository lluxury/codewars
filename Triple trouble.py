def triple_double(num1, num2):
    '''
    >>> triple_double(45199979, 41177722899)
    1
    '''
    #return any([str(i) * 2 in num2 and str(i) * 3 in num1 for i in '0123456789'])
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])

# 模仿昨天的解法写出的1行等式,一个范围,2阶判断的模型,反回的是逻辑值
# 错误,'123'是字符串, num1,num2才是int, 概念不清,混淆了需要转换的对象



+def sqInRect(lng, wdth, recur = 0):
 -    if a == b:         +    if lng == wdth:
 -        return None         +        #return (None, [lng][recur])
 +        return (None, [lng])[recur]        #return(None,[1])[0]
            
 -    res = []         +    #lessen = min(lng, wdth)
 +    lesser = min(lng, wdth)
 +    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)



def digital_root(n, j=0):
   #print(str(n))
   while n >10:
       for i in '0123456789':
           if i in str(n):
               j+=int(i)
               #print(i)
               n=j               
   return j
   
    
def     digital_root(n, j=0,recur =0):
    if j >10 :


def digital_root(n, j=0,s=1):
    print(str(n))
    while s:
        #for i in '0123456789':
        for i in str(n):
            #if i in str(n):
            j+=int(i)
            print(j)
        if j<10:
            s=0
        n=j
    return n
print(digital_root(93))
