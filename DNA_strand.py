
import unittest

def DNA_strand(dna):
    # code here
    str = [i for i in dna]
    #print (str)
    n = len(str)
    dst = []
    #print (n)
    #while n >0 :
    for s in str:
        if s =='A':
            s = 'T'
            dst.append(s)
            print(s)
            continue
        elif s == 'T':
            s = 'A'
            dst.append(s)
            continue
        elif s == 'G':
            s = 'C'
            dst.append(s)
            continue
        elif s == 'C':
            s = 'G'
            dst.append(s)
            continue
    return ''.join(dst)


class SumTestCase(unittest.TestCase):

    def test_summary(self):
        '''能够正确处理获得结果'''
        #self.assert_equal(digital_root(16),7)
        self.assertEqual(DNA_strand("AAAA"),"TTTT","String AAAA is")

unittest.main()