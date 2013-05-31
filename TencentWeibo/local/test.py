
from tencentweibo import TencentWeiboAutoAuth

api = TencentWeiboAutoAuth('app id','app_secret','app_redirect_uri','qq号','qq 密码')
print api.get_access_token()
print 'OpenId:',api.get_openid()
print 'OpenKey:',api.get_openkey()