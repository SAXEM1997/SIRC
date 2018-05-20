# coding:utf-8  
import jieba
import os  
import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
#import csv
#import pandas
#import numpy

sentence1 = sys.argv[1]
sentence2 = sys.argv[2]
#sentence1 = '他很喜欢玩游戏，也喜欢看小说'
#sentence2 = '他喜欢玩游戏，最喜欢看小说'

Divlist1 = jieba.lcut(sentence1, cut_all=True)
Divlist2 = jieba.lcut(sentence2, cut_all=True)

Sen = [" ".join(Divlist1), " ".join(Divlist2)]

vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值 

TFIDF_value=vectorizer.fit_transform(Sen)
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
matrix_value = TFIDF_value.toarray()
vex1 = list(matrix_value[0])
vex2 = list(matrix_value[1])

def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(a,b):
        part_up += a1*b1
        a_sq += a1**2
        b_sq += b1**2
    part_down = math.sqrt(a_sq*b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down

Similarity_Cos = cos_dist(vex1, vex2)       #余弦

sumdot = 0.0
for iii in range(len(vex1)):
    sumdot += vex1[iii] * vex2[iii]
Similarity_dot = sumdot #内积

sum12 = 0.0
sum1 = 0.0
sum2 = 0.0
for index in range(len(vex1)):
    sum12 += vex1[index] *vex2[index]
    sum1 += vex1[index] ** 2
    sum2 += vex2[index] ** 2

Similarity_Jaccard = sum12/(sum1 + sum2 - sum12)    #jaccard相似度

res=open("SIMresult.txt", 'w')
res.write('余弦: '+str(Similarity_Cos)+'\n内积: '+str(sumdot)+'\nJaccard系数: '+str(Similarity_Jaccard))
res.close()
print('余弦: '+str(Similarity_Cos)+' 内积: '+str(sumdot)+' Jaccard系数: '+str(Similarity_Jaccard))
#print(' ')
#print(Similarity_dot)
#print(' ')
#print(Similarity_Jaccard)

    

 