#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 26, 2017

@author: lancer
'''
import random;
import csv;
import re;
import extractSample as es

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import preprocessing


'''
   19701    19701   261124 Address_City_NameDict.csv
  139445   139445  1724273 Address_First_LineDict.csv
   75911    75911   910399 Address_Second_LineDict.csv
  158380   158380  1907517 Provider_First_Name.csv
  514291   514291  6877143 Provider_Last_Name.csv
  231551   231551  2964421 Provider_Organization_NameDict.csv

'''

allFile = '../origData/Address_First_LineDict.csv';
totalForTrain = 2000;
totalForTest = 100;


sampleData = []
trainData = []
testData = []
sampleWords = []
testWords = []

def countAlpha(w):
    return countTotalAndMax(re.split(r'[^a-zA-Z.]', w));
    
def countNumber(w):
    return countTotalAndMax(re.split(r'[^0-9#.-]+', w));

def isNumber(w):
    s, t = countAlpha(w)
    return s < 1;

def isAlpha(w):
    if len(re.split(r'[^a-zA-Z.]', w)) == 1 : return True;
    if len(re.split(r'\'', w)) == 2 : return True;
    return False;

# return (total length, maximum length) of words
def countTotalAndMax(words):
    t = 0.0;
    s = 0.0;
    for ww in words :
        wwlen = len(ww);
        if wwlen > t:
            t = wwlen;
        if wwlen > 0 :
            s += wwlen;
    return s, t

# if all alpha = 1, is Number = -1, other  unknown = 0
def guessType(w):
    if isAlpha(w) : return 1;
    if isNumber(w): return -1;
    return 0;

# 1st, 2nd, 3rd, 4-9th, 0-9fl
def isSpecWord(w):
    if re.match(r'^[0-9]*1ST$', w): return True;
    if re.match(r'^[0-9]*2ND$', w): return True;
    if re.match(r'^[0-9]*3RD$', w): return True;
    if re.match(r'^[0-9]*[4-9]TH$', w): return True;
    if re.match(r'^[0-9]+FL$', w): return True;
    return False;

def prepareData(wordsfreq):
    sampleData = []
    infos = []
    i = 0;
    for row in wordsfreq:
        word = row[0];
        freq = row[1];
        #if isSpecWord(word) : continue;
        #if guessType(word) != 0 : continue;
        #if not re.match(r'[,-]{1}', word) : continue;
        infos.append(row);
        wordLen = len(word);
        alen, amax = countAlpha(word);
        nlen, nmax = countNumber(word);
        sample = [alen/wordLen, amax/wordLen, nlen/wordLen, nmax/wordLen];
        sampleData.append(sample);
        sampleWords.append([word, freq])
        i += 1;
    return sampleData, infos;


if __name__ == '__main__':

    freqData = es.extractFreqBetween(es.readAll('../origData/geoname.csv'), 300);
    print('total extracted', len(freqData))
    samples, sampleInfo = prepareData(freqData)
    print('total samples',  len(samples))
    
    if len(samples) == 0:
        print ('samples is empty, exit');
        exit(0);

    
    X = np.array(samples);
    
    name, est = 'k_means_iris_3', KMeans(n_clusters=3);
    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    plt.cla()
    est.fit(X)
    labels = est.labels_
    r = est.predict(X);
    
    i = 0;
    stat = {}
    for item in sampleInfo :
        #print (item, r[i])
        if r[i] in stat:
            stat[r[i]].append(item);
        else :
            stat[r[i]] = [];
            stat[r[i]].append(item);
        i += 1;
    for k in stat.keys():
        s = len(stat[k])
        print (k, 'size:', s)
        #if s < len(sampleInfo) /2 :
        print (k, stat[k]);

    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width')
    ax.set_ylabel('Sepal length')
    ax.set_zlabel('Petal length')

    plt.show()
    pass