# coding:utf-8  
import jieba
import os  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
import csv
import pandas

filename = 'E:/SIRC/weibo.CSV'
with open(filename) as f:
    csv_reader = csv.reader(f)
    articles = [x[4] for x in list(csv_reader)]
    listcorpus = [jieba.lcut(article, cut_all=True) for article in articles]
    sentence_n=[" ".join(corpu) for corpu in listcorpus]
    
    sentence_all= [" ".join(sentence_n)]
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值 
    
    TFIDF_all_value=vectorizer.fit_transform(sentence_all)
    TFIDF_all_weight=transformer.fit_transform(TFIDF_all_value)#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
    
    matrix_all_value = TFIDF_all_value.toarray()
    matrix_all_weight = TFIDF_all_weight.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重   
    
    data_all = [[word[i], matrix_all_value[0][i], matrix_all_weight[0][i]] for i in range(len(word))]
    name_all = ['单词', 'TF-IDF权值', 'TF-IDF权重']
    result_all = pandas.DataFrame(columns=name_all, data=data_all)
    result_all.to_csv('E:/SIRC/result.CSV')
    f.close()
