# -*- coding: utf8 -*-

from weibo import APIClient
import urllib2
import urllib

if __name__ == "__main__":
	APP_KEY = '3471849585'
	APP_SECRET = '7b0dd7f9bae77257734586afcfbafd38'
	CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
	AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
	TOKEN_URL = 'https://api.weibo.com/oauth2/access_token'
	USERID = '你的微博邮箱'
	PASSWD = '你的微博密码'
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	referer_url = client.get_authorize_url()
	print "referer url is : %s" % referer_url

	# cookies = urllib2.HTTPCookieProcessor()
	# opener = urllib2.build_opener(cookies)
	# urllib2.install_opener(opener)

	postdata = {"client_id": APP_KEY,
			"redirect_uri": CALLBACK_URL,
			"userId": USERID,
			"passwd": PASSWD,
			"isLoginSina": "0",
			"action": "submit",
			"response_type": "code",
			}
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
			"Host": "api.weibo.com",
			"Referer": referer_url
			}
	req = urllib2.Request(
			url = AUTH_URL,
			data = urllib.urlencode(postdata),
			headers = headers
			)
	try:
		resp = urllib2.urlopen(req)
		code = resp.geturl()[-32:]
		print "callback url is : %s" % resp.geturl()
		print "code is : %s" % code
	except Exception, e:
		print "Error:",e

	print client.request_access_token(code=code),
