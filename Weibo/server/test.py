# coding=utf8
import urllib
import urllib2
import json

auth_url = "http://localhost:5000/weibo"

def auth(username,password,app_key,app_secret,redirect_uri):
	params = urllib.urlencode({'username':username,'password':password,'app_key':app_key,'app_secret':app_secret,'redirect_uri':redirect_uri})
	req = urllib2.Request(url=auth_url,data=params);
	f = urllib2.urlopen(req)
	json_str = f.read()
	print json_str
		
if __name__ == '__main__':
	app_key = '3530915833' #请修改成您的app_key
	app_secret = 'f34a9eb3404c7f99b5e8466e18ce9b6e' #请修改成您的app_secret
	redirect_uri = 'http://snsapi.sinaapp.com/auth.php' #请修改成您的redirect_uri
	username = '' #请修改成您的测试用户名
	password = '' #请修改成您的测试微博密码
	auth(username,password,app_key,app_secret,redirect_uri)