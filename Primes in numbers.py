from math import sqrt
def primeFactors(n):
    primes=[]
    j = 2
    while j<= 100:
        i=2
        k=sqrt(j)
        while(i<k):
            if j%i==0:
                break
            i=i+1
        if(i>k):
            #print(j)
            primes.append(j)
        j=j+1
    #print(primes)
    

    def eladuosai(n):
    l = list(range(1,n+1))
    l[0] = 0
    for i in range(2,n+1):
        if l[i-1] != 0 :
            for j in range(i*2,n+1,i):
                l[j-1] = 0
    result = [x for x in l if x != 0]
    return result
    


    vaule=[0]*len(primes)
    #print(vaule)
    result=dict(zip(primes,vaule))
    #print(result)
    while n > 1:
        for m in primes:
            while n % m==0:
                result[m]+=1
                n=n / m
    #print(result)
    pp=[]
    for x in primes:
        if result[x]>1:
            pp.append('('+str(x)+'**'+str(result[x])+')')
        elif result[x]==1:
            pp.append('('+str(x)+')')
        else:
            continue
    #print(pp)
    return "".join(pp)


# [[filter(None, (s.__setitem__(1,0), [[s.__setitem__(j,0) for  j in xrange(i*i, n+1, i)] for  i in xrange(2, int(__import__("math").sqrt(n)) + 1)], s)[2]) for s in (list(range(n+1)),)][0] for n in [10000]][0]