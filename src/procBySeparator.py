'''
Created on Mar 29, 2017

@author: lancer
'''

import csv;
import re;
from fuzzywuzzy import process

'''
   19701    19701   261124 Address_City_NameDict.csv
  139445   139445  1724273 Address_First_LineDict.csv
   75911    75911   910399 Address_Second_LineDict.csv
  158380   158380  1907517 Provider_First_Name.csv
  514291   514291  6877143 Provider_Last_Name.csv
  231551   231551  2964421 Provider_Organization_NameDict.csv

'''

allFile, allLine = '../origData/Address_First_LineDict.csv', 139445;
freqDict = {}

_englishDict = set([]);

def isWords(s):
    return re.match(r'^[A-Z\']+$', s.upper())

def readEnglishDict():
    with open('../origData/american-english', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            _englishDict.add(row[0].upper());
    return _englishDict;

def readData():
    _freqDict = {}
    with open(allFile, 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            _freqDict[row[0]] = int(row[1])
    return _freqDict;

if __name__ == '__main__':
    readEnglishDict();
    print ('english dictionary length:', len(_englishDict))

    freqDict = readData();
    
    separators = ',/'
    trans = str.maketrans(separators, ' ' * len(separators));
    i = 0;    
    j = 0;
    allWords = sorted(freqDict.keys());
    for k in allWords:
        stripped = k.translate(trans);
        newWords = stripped.split(' ')
        if len(newWords) > 1 :
            #print ()
            #print (i, k, ' split to ', newWords)

            newWordLen = []
            newWordFreq = []
            for w in newWords:
                if len(w) == 0 : continue;
                newWordLen.append(len(w));

                if w.isdigit() :
                    newWordFreq.append(999)
                elif w in freqDict : 
                    newWordFreq.append(freqDict[w])
                    #freqDict[w] += 1;
                    #print ('--------', w, freqDict[w])
                else :
                    newWordFreq.append(-1)
                    #freqDict[w] = 1;
                    pass
            if min(newWordFreq) <= 10:
                print ()
                print (i, k, ' split to ', newWords)
                print (newWords, newWordFreq)
                for w in newWords :
                    if isWords(w) and w not in freqDict and w not in _englishDict:
                        nearWords = process.extractBests(w, _englishDict)
                        print (w, 'near words is ', nearWords)
                j += 1;
            #if min(newWordLen) <= 2:
            #    print ('********')
            i += 1;
    
    print ('total:', i, j)
    pass