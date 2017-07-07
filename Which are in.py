def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

    # return sorted({sub for sub in a1 if 1})
# any 传入空可迭代对象时返回False，当可迭代对象中有任意一个不为False，则返回True
# all 传入空可迭代对象时返回True，当可迭代对象中有任意一个不为True，则返回False
# if 真有返回,if假无返回, 真假由 ()里内容决定,对a1里的每个sub反回真,假
# 不知道使用{}的原因,但是换掉会报错 ['duplicates', 'duplicates'] should equal ['duplicates']