'''
Created on Mar 30, 2017

@author: lancer
'''
import unittest

import showSamples as ss;


class Test(unittest.TestCase):


    def testName(self):
        self.assertTrue(ss.isSpecWord('1ST'));
        self.assertTrue(ss.isSpecWord('22ND'));
        self.assertTrue(ss.isSpecWord('333RD'));
        self.assertTrue(ss.isSpecWord('4444TH'));
        self.assertTrue(ss.isSpecWord('55555TH'));
        self.assertTrue(ss.isSpecWord('666666FL'));
        self.assertFalse(ss.isSpecWord('A666666FL'));
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()