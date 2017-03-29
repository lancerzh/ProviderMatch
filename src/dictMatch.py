'''
Created on Mar 29, 2017

@author: lancer
'''
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import csv;

dictByWordLength = {}
#aDict = {}
def readEnglishDict():
    with open('../origData/american-english', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            word = row[0].upper();
            wl = len(word)

            if wl not in dictByWordLength:
                dictByWordLength[wl] = set();
            aDict = dictByWordLength[wl]
            aDict.add(word);
    return ;

def hasWord(w):
    if len(w) not in dictByWordLength :
        return False;
    return w in dictByWordLength[len(w)]

def extractBests(w):
    aDict = dictByWordLength[len(w)]
    nearWords = process.extractBests(w, aDict, scorer=fuzz.WRatio)
    return nearWords


if __name__ == '__main__':
    readEnglishDict()
    for k in dictByWordLength.keys():
        print (k, len(dictByWordLength[k]))

    pass