# coding=utf8
import urllib
import urllib2
import json

auth_url = "http://end.zhan-dui.com/weibo/test.php"

##3471849585
##7b0dd7f9bae77257734586afcfbafd38
##https://api.weibo.com/oauth2/default.html

def auth(uid,password,app_key,app_secret,callback_uri):
	params = urllib.urlencode({'userid':uid,'password':password,'app_key':app_key,'app_secret':app_secret,'callback_uri':callback_uri})
	req = urllib2.Request(url=auth_url,data=params);
	f = urllib2.urlopen(req)
	json_str = f.read()
	print json_str
	
	#以下是错误处理，现在还不够详细，没有多错误归类和列错误Number
	decoded = json.loads(json_str)
	if "error_msg" in decoded.keys():
		print "错误消息(error_msg):",decoded['error_msg'],
		
	


if __name__ == '__main__':
	auth("你的微博用户名","你的博密码","3471849585","7b0dd7f9ba微e77257734586afcfbafd38","https://api.weibo.com/oauth2/default.html")
