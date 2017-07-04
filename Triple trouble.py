def triple_double(num1, num2):
    '''
    >>> triple_double(4519979, 41177722899)
    1
    '''
    for x in range(10):
        if str(x)*3 in str(num1):
            if str(x)*2 in str(num2):
                return 1
    return 0

print(triple_double(45199979, 45199979))


#用 str(x)*3的方法来表示3个连续的值, 这点要学习
#用2阶if判断表示包容关系,只用一套变量,大大省略代码