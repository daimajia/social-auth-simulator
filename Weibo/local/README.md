
	一切在本地即可完成模拟登陆、授权、获取access_token
	让密码更安全。

### 用法：

```python
from weibo import WeiboAutoAuth

api = WeiboAutoAuth('你的app_key','你的app_secret','你的appredirect_uri','微博用户名','微博密码')

print api.get_access_token()

```
