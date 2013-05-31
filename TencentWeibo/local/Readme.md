###腾讯微博登陆，授权，认证

用法依旧简单至极

```python

from tencentweibo import TencentWeiboAutoAuth

api = TencentWeiboClient('app id','app_secret','app_redirect_uri','qq号','qq 密码')
print api.get_access_token()
print 'OpenId:',api.get_openid()
print 'OpenKey:',api.get_openkey()

```