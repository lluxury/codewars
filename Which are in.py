def in_array(array1, array2):
    r = []
    t = []
    for x in array1:
        for y in array2:
            if x in y:
                #z=set(x)
                #print (x)
                r.append(x)
                for z in r:
                #r.sort()
                #for z in r:
                    if z not in t:
                        t.append(z)
                        t.sort()
        continue
    # your code
    return t

# 巨蠢流解法,好坏是解出来了
# 偷了别人一个用法,完成了list去重