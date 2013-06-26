# -*- coding: utf8 -*-
from flask import Flask,request,jsonify
import json

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 

from local.weibo import WeiboAutoAuth

app = Flask(__name__)

app.debug = True
@app.route('/weibo',methods=['POST'])
def weibo_auth():
	keys = {'app_key','app_secret','redirect_uri','username','password'}
	for key in keys:
		if(request.form.has_key(key) == False):
			return jsonify(
					error=True,
					msg='mission param:'+key
			)

	app_key = request.form['app_key']
	app_secret = request.form['app_secret']
	redirect_uri = request.form['redirect_uri']
	username = request.form['username']
	password = request.form['password']

	app = WeiboAutoAuth(app_key,app_secret,redirect_uri,username,password)
	d = json.loads(app.get_access_token())
	d['error'] = False
	return jsonify(d)

if __name__ == '__main__':
    app.run()