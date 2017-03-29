'''
Created on Feb 4, 2017

@author: lancer
'''
import unittest

import npidb;


class Test(unittest.TestCase):


    def testName(self):
        result = npidb.getDupNpiTaxid(npidb.getConnection());
        for i in range(0, 10):
            print(i, result[i]);
        pass
    
    def testFirst(self):
        conn = npidb.getConnection()
        result = npidb.getProvideByNpiTaxid(conn, '1316983158', '382084239');
        for provider in result:
            print(provider);
            
    def testGetAddressLine(self):
        result = npidb.getAddressLine(npidb.getConnection(), 'First_line');
        for i in range(0, 10):
            print(i, result[i]);

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()