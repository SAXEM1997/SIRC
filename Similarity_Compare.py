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
import csv
import pandas
import numpy

#sentence1 = sys.argv[1]
#sentence2 = sys.argv[2]
test1 = '周杰伦是一个歌手,也是一个叉叉'
test2 = '周杰伦不是一个叉叉，但是是一个歌手'

Divlist1 = jieba.lcut(test1, cut_all=True)
Divlist2 = jieba.lcut(test2, cut_all=True)

Sen = [" ".join(Divlist1), " ".join(Divlist2)]

vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
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

suma = 0.0
sumb = 0.0

for qa in vex1:
    suma += qa**2
for qb in vex2:
    sumb += qb**2

Similarity_dot = sum(vex1 / (suma**0.5) * vex2 / (sumb**0.5)) #内积

sum12 = 0.0
sum1 = 0.0
sum2 = 0.0
for index in range(len(vex1)):
    sum12 += vex1[index] *vex2[index]
    sum1 += vex1[index] ** 2
    sum2 += vex2[index] ** 2

Similarity_Jaccard = sum12/(sum1 + sum2 - sum12)    #jaccard相似度


    

 