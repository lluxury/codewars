def order(sentence):
    '''
    >>> order("is2 Thi1s T4est 3a")
    'Thi1s is2 3a T4est'
    '''
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)

# 比较正常的解法 判空返回
# 分割字符串, 直接写了范围1,10, 貌似题目有给,我没仔细看
# 按序匹配,插入列表,但是并没有空值的处理,我理解错了?
# 论读清楚题的重要性,难度下除指数级