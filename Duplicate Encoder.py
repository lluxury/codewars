def duplicate_encode(word):
    #your code here
    print(word)
    return ''.join([')' if (w.encode('utf-8')=='(' or word.lower().count(w.lower()) >1 )  else '(' for w in word])

# 很感动,第一个自己做出来,很pythonic的代码
# 使用了返回值判断的写法,尝试了双条件判断的写法
# 涉及了 str.count(), str.lower(), 
# 使用了w.encode('utf-8') 但是看别人写的很简洁,也没有涉及字符问题,难道是因为我用ps3版本?