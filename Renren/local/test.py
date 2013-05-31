from renren import RenrenAuthAutomatic

api = RenrenAutoAuth('你的app Id','你的 app Key','你的app secret','你的app redirect uri','人人账号','人人密码')

print api.get_access_token()
