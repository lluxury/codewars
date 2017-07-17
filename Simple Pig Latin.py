def pig_it(text):
    return ' '.join([x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split()])

# 其实就是2个字符串过滤拼接,比移动方便多了,思路巧妙
# a if xx else b, 单行判断处理异常字符,xx为判断,标准套路