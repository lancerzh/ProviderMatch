#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 26, 2017

@author: lancer
'''
import random;
import csv;
import re;

import npidb;


'''
=1 3606609
=2 1132779

'''


    
def extractByIds(entity_type, inCause):
    sqlstmt = '''
        SELECT 
            Entity_Type_Code, 
            Provider_Organization_Name,
            Provider_Last_Name, 
            Provider_First_Name, 
            Provider_Middle_Name, 
            Provider_Other_Organization_Name, 
            Provider_Other_Last_Name, 
            Provider_Other_First_Name, 
            Provider_Other_Middle_Name,
            Provider_First_Line_Business_Mailing_Address,
            Provider_Second_Line_Business_Mailing_Address,
            Provider_Business_Mailing_Address_City_Name,
            Provider_First_Line_Business_Practice_Location_Address,
            Provider_Second_Line_Business_Practice_Location_Address,
            Provider_Business_Practice_Location_Address_City_Name
        FROM jms_npi.NPI_S
        where Entity_Type_Code = ''' + entity_type + '''
        and NPI in ''' + inCause + '''
        ;
    '''
    conn = npidb.getConnection();

    result = None;
    try:
        with conn.cursor() as cursor:
            cursor.execute(sqlstmt);
            result = cursor.fetchall()
    except :
        conn.close()
        conn = None
    return result;


totalOfSamples = 20;

def extractNpiID(entity_type):
    conn = npidb.getConnection();
    npiidsql = '''
        SELECT NPI
        FROM jms_npi.NPI_S
        where Entity_Type_Code = ''' + entity_type + '''
        ;
    '''
    result = None;
    try:
        with conn.cursor() as cursor:
            cursor.execute(npiidsql);
            result = cursor.fetchall()
    except :
        conn.close()
        conn = None
    return result;


def extractSamples(allData, total):  
    allIds = list(range(0, len(allData) - 1));
    allSampleIds = set(random.sample(allIds, total))
    samples = []

    i = 0;
    for row in allData:
        if i in allSampleIds :
            samples.append(row[0]);
        i += 1;
    return samples;

def extractTopFreq(allData, top):
    result = []
    sorted_x = sorted(allData, key=lambda x:x[1]);
    sorted_x.reverse();
    i = 0;
    for row in sorted_x:
        if i >= top : break;
        #print (row)
        result.append(row);
        i += 1;
    return result;

def extractFreqBetween(allData, minimum, maximum=1000000):
    result = []
    i = 0;
    for row in allData:
        freq = row[1]
        if freq >= minimum and freq <= maximum:
            #print (row)
            result.append(row);
            i += 1;
    return result;

def writeFile(filename, data):
    fdt = open(filename, 'w', encoding='utf-8');
    for row in data:
        fdt.write('"' + row[0] + '",' + str(row[1]) + '\n');
    fdt.close();

def readAll(filename):
    allData = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            word = row[0].strip('-,');
            freq = int(row[1]);
            allData.append([word, freq])
    print('total of data', len(allData))
    return allData;


if __name__ == '__main__':
    npitype= '2';
    totalSamples = 5000;
    
    allIds = extractNpiID(npitype)
    sampleIds = extractSamples(allIds, totalSamples);
    strIds = []
    for aId in sampleIds:
        print(aId);
        strIds.append(str(aId))
        
    inCause = '(' + ','.join(strIds) + ')';
    print (inCause);
    allSamples = extractByIds(npitype, inCause);
    
    fdt = open('../npisamples' + npitype + '.csv', 'w', encoding='utf-8');

    for aSample in allSamples :
        print (aSample);
        if len(aSample[1]) > 0:
            outputline = '"'+aSample[1]+'", ' + '1';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[2]) > 0:
            outputline = '"'+aSample[2]+'", ' + '2';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[3]) > 0:
            outputline = '"'+aSample[3]+'", ' + '2';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[5]) > 0 and aSample[5] != aSample[1] :
            outputline = '"'+aSample[5]+'", ' + '1';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[6]) > 0 and aSample[6] != aSample[2] :
            outputline = '"'+aSample[6]+'", ' + '2';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[7]) > 0 and aSample[7] != aSample[3] :
            outputline = '"'+aSample[7]+'", ' + '2';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[9]) > 0 :
            outputline = '"'+aSample[9]+'", ' + '3';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[10]) > 0 :
            outputline = '"'+aSample[10]+'", ' + '3';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[11]) > 0 :
            outputline = '"'+aSample[11]+'", ' + '4';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[12]) > 0 and aSample[12] != aSample[9] :
            outputline = '"'+aSample[12]+'", ' + '3';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[13]) > 0 and aSample[13] != aSample[10]:
            outputline = '"'+aSample[13]+'", ' + '3';
            print (outputline);
            fdt.write(outputline + '\n');
        if len(aSample[14]) > 0 and aSample[14] != aSample[11]:
            outputline = '"'+aSample[14]+'", ' + '4';
            print (outputline);
            fdt.write(outputline + '\n');
                
            #fdt.write('"' + row[0] + '",' + str(row[1]) + '\n');
    fdt.close();


    #writeFile(samplesFileName, extractSamples(totalOfSamples));
    #writeFile('top1000.csv', extractTopFreq(1000));
    
    
