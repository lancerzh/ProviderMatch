'''
Created on Mar 29, 2017

@author: lancer
'''

import re
import extractSample as es
import readNamesFromDB as namedb
import dictMatch;

def data2Map (data):
    result = set();
    for d in data:
        result.add(d[0]);
    return result;

if __name__ == '__main__':
    dictMatch.readEnglishDict();

    citynames = data2Map(es.extractFreqBetween(es.readAll('../origData/Address_City_NameDict.csv'), 200))
    peopleFirstName = data2Map(es.extractFreqBetween(es.readAll('../origData/Provider_First_Name.csv'), 200))
    peopleLastName = data2Map(es.extractFreqBetween(es.readAll('../origData/Provider_Last_Name.csv'), 200))
    allNames = data2Map(namedb.readNames())
    geoName = data2Map(es.extractFreqBetween(es.readAll('../origData/geoname.csv'), 10))
    print ('citynames', len(citynames))
    print ('peopleFirstName', len(peopleFirstName))
    print ('peopleLastName', len(peopleLastName))
    print ('allNames', len(allNames))
    print ('geoName', len(geoName))
    
    allData = es.extractFreqBetween(es.readAll('../origData/Address_Second_LineDict.csv'), 100)
    #top100 = es.extractTopFreq(allData, 100000);
    top100 = allData;
    
    i = 0;
    cityNameCount = 0;
    firstNameCount = 0;
    lastNameCount = 0;
    allNamesCount = 0;
    geoNameCount = 0;
    englishDictCount = 0;
    unknownCount = 0
    unknownWords = []
    for word, freq in top100:
        if not re.match(r'[A-Z]+', word): continue;
        if dictMatch.hasWord(word) :
            englishDictCount += 1;
        elif word in citynames :
            #print (i, word, 'is a city name')
            cityNameCount += 1;
        elif word in peopleFirstName :
            #print (i, word, 'is a First name')
            firstNameCount += 1;
        elif word in peopleLastName :
            #print (i, word, 'is a Last name')
            lastNameCount += 1;
        elif word in allNames :
            #print (i, word, 'is a Last name')
            allNamesCount += 1;
        elif word in geoName :
            #print (i, word, 'is a Last name')
            geoNameCount += 1;
        else :
            unknownCount += 1;
            #print (i, word, freq)
            unknownWords.append([word, freq])
            #b = dictMatch.extractBests(word)
            #print (i, word, freq, b)
        i += 1;
    sorted_x = sorted(unknownWords, key=lambda x:x[1]);
    sorted_x.reverse();
    
    for i, r in enumerate(sorted_x):
        print (i, r[0], r[1])

    print ('total', len(top100))
    print ('cityNameCount =', cityNameCount);
    print ('peopleFirstName =', firstNameCount);
    print ('peopleLastName =', lastNameCount);
    print ('allName =', allNamesCount);
    print ('geoNameCount =', geoNameCount);
    print ('englishDictCount =', englishDictCount);
    print ('unknownCount =', unknownCount);
    pass