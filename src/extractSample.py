#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 26, 2017

@author: lancer
'''
import random;
import csv;
import re;

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


if __name__ == '__main__':
    allIds = list(range(0, allLine - 1));
    allSampleIds = set(random.sample(allIds, totalForTrain + totalForTest))
    
    
    with open(allFile, 'r', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        i = 0;
        for row in spamreader:
            if i in allSampleIds :
                word = row[0];
                freq = row[1];
                wordLen = len(word);
                alen, amax = countAlpha(word);
                nlen, nmax = countNumber(word);
                sample = [wordLen, alen/wordLen, amax/wordLen, nlen/wordLen, nmax/wordLen];
                sampleData.append(sample);
                sampleWords.append([word, freq])
            i += 1;
    
    #sampleData = preprocessing.scale(sampleData);
    min_max_scaler = preprocessing.MinMaxScaler()
    sampleData = min_max_scaler.fit_transform(sampleData)

    
    trainIds = set(random.sample(list(range(0, len(sampleData) - 1)), totalForTrain))
    i = 0;
    for aSample in sampleData:
        if i in trainIds :
            #print(i, 'train data', word, sample, freq)
            trainData.append(aSample)
        else :
            #print(i, '\t\t\ttest data', word, sample, freq)
            testData.append(aSample)
            testWords.append(sampleWords[i]);
        i += 1;
    #print (trainData)
    #print (testData)
    
    #centers = [[1, 1], [-1, -1], [1, -1]]
    
    X = np.array(trainData);
    
    name, est = 'k_means_iris_3', KMeans(n_clusters=3);
    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    plt.cla()
    est.fit(X)
    labels = est.labels_
    r = est.predict(testData);
    
    i = 0;
    for item in testWords :
        print (item, testData[i], r[i])
        i += 1;

    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width')
    ax.set_ylabel('Sepal length')
    ax.set_zlabel('Petal length')

    plt.show()
    pass