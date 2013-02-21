weibo-simulator
===============

	php模拟微博登陆->授权->获取access_token

**用法：**
----
------
 *1.部署Server文件夹中 `saev2.ex.class.php`,`weibo_auto_auth.class.php`,`auth.php`文件到服务器

 *2.在test.py中填入你的部署的`auth.php`文件地址，并且填入你的测试账号的微博用户名，微博密码
 
 *3.执行`python test.py`即可查看到获取的`access_token`系列数据。
 
 -------
 
 说明：
 
 在AnotherSolution文件夹中，存储了两个Python文件，实现了在本地发送并直接请求新浪服务器，不经过第三方服务器端的实现。
 只要在`sina.py`中，修改您的微博用户名、密码、app_key,app_secret,callback_rui，而后运行`sina.py`即可完成授权，并且获取到access_token。
 
 php文件模拟了用户的登陆，对app的授权，以及post获取access_token请求
 
 即将添加人人模拟,借鉴小黄鸡