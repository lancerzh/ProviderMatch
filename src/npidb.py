'''
Created on Apr 12, 2016

@author: lancer
'''
import pymysql

connection = None;

def getConnection():
    connection = pymysql.connect(host='localhost',
                     user='npi',
                     password='npi',
                     db='jms_npi',
                     charset='utf8',
                     cursorclass=pymysql.cursors.Cursor)
    return connection;

def getDupNpiTaxid(conn):
    result = []
    try:
        with conn.cursor() as cursor:
            sql = '''
                        select * from (
                            SELECT count(*) ccc, NPI, TAXID FROM jms_npi.PROV_NO_NET
                            where NPI <> ''
                            group by NPI, TAXID ) as a
                        order by a.ccc desc;
            '''
            cursor.execute(sql);
            result = cursor.fetchall()
    except :
        conn.close()
        conn = None
    return result;

def getProvideByNpiTaxid(conn, npi, taxid):
    result = []
    try:
        with conn.cursor() as cursor:
            sql = '''
                    SELECT * 
                    FROM jms_npi.PROV_NO_NET
                    where NPI = %s
                    and taxid = %s
                    ;
            '''
            cursor.execute(sql, (npi, taxid));
            result = cursor.fetchall()
    except :
        conn.close()
        conn = None
    return result;

def getNPIByNpiId(conn, npi):
    result = []
    try:
        with conn.cursor() as cursor:
            sql = '''
                    SELECT * 
                    FROM jms_npi.PROV_NO_NET
                    where NPI = %s
                    and taxid = %s
                    ;
            '''
            cursor.execute(sql, (npi));
            result = cursor.fetchall()
    except :
        conn.close()
        conn = None
    return result;

def getAddressLine(conn, colName):
    result = []
    try:
        with conn.cursor() as cursor:
            sql = '''
                    SELECT @@COLNAME@@ 
                    FROM jms_npi.NPI_ADDR 
                    where Country_Code = 'US'
                    limit 10000000
                    ;
            '''
            sql = sql.replace('@@COLNAME@@', colName);
            print('sql=', sql);
            cursor.execute(sql);
            result = cursor.fetchall();
    except :
        conn.close()
        conn = None
    return result;

def getNpiWords(conn, colName):
    result = []
    try:
        with conn.cursor() as cursor:
            sql = '''
                    SELECT @@COLNAME@@ 
                    FROM jms_npi.NPI_S 
                    limit 10000000
                    ;
            '''
            sql = sql.replace('@@COLNAME@@', colName);
            print('sql=', sql);
            cursor.execute(sql);
            result = cursor.fetchall();
    except :
        conn.close()
        conn = None
    return result;



if __name__ == '__main__':
    
    pass