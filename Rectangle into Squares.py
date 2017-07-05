def sqInRect(lng, wdth, recur = 0):
	if lng == wdth:
		#return (None, [lng][recur])
		return (None, [lng])[recur]		#return(None,[1])[0]

	#lessen = min(lng, wdth)
	lesser = min(lng, wdth)
	return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)

# 抄都抄不对orz, 这个代码比较深了,啃的比较累,第一个反回值应该用了元组的表示
# abs跳过较大值的想法,确实可用

# 由迭代迭出4组值
# lng	wdth recur lesser Return value 每运算一次,产生一个算式,直到条件改变,触发None
# 然后,欠了的债要否,用产生算式时变量的值带入,会产生返回列表,在算式耗完时产生的列表就是期望值
# 5,3,0,3 return [3,2,1,1] ,疑问,为什么不直接用最后面的式子来计算呢? 