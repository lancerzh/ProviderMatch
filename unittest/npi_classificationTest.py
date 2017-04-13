'''
Created on Apr 13, 2017

@author: lancer
'''
import unittest

import npi_classification as nc;


class Test(unittest.TestCase):


    def testName(self):
        trainData, testData, trainDataY, testDataY = nc.fetch_from_file(10);
        print ('trainData', trainData)
        print ('testData', testData)
        print ('trainDataY', trainDataY)
        print ('testDataY', testDataY)
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()