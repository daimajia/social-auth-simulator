# -*- coding: utf8 -*-
import urllib
import urllib2

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
		postdata = {"client_id": self.app_key,
			"redirect_uri": self.redirect_uri,
			"userId": self.username,
			"passwd": self.password,
			"isLoginSina": "0",
			"action": "submit",
			"response_type": "code"
		}
		auth_url = 'https://api.weibo.com/oauth2/authorize'
		referer_url = self.__get_authorize_url()
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
			"Host": "api.weibo.com",
			"Referer": referer_url
		}
		request = urllib2.Request(
			url = auth_url,
			data = urllib.urlencode(postdata),
			headers = headers
		)
		try:
			response = urllib2.urlopen(request)
			code = response.geturl()[-32:]
			return code
		except Exception as e:
			print "Error:",e

	def get_access_token(self):
		postdata = {
			'redirect_uri':self.redirect_uri,
			'client_id':self.app_key,
			'grant_type':'authorization_code',
			'code':self.get_code(),
			'client_secret':self.app_secret
		}
		request_url = 'https://api.weibo.com/oauth2/access_token'
		request = urllib2.Request(
			url = request_url,
			data = urllib.urlencode(postdata)
		)
		return urllib2.urlopen(request).read()
