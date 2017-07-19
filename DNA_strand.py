import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

# 翻译功能和字符串的转换功能,但我不知道这2个方法的区别
# 过滤 和翻译
# str.maketrans(x[, y[, z]])
# str.translate(table)