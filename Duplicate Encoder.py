def duplicate_encode(word):
    '''
    >>> duplicate_encode("din")
    '((('
    '''
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# 最优解是判断了对的情况,其他都else,而我是判断了错的情况,
# 注意思考方向的不同,导致了复杂度的不同
# 另外发现一个小bug, doctest给的参考值需要单引号 ''的 ,""会报错