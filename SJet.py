# coding:utf-8  
import jieba 
import sys
import os, os.path
import math
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
import csv
import pandas

filename = 'E:/SIRC/weibo.CSV'
#entence1 = '我是周杰伦';
sentence1 = sys.argv[1];

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

with open(filename) as f:
    csv_reader = csv.reader(f)
    articles = [x[2] for x in list(csv_reader)]
    relative = []
    for i in range(len(articles)):
        Divlist1 = jieba.lcut(sentence1, cut_all=True)
        Divlist2 = jieba.lcut(articles[i], cut_all=True)
        
        Sen = [" ".join(Divlist1), " ".join(Divlist2)]
        
        vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵
        transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值 
        
        TFIDF_value=vectorizer.fit_transform(Sen)
        word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
        matrix_value = TFIDF_value.toarray()
        vex1 = list(matrix_value[0])
        vex2 = list(matrix_value[1])
        
        Similarity_Cos = cos_dist(vex1, vex2)       #余弦
        sum12 = 0.0
        sum1 = 0.0
        sum2 = 0.0
        for index in range(len(vex1)):
            sum12 += vex1[index] *vex2[index]
            sum1 += vex1[index] ** 2
            sum2 += vex2[index] ** 2
        
        Similarity_Jaccard = sum12/(sum1 + sum2 - sum12)    #jaccard相似度
        myweight = Similarity_Cos*0.5 + Similarity_Jaccard*0.5
        relative.append(myweight)
    sortres=sorted(enumerate(relative), key=lambda x:x[1])
    myres=[]
    for j in range(10):
        myres.append(sortres[len(sortres)-j-1][0])
    myres2=''
    for jj in range(len(myres)):
        myres2=myres2 + '<p><a href="/SJetRes/'+str(myres[jj])+ '">' + articles[myres[jj]] + '</a></p><br/>'
    myres3=(myres2.decode('utf8')).encode('gbk')
    print(myres2)
f.close()
    
        