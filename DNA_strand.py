pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    '''
    DNA_strand("AAAA")
    "TTTT"
    '''
    return ''.join([pairs[x] for x in dna])

# 标准的解法,构造一个表,用值来替代键返回