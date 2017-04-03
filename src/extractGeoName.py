'''
Created on Mar 30, 2017

@author: lancer
'''

import csv;
import dictMatch;
import extractSample;

filename = '../origData/NationalFile_20170201.txt'

maxline = 10000000;

def readfile():
    names = {}
    separators = ' -()/'
    tb = str.maketrans(separators, ' ' * len(separators))
    with open(filename, 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
        i = 0;
        for row in spamreader:
            i += 1;
            if i == 1: continue;
            if i > maxline : break;
            aName = row[1].upper().translate(tb);
            #aName = row[1].upper();
            #print (aName)
            for w in aName.split(' '):
                if len(w) == 0: continue;
                if w.isdigit(): continue;
                if w in names :
                    names[w] += 1;
                else :
                    names[w] = 1;
    return names;

if __name__ == '__main__':
    dictMatch.readEnglishDict();
    names = readfile();
    notInDict = [];
    i = 0;
    for w in names.keys():
        if not dictMatch.hasWord(w):
            print( w, names[w]);
            notInDict.append([w, names[w]]);
        i += 1;
    print ('total:', i)
    extractSample.writeFile('a.csv', notInDict);
    pass