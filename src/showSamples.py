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

allFile, allLine = '../origData/Address_First_LineDict.csv', 139445;
sampleForTrain, totalForTrain = 'trainSample.csv', 2000;
sampleForTest, totalForTest = 'testSample.csv', 100;


sampleData = []
trainData = []
testData = []
sampleWords = []
testWords = []

def countAlpha(w):
    return countTotalAndMax(re.split(r'[^a-zA-Z-]', w));
    
def countNumber(w):
    return countTotalAndMax(re.split(r'[^0-9#.-]+', w));


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

def prepareData(wordsfreq):
    sampleData = []
    i = 0;
    for row in wordsfreq:
        word = row[0];
        freq = row[1];
        wordLen = len(word);
        alen, amax = countAlpha(word);
        nlen, nmax = countNumber(word);
        sample = [alen/wordLen, amax/wordLen, nlen/wordLen, nmax/wordLen];
        sampleData.append(sample);
        sampleWords.append([word, freq])
        i += 1;
    return sampleData;


if __name__ == '__main__':

    citynames = es.extractFreqBetween(es.readAll('../origData/Provider_Organization_NameDict.csv'), 200);
    print(len(citynames))
    samples = prepareData(citynames)
    print(len(samples))

    
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
    for item in citynames :
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
        if s < len(citynames) /2 :
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