'''
Created on Mar 30, 2017

@author: lancer
'''

import csv;

import extractSample

maxLine = 1000000

def writeFile(filename, data):
    fdt = open(filename, 'w', encoding='utf-8');
    for row in data:
        fdt.write('"' + row[0] + '",' + str(row[1]) + '\n');
    fdt.close();
    
if __name__ == '__main__':
    allData = []
    filename = '/Users/lancer/jms/JMS_HCC_5010HCFATest_20140618/facilityaddress1.csv';
    with open(filename, 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        i = 0;
        for row in spamreader:
            i += 1;
            if i == 1 : continue;
            if i >= maxLine : break;
            al1 = row[5];
            al2 = row[6];
            al3 = row[7];
            alc = row[8];
            als = row[9];
            alz = row[10];
            aln = row[12];
            if len(al3) > 0 : continue;
            #print (i, al1, al2, alc, als, alz, aln);
            allData.append((al1, al2, alc, als, alz, aln))
    samples = extractSample.extractSamples(allData, 1000)
    for s in samples :
        print (s)
    pass