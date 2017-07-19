def nb_year(population, percent, aug, target, years=0):
    '''
    >>> nb_year(1500, 5, 100, 5000)
    15
    '''
    if population < target:
        return nb_year(population + int(population * percent / 100) + aug, percent, aug, target, years+1)
    return years

# 不用while的标准处理方法, 两步return, 返回调用函数及设法构造参数,继续运算