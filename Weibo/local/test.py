# -*- coding: utf8 -*-
from weibo import WeiboAutoAuth

app_key = '3530915833' #请修改成您的app_key
app_secret = 'f34a9eb3404c7f99b5e8466e18ce9b6e' #请修改成您的app_secret
redirect_uri = 'http://snsapi.sinaapp.com/auth.php' #请修改成您的redirect_uri
username = '' #请修改成您的测试用户名
password = '' #请修改成您的测试微博密码

api = WeiboAutoAuth(app_key,app_secret,redirect_uri,username,password)

print api.get_access_token()