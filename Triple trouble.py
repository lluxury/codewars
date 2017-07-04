def triple_double(num1, num2):
    '''
    >>> triple_double(45199979, 41177722899)
    1
    '''
    #return any([str(i) * 2 in num2 and str(i) * 3 in num1 for i in '0123456789'])
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])

# 模仿昨天的解法写出的1行等式,一个范围,2阶判断的模型,反回的是逻辑值
# 错误,'123'是字符串, num1,num2才是int, 概念不清,混淆了需要转换的对象