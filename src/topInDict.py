'''
Created on Mar 29, 2017

@author: lancer
'''

import extractSample as es
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
    print (len(citynames))
    print (len(peopleFirstName))
    print (len(peopleLastName))
    
    allData = es.extractFreqBetween(es.readAll('../origData/Provider_Last_Name.csv'), 100)
    #top100 = es.extractTopFreq(allData, 100000);
    top100 = allData;
    
    i = 0;
    cityNameCount = 0;
    firstNameCount = 0;
    lastNameCount = 0;
    englishDictCount = 0;
    unknownCount = 0
    for word, freq in top100:
        if not dictMatch.hasWord(word) :
            if word in citynames :
                #print (i, word, 'is a city name')
                cityNameCount += 1;
            elif word in peopleFirstName :
                #print (i, word, 'is a First name')
                firstNameCount += 1;
            elif word in peopleLastName :
                #print (i, word, 'is a Last name')
                lastNameCount += 1;
            else :
                unknownCount += 1;
                print (i, word, freq)
                #b = dictMatch.extractBests(word)
                #print (i, word, freq, b)
        else :
            englishDictCount += 1;
        i += 1;
    
    print ('total', len(top100))
    print ('cityNameCount =', cityNameCount);
    print ('peopleFirstName =', firstNameCount);
    print ('peopleLastName =', lastNameCount);
    print ('englishDictCount =', englishDictCount);
    print ('unknownCount =', unknownCount);
    pass