def multiply(a, b):
  return a * b


multiply = lambda x, y: x * y
# multiply(1,5)
# 很奇妙的用法

multiply = __import__('operator').mul



multiply = int.__mul__


import operator
multiply = operator.mul
# multiply(1,5)
