weibo-simulator
===============

	php模拟微博登陆->授权->获取access_token

**用法：**
----
------
 *1.部署`saev2.ex.class.php`,`weibo_auto_auth.class.php`,`auth.php`文件到服务器

 *2.在test.py中填入你的部署的`auth.php`文件地址，并且填入你的测试账号的微博用户名，微博密码
 
 *3.执行`python test.py`即可查看到获取的`access_token`系列数据。
 
 -------
 
 php文件模拟了用户的登陆，对app的授权，以及post获取access_token请求