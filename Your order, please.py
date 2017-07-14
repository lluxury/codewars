def order(sentence):
    '''
    >>> order("is2 Thi1s T4est 3a")
    'Thi1s is2 3a T4est'
    '''
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# 又是传说中的一行过,我啥时候能写出这么叼的代码呢
# 反回,拼接,排序,列表,按关键字排 x ,x变量值,ps2的用法,这种的还是要多写
# 学到了2个方法 用key排序,用isdigit判断数字
# : 后面全部是表达式,为了生成一个合适的排序关键字
# filter()也接收一个函数和一个序列 把传入的函数依次作用于每个元素 根据返回值是True还是False决定保留还是丢弃该元素