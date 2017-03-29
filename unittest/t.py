'''
Created on Mar 26, 2017

@author: lancer
'''
import unittest
import random

import procBySeparator;
import dictMatch;
from fuzzywuzzy import process


class Test(unittest.TestCase):


    def testName(self):
        
        y=list(range(1,10))
        slice = random.sample(y, 5)  #从list中随机获取5个元素，作为一个片断返回  
        print (slice)  
        print (y) #原有序列并没有改变。
        pass

    def testMin(self):
        self.assertEqual(1, min([1,2,3,4,5]))
        self.assertEqual(1, min([2,3,4,5, 1]))
        self.assertEqual(5, max([1,2,3,4,5]))
        self.assertEqual(5, max([2,3,4,5, 1]))
        
    def testDictNone(self):
        aDict = {'A':1, 'B':2}
        self.assertTrue('A' in aDict)
        self.assertFalse('C' in aDict)
        
    def testFreqLess10(self):
        edict = procBySeparator.readEnglishDict()
        print (len(edict))
        data = procBySeparator.readData();
        print (len(data))
        allWords = sorted(data.keys());
        for k in allWords:
            freq = data[k];
            if freq <=10 :
                if len(k) > 23 :
                    print ('too long word, jump over', k);
                    continue;
                if procBySeparator.isWords(k) and not dictMatch.hasWord(k):
                    nearWords = dictMatch.extractBests(k)
                    print (k, freq, 'near words is ', nearWords)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()