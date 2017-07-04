def sum_two_smallest_numbers(numbers):
    '''
    >>> sum_two_smallest_numbers([8, 5, 12, 18, 22])
    13
    '''
    return sum(sorted(numbers)[:2])


# 叼人你为什么这么叼呢
# 据说速度不快,目前顾及不了这么多
# 测试感觉list被改变了,待验证