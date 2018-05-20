# coding:utf-8  
import jieba 
import sys
import os, os.path
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
import csv
import pandas
import zipfile

#filename = 'E:/SIRC/weibo.CSV'
filename = sys.argv[1];
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
          
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
with open(filename) as f:
    csv_reader = csv.reader(f)
    articles = [x[2] for x in list(csv_reader)]
    listcorpus = [jieba.lcut(article, cut_all=True) for article in articles]
    sentence_n=[" ".join(corpu) for corpu in listcorpus]
    
    sentence_all= [" ".join(sentence_n)]
    for index in range(len(sentence_n)):
        vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵
        transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值 
        
        #TFIDF_all_value=vectorizer.fit_transform(sentence_all)#计算tf-idf 
        #TFIDF_all_weight=transformer.fit_transform(TFIDF_all_value)#计算tf-idf词频 
        TFIDF_value=vectorizer.fit_transform([sentence_n[index]])#计算tf-idf 
        TFIDF_weight=transformer.fit_transform(TFIDF_value)#计算tf-idf词频 
        word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
        
        #matrix_all_value = TFIDF_all_value.toarray()#抽取为数组
        #matrix_all_weight = TFIDF_all_weight.toarray()#抽取为数组
        matrix_value = TFIDF_value.toarray()#抽取为数组
        matrix_weight = TFIDF_weight.toarray()#抽取为数组
        
        data_n = [[word[i], matrix_value[0][i], matrix_weight[0][i]] for i in range(len(word))]
        name_n = ['单词', 'TF-IDF权值', 'TF-IDF权重']
        result = pandas.DataFrame(columns=name_n, data=data_n)
        result.to_csv('E:/SIRC/results/result' + str(index) + '.CSV')
    zip_dir('E:/SIRC/results', 'allresults.zip')
    f.close()
    