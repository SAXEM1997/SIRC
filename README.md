# SIRC_work2

## Required
- python2.7
- scilearn
- jieba
- numpy(非必需)
- pandas(非必需)
- flask

## 1.TFIDF:对所给语料库进行TF-IDF统计，给出总TF-IDF权值与单位权重
代码: ./get_TFIDF.py
语料库: ./database/  (753条微博正文与来源)

## 2.SIM:对给与的两个句子计算其内积/余弦，以及Jaccard相似度
代码: ./Similary_Compare.py

## 3.SJet:基于向量空间模型实现搜索引擎
代码: ./SJet.py

## 4.全部功能均基于flask在线实现
app代码: app.py 
