def sum_two_smallest_numbers(numbers):
    '''
    >>> sum_two_smallest_numbers([8, 5, 12, 18, 22])
    13
    '''
    #your code here
    #if type(numbers) != list:
    #    pass
    #for x in numbers:
    #    if x > 0:
        #if type(eval(x)) != float
    numbers_1 = numbers[:]
    #numbers_2 = numbers_1.sort()
    numbers_1.sort() 
    #print(numbers_1[0])
    x = int(numbers_1[0]) + int(numbers_1[1])
    #print(x)
    return x


# 思路还算正确,排序并相加,没考虑多于4个的限制,没考虑空或浮点
# 还是写的很啰嗦啊,但是不知道保留原list的要求是怎么完成的
# 把一个列表的排序赋值给另一个列表的写法是错误的,要注意