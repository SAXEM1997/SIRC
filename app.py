#-*- coding=utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for,jsonify,send_from_directory,abort
from werkzeug.utils import secure_filename
import os
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/TFIDF', methods=['GET', 'POST'])
def upload_file():
	if request.method=='GET':  
		return render_template('TFIDF.html')
	else: 
		f = request.files['data']
		tempdir = 'uploads/' + secure_filename(f.filename)
		f.save(tempdir)
		os.system("E:")
		os.system("cd E:\\SIRC\\")
		#os.system("activate python2.7")
		os.system("python Get_TFIDF.py " + tempdir)
		return render_template('TFIDF.html')+'<br/>提交成功!'

@app.route('/TFIDF_Result', methods=['GET'])
def download_file():
	if request.method=='GET':
		dfilename="allresults.zip"
		if os.path.isfile(dfilename):
			return send_from_directory('',dfilename,as_attachment=True)
		abort(404)

@app.route('/SIM', methods=['GET', 'POST'])
def input_sentence():
	if request.method=='GET':
		return render_template('SIM.html')
	else:
		s1 = request.form.get("sentence1").encode('gbk')
		s2 = request.form.get("sentence2").encode('gbk')
		os.system("E:")
		os.system("cd E:\\SIRC\\")
		#os.system("activate python2.7")
		#os.system('python Similarity_Compare.py ' + s1 + ' ' + s2)
		simcmd = os.popen('python Similarity_Compare.py ' + s1 + ' ' + s2)
		simres = simcmd.read()
		return render_template('SIM.html')+'<h2>计算结果</h2><p>'+simres+'</p>'

@app.route('/SJet', methods=['GET', 'POST'])
def mySJet():
	if request.method=='GET':
		return render_template('SJet.html')
	else:
		myinput = request.form.get("userinput").encode('gbk')
		os.system("E:")
		os.system("cd E:\\SIRC\\")
		#os.system("activate python2.7")
		#os.system('python Similarity_Compare.py ' + s1 + ' ' + s2)
		simcmd1 = os.popen("python SJet.py '" + myinput + "'")
		simres1 = simcmd1.read()
		return render_template('SJet.html')+'<h2>搜索结果</h2><br/><br/>'+simres1

@app.route('/SJetRes/<int:post_id>', methods=['GET'])
def show_res(post_id):
	if request.method=='GET':
		dfilename1="database/articles/article"+str(post_id)+".txt"
		if os.path.isfile(dfilename1):
			return send_from_directory('',dfilename1,as_attachment=True)
		abort(404)

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port='6789')