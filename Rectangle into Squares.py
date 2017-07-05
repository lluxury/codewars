def sqInRect(a, b):
	if a == b:
		return None

	res = []

	while b:
		b, a = sorted([a, b])
		res +=[b]
		a, b = b, a-b

	return res


# 原理同上, 一样是返回b, 和a,b之差
# 技巧之处是 用了 b, a = sorted([a,b])保证b是较小值