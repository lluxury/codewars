#sqInRect=s=lambda a,b,r=0:(None,[a][r]if a==b else [min(a,b)]+s(min(a,b),abs(a-b),1)
sqInRect=s=lambda a,b,r=0 : (None,[a])[r] if a==b else [min(a,b)]+s(min(a,b),abs(a-b),1)

# 这也叫人写的东西?
# 原理上和递归那一个的写法类似,但是lambda不是很熟,只能领会,解释不完全
# 也是不相等的时候,返回ab的较小值,和相减的绝对值,并递归,只到相等
# if a==b取前式, 否则取后式计算