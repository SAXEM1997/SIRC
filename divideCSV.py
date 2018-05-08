# coding:utf-8  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv

filename = 'E:/SIRC/weibo.CSV'
with open(filename) as f:
    csv_reader = csv.reader(f)
    ewww = list(csv_reader)
    articles = [x[2] for x in list(csv_reader)]
    resources = [y[4] for y in ewww]
    for index in range(len(articles)):
        file1 = open('E:/SIRC/database/articles/article' + str(index) + '.txt', 'w')
        file1.write(articles[index])
        file1.close()
    for index in range(len(resources)):
        file2 = open('E:/SIRC/database/resources/resource' + str(index) + '.txt', 'w')
        file2.write(resources[index])
        file2.close()
    f.close()
