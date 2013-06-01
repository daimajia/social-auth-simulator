# -*- coding: utf8 -*-
import urllib
import urllib2,httplib
import cookielib
from bs4 import BeautifulSoup

class RenrenAutoAuth(object):
	'''
	人人自动认证授权
	'''
	def __init__(self,app_id, app_key, app_secret, redirect_uri, username, password, response_type='code'):
		self.app_key = app_key
		self.app_id = app_id
		self.app_secret = app_secret
		self.redirect_uri = redirect_uri
		self.response_type = response_type
		self.username = username
		self.password = password

	def get_authorize_url(self):
		base_url = 'https://graph.renren.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code'
		return base_url % (self.app_key,urllib2.quote(self.redirect_uri))

	def get_code(self):
		httplib.HTTPConnection.debuglevel = 0
		opener = urllib2.build_opener(
				urllib2.HTTPRedirectHandler(),
				urllib2.HTTPHandler(),
				urllib2.HTTPSHandler(),
				urllib2.HTTPCookieProcessor(cookielib.CookieJar())
			)
		# step1: 打开登陆框，并且记录cookies
		open_login_form = opener.open(self.get_authorize_url())
		login_form_url = open_login_form.geturl()
		login_form_html = open_login_form.read()

		# print (login_form_html)
		

		# step2:获取所有表单数据
		login_form_data = {}
		soup = BeautifulSoup(login_form_html)
		inputs = soup.find_all('input')
		for input in inputs:
			login_form_data[input.get('name')] = input.get('value')

		login_form_data['username'] = self.username
		login_form_data['email'] = self.username
		login_form_data['password'] = self.password
		del login_form_data['']
		# print login_form_data

		# step3:提交表单
		try:
			# print urllib.urlencode(login_form_data)
			login_request_url = 'https://graph.renren.com/login'
			login_request = urllib2.Request(login_request_url,urllib.urlencode(login_form_data))
			response = opener.open(login_request)
			# print response.geturl()
			location = response.geturl()

			#step 3.1 判断是否已经授权过，如果授权过则直接获取code
			if 'code=' in location:
				return location[-32:]

			to_make_sure_html = response.read()

		#step4：如果未授权过，则在新的表单中提交授权确认
			to_make_sure_form = 'https://graph.renren.com/oauth/grant'
			to_make_sure_data = {}

			# print to_make_sure_html

			soup = BeautifulSoup(to_make_sure_html)
			inputs = soup.find_all('input')
			for input in inputs:
				to_make_sure_data[input.get('name')] = input.get('value')
			# print to_make_sure_data
			response = opener.open(to_make_sure_form,urllib.urlencode(to_make_sure_data),100)
			return response.geturl()[-32:]
		except Exception as e:
			print e
			return 'error:',e


	def get_access_token(self):
		token_url = 'https://graph.renren.com/oauth/token?'+ urllib.urlencode({
						'grant_type':'authorization_code',
						'client_id':self.app_key,
						'client_secret':self.app_secret,
						'code':self.get_code(),
						'redirect_uri':self.redirect_uri
					})
		response = urllib2.urlopen(token_url)
		return response.read()



















