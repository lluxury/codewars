def primeFactors(n):    
    class Counter(dict):
            def __missing__(self, key):
                return 0
    #queue=Counter()
    def pf(n):
        queue=Counter()
        f=2
        queue[f]=0
        while f*f<=n:
            while not n%f:
                yield f
                n//=f
                #queue[f]=0
                queue[f]+=1
            f+=1
        if n>1:
            yield n
        #print((dict(queue)))
        return queue
    
    #print(list(pf(7775460)))
    # for x in(list(pf(7775460))):
    #     print(x)
    mylist=list(pf(n))
    myset=set(mylist)
    mylist2=sorted(myset)
    # print(mylist2)
    # mydict={}
    # print(myset)
    # for item in myset:
    #     #print(item,mylist.count(item))
    #     mydict[item]=mylist.count(item)
    # print(mydict)
    
    pp=[]
    for item in mylist2:
        if mylist.count(item) > 1:
            pp.append('('+str(item)+'**'+str(mylist.count(item))+')')
        elif mylist.count(item) == 1:
            pp.append('('+str(item)+')')
        else:
            continue
    #print(pp)
    return "".join(pp)  
print(primeFactors(7775460))

# 遇到了超时,遇到了内存溢出,算数题果然应该好好做一下
# 写的再乱再差也是我的痕迹