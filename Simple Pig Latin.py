def pig_it(text):
    #your code here
    res=[]
    pig_it_list=text.split()
    for word in pig_it_list:
        #if word.alpha():
        if word.encode( 'UTF-8' ).isalpha():
            word_new=word[1:]
            word_new=word_new+word[:1]+'ay'
            #print(type(word))
            #word_l=list(word)
            #list(word)
            #print(type(list(word)))
            #word_d=word[:]
            #print(type(word_d))
            #word.pop(list(word_d)[:1])
            #word.append(list(word_d)[:1])
            #word.append("ay")
            #word_r="".join(word)
            res.append(word_new)
        else:        
            res.append(word)
            break
    return ' '.join(res)


# 虽然写的很2,还是过了
# 注意区别list方法和str方法及级变量的保存方法
# list不能直接操作以后,赋值给别一个list #word_d=word[:]
# py3里面是否是字符的方法写法有变