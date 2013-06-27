# -*- coding: utf8 -*-
import urllib
import urllib2
import cookielib
import requests
from bs4 import BeautifulSoup

class WeiboAutoAuth(object):
	'''
	新浪微博自动认证
	'''
	def __init__(self,app_key,app_secret,redirect_uri,username,password,response_type='code'):
		self.app_key = app_key
		self.app_secret = app_secret
		self.redirect_uri = redirect_uri
		self.response_type = response_type
		self.username = username
		self.password = password

	def __get_authorize_url(self):
		base_url = 'https://api.weibo.com/oauth2/authorize?client_id=%s&response_type=code&redirect_uri=%s'
		return base_url % (self.app_key,self.redirect_uri)

	def get_code(self):

		print self.__get_authorize_url()
		# step1: 打开登陆框，并且记录cookies

		open_login_form = requests.get(self.__get_authorize_url())
		open_login_form_html = open_login_form.text
		open_login_form_url = open_login_form.url

		soup = BeautifulSoup(open_login_form_html)
		inputs = soup.find_all('input')

		#step2:获取表单数据
		login_form_data = {}
		for input in inputs:
			value = input.get('value')
			login_form_data[input.get('name')] = unicode(value).encode('utf-8')
		
		login_form_data['userId'] = self.username
		login_form_data['passwd'] = self.password

		print login_form_data

		#step3:提交表单
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
			"Host": "api.weibo.com",
			"Referer":self.__get_authorize_url(),
			"Origin":"http://api.weibo.com"
		}

		auth_url = 'https://api.weibo.com/oauth2/authorize'
		response = requests.post(auth_url,data = login_form_data,headers=headers)
		url = response.url

		#如果已经认证过，则地址中包含code=，然后直接返回
		if('code=' in url):
			return url[-32:]

		content = response.text

		soup = BeautifulSoup(content)
		auth_data = {}
		inputs = soup.find_all('input')

		for input in inputs:
			value = input.get('value')
			auth_data[input.get('name')] = unicode(value).encode('utf-8')

		# print auth_data

		sure_url = 'https://api.weibo.com/2/oauth2/authorize'
		r =  requests.post(sure_url,data = auth_data, headers = headers)
		print r.url[-32:]
		return r.url[-32:]

	def get_access_token(self):
		postdata = {
			'redirect_uri':self.redirect_uri,
			'client_id':self.app_key,
			'grant_type':'authorization_code',
			'code':self.get_code(),
			'client_secret':self.app_secret
		}
		request_url = 'https://api.weibo.com/oauth2/access_token'

		r = requests.post(request_url,data=postdata)
		return r.text
