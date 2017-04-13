'''
Created on Apr 12, 2017

@author: lancer
'''
import csv;

if __name__ == '__main__':
    fdt1 = open('../samplesTrain1.txt', 'w', encoding='utf-8');
    fdt2 = open('../samplesTrain2.txt', 'w', encoding='utf-8');
    fdt3 = open('../samplesTrain3.txt', 'w', encoding='utf-8');
    fdt4 = open('../samplesTrain4.txt', 'w', encoding='utf-8');

    with open('../npisamples1.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            t = row[1].strip();
            w = row[0].strip();
            #print (t, w)
            if t == '1':
                fdt1.write(w + '\n');
                print ('1:', w)
            if t == '2':
                fdt2.write(w + '\n');
                print ('2:', w)
            if t == '3':
                fdt3.write(w + '\n');
                print ('3:', w)
            if t == '4':
                fdt4.write(w + '\n');
                print ('4:', w)
    with open('../npisamples2.csv', 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            t = row[1].strip();
            w = row[0].strip();
            #print (t, w)
            if t == '1':
                fdt1.write(w + '\n');
                print ('1:', w)
            if t == '2':
                fdt2.write(w + '\n');
                print ('2:', w)
            if t == '3':
                fdt3.write(w + '\n');
                print ('3:', w)
            if t == '4':
                fdt4.write(w + '\n');
                print ('4:', w)
                
    fdt1.close();
    fdt2.close();
    fdt3.close();
    fdt4.close();
    pass