'''
Created on Mar 20, 2017

@author: lancer
'''

import re;

import npidb;


worddict = {};

def reformat(aword):
    if re.match('P.O.', aword) :
        return 'PO';
    
    if re.match('N.E.', aword) :
        return 'NE';
    if re.match('N.W.', aword) :
        return 'NW';
    if re.match('S.E.', aword) :
            return 'SE';
    if re.match('S.W.', aword) :
        return 'SW';
    
    m = re.match(r'^([A-Z]+)([0-9]+)([A-Z]{0,1})$', aword);
    if m : 
        return m.group(1);
    w = aword.strip('_.,:;()[]{}%@!\'"');
    
    return w;

def isDigit(aword):
    if re.match(r'^[0-9]+$', aword) :
        return True;
    if re.match(r'^\d*1ST$', aword) :
        return True;
    if re.match(r'^\d*2ND$', aword) :
        return True;
    if re.match(r'^\d*3RD$', aword) :
        return True;
    if re.match(r'^\d+TH$', aword) :
        return True;
    if re.match(r'^\d+[A-Z]{1}$', aword) :
        return True;
    if re.match(r'^\d+[A-Z]{1}\d*$', aword) :
        return True;
    else :
        return False;
    
def isSymbol(aword):
    if re.match(r'^\W+$', aword) :
        return True;

    else :
        return False;
    

def countword(aword):
    if len(aword) == 0 :
        return;
    if isDigit(aword) :
        return;
    if isSymbol(aword) :
        return;
    if aword in worddict:
        worddict[aword] += 1;
    else :
        worddict[aword] = 1;
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReformat']
    #result = npidb.getAddressLine(npidb.getConnection(), "City_Name");
    result = npidb.getNpiWords(npidb.getConnection(), "Provider_First_Name, Provider_Other_First_Name");
    print (len(result));
    total = len(result)
    for i in range(0, total - 1):
        #print(i, result[i]);
        line1 = result[i][0].strip();
        line2 = result[i][1].strip();
        if len(line2) > 0 :
            line1 = line1 + ' ' + line2;
        #print (line1);
        #spchars = '-/#:.,;&1234567890';
        #t = line1.maketrans(spchars, ' ' * len(spchars));
        #words = line1.translate(t).split();
        words = line1.split();
        #print (words);
        for w in words :
            w = reformat(w);
            countword(w);
    
    fdt = open('Provider_First_Name.csv', 'w');
    
    for k in sorted(worddict.keys()) :
        freq = worddict[k];
        print (k, freq);
        fdt.write('"' + k + '",' + str(freq) + '\n');
    fdt.close();
    
    print(len(worddict))
    
    
        
        