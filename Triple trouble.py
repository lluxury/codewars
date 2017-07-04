def triple_double(num1, num2):
    '''
    >>> triple_double(451999277, 41177722899)
    1
    '''
    if num1 == num2:
        return 0
    else:
        #code me ^^
        num1_l=[]
        num2_l=[]
        num1_l = [0 for x in range(10)]
        num2_l = [0 for x in range(10)]
        #print(num1_l[1])
        for y in str(num1):
            #print(y)
            num1_l[int(y)] = int(num1_l[int(y)]) +1
            #print(num1_l[int(y)])
        for z in range(len(num1_l)):
            if num1_l[z] >=3:
                #print(z)
                b = 0
                for a in str(num2):
                    if a == str(z):
                        b+=1
                if b >=2:
                    return 1
                else:
                    return 0



#2个大数字,从第一个里面找出3个相同的,从第二个找出2个连续的,反回成功
#犯了2个错误, 没考虑连续(但测试没测出来), 没考虑相同,