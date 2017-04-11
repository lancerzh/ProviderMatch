'''
Created on Apr 11, 2017

@author: lancer
'''

import random;
import npidb;
import pymysql;


totalSample = 2000;

def getAlIds():
    conn = npidb.getConnection();
    result = []
    try:
        with conn.cursor() as cursor:
            sql = '''
                        SELECT FacilityID FROM jms_npi.Facility
                        where BillingAddrID <> 0;
            '''
            cursor.execute(sql);
            result = cursor.fetchall()
    except :
        conn.close()
        conn = None
    return result;

if __name__ == '__main__':
    allData = getAlIds();
    print ('len(allData):', len(allData));
    allIds = list(range(0, len(allData) - 1));
    allSampleIds = set(random.sample(allIds, totalSample))

    samples = []

    i = 0;
    conn = npidb.getConnection();
    try :
        
        for row in allData:
            if i in allSampleIds :
                samples.append(row[0]);
                #print (row); 
                sql = " UPDATE jms_npi.Facility set PosHolder1 = 'S' where FacilityID = " + str(row[0]);
                print (sql)
                with conn.cursor() as cursor:
                    cursor.execute(sql);
                    
                
            i += 1;
        conn.commit();
    except :
        conn.close()
        conn = None
    #print (samples)
    pass