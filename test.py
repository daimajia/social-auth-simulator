import urllib
import urllib2

auth_url = "http://end.zhan-dui.com/weibo/test.php"

##3471849585
##7b0dd7f9bae77257734586afcfbafd38
##https://api.weibo.com/oauth2/default.html

def auth(uid,password,app_key,app_secret,callback_uri):
	params = urllib.urlencode({'userid':uid,'password':password,'app_key':app_key,'app_secret':app_secret,'callback_uri':callback_uri})
	req = urllib2.Request(url=auth_url,data=params);
	f = urllib2.urlopen(req)
	print f.read()

if __name__ == '__main__':
	auth("你的微博用户名","你的微博密码","3471849585","7b0dd7f9bae77257734586afcfbafd38","https://api.weibo.com/oauth2/default.html")