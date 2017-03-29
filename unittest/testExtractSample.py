'''
Created on Mar 29, 2017

@author: lancer
'''
import unittest

import extractSample as es


class Test(unittest.TestCase):


    def testName(self):
        
        top10 = es.extractTopFreq(10)
        print (top10)
        self.assertEqual(10, len(top10))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()