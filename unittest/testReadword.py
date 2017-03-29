'''
Created on Mar 20, 2017

@author: lancer
'''
import unittest

import readword;


class Test(unittest.TestCase):


    def testReformat(self):
        self.assertEqual('PO', readword.reformat('P.O.'))
        self.assertEqual('NE', readword.reformat('N.E.'))
        self.assertEqual('NW', readword.reformat('N.W.'))
        self.assertEqual('SE', readword.reformat('S.E.'))
        self.assertEqual('SW', readword.reformat('S.W.'))
        
        self.assertEqual('MC', readword.reformat('MC01'))
        self.assertEqual('MC', readword.reformat('MC01A'))
        self.assertEqual('MC01AB', readword.reformat('MC01AB'))
        
        self.assertEqual('15TH', readword.reformat('15TH'))
        pass

    def testIsDigit(self):
        self.assertTrue(readword.isDigit('12345678'))
        self.assertTrue(readword.isDigit('15TH'))
        self.assertTrue(readword.isDigit('15D'))
        
    def testIsSymbol(self):
        self.assertTrue(readword.isSymbol('#'))
        self.assertFalse(readword.isSymbol('#12'))
        
        self.assertTrue(None == None);

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReformat']
    unittest.main()