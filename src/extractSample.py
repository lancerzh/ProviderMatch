#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 26, 2017

@author: lancer
'''
import random;
import csv;
import re;


'''
   19701    19701   261124 Address_City_NameDict.csv
  139445   139445  1724273 Address_First_LineDict.csv
   75911    75911   910399 Address_Second_LineDict.csv
  158380   158380  1907517 Provider_First_Name.csv
  514291   514291  6877143 Provider_Last_Name.csv
  231551   231551  2964421 Provider_Organization_NameDict.csv

'''

allFile, allLine = '../origData/Address_First_LineDict.csv', 139445;
samplesFileName, totalOfSamples = 'samples.csv', 1000;

def extractSamples(allData, total):  
    allIds = list(range(0, len(allData) - 1));
    allSampleIds = set(random.sample(allIds, total))
    samples = []

    i = 0;
    for row in allData:
        if i in allSampleIds :
            samples.append(row);
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
    writeFile(samplesFileName, extractSamples(totalOfSamples));
    writeFile('top1000.csv', extractTopFreq(1000));
    
    
