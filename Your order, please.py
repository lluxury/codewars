def order(sentence):
    if sentence == "":
        return sentence
    n = 0
    sentence_list = sentence.split(" ")
    res=[]
    for x in range(len(sentence_list)):
        res.append(" ")
    while n < len(sentence_list):
        #n + =1
        m = n +1
        for word in sentence_list:
            if str(m) in word:
                res[n] = word
            else:
                continue
        n+=1
        #print(res)
    return " ".join(res)

# 虽然写的比较啰嗦,还是解出来了
# 挖出一个大盲点: 列表必须要按顺序操作,append和提前建好空列表再改值是比较靠谱的方法
# 如果随机插入,不连续,需要用字典