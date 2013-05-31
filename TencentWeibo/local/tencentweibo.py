# -*- coding: utf8 -*-
import urllib
import urllib2,httplib
import cookielib
from bs4 import BeautifulSoup

class TencentWeiboAutoAuth(object):
	'''
	腾讯微博自动认证客户端
	曲线救国，从wap端下手更容易
	'''
	def __init__(self, app_key,	app_secret, redirect_uri, username,	password, response_type='code'):
		self.app_key = app_key
		self.app_secret = app_secret
		self.redirect_uri = redirect_uri
		self.response_type = response_type
		self.username = username
		self.password = password
		self.__get_code()

	def __get_authorize_url(self):
		base_url = 'https://open.t.qq.com/cgi-bin/oauth2/authorize?client_id=%s&response_type=code&redirect_uri=%s&wap=2'
		return base_url % (self.app_key,urllib2.quote(self.redirect_uri))

	def __get_code(self):
		opener = urllib2.build_opener(
				urllib2.HTTPRedirectHandler(),
				urllib2.HTTPHandler(),
				urllib2.HTTPSHandler(),
				urllib2.HTTPCookieProcessor(cookielib.CookieJar())
		)
		# step1: 打开登陆框，记录cookies
		open_login_form = opener.open(self.__get_authorize_url())
		login_form_url = open_login_form.geturl()
		login_form_html = open_login_form.read()

		# step2: 获取表单
		login_form_data = {}
		soup = BeautifulSoup(login_form_html)
		inputs = soup.find_all('input')
		for input in inputs:
			login_form_data[input.get('name')] = input.get('value')

		del login_form_data[None]
		print login_form_data

		login_form_data['u'] = self.username
		login_form_data['p'] = self.password

		# step3：提交数据
		request_url = 'https://open.t.qq.com/cgi-bin/oauth2/authorize'
		response = opener.open(request_url,urllib.urlencode(login_form_data))
		htmlcontent = response.read()
		code_start = htmlcontent.index('code=')
		openid_start = htmlcontent.index('openid=')
		openkey_start = htmlcontent.index('openkey=')
		
		self.code = htmlcontent[code_start+5:code_start+5+32]
		self.openid = htmlcontent[openid_start+7:openid_start+7+32]
		self.openkey = htmlcontent[openkey_start+8:openkey_start+8+32]
	
	def get_code(self):
		return self.code

	def get_access_token(self):
		request_url = 'https://open.t.qq.com/cgi-bin/oauth2/access_token?client_id=%s&client_secret=%s&redirect_uri=%s&grant_type=authorization_code&code=%s'
		request_url = request_url % (self.app_key,self.app_secret,urllib.quote(self.redirect_uri),self.code)
		response = urllib2.urlopen(request_url)
		print response.read()

	def get_openid(self):
		return self.openid

	def get_openkey(self):
		return self.openkey


