### 人人自动认证

#### 关于

提供足够信息，包括`app_id`,`app_key`,`app_secret`.`app_redirect_uri`,`人人username`,`人人password`，不用再开浏览器，即可完成所有的授权获取到access_token等信息。

####Demo
接口简单至极:

```python

from renren import RenrenAutoAuth

api = RenrenAutoAuth('你的app Id','你的 app Key','你的app secret','你的app redirect uri','人人账号','人人密码')

print api.get_access_token()

```
