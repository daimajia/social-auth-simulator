#用法：

#预备工作
采用了python `Falsk`web框架，请预先安装

安装方法：`pip install flask` or `easy_install flask`

#部署

1.部署Server文件夹中 `index.py`, `../local/weibo.py` 以及两个目录下的`__init__.py` 文件到服务器

2.在test.py中填入你的部署的`auth_url`地址，并且填入你的测试账号的微博用户名，微博密码
 
3.执行`python test.py`即可查看到获取的`access_token`系列数据。

也可以直接采用本地测试方法：

1	`python index.py`启动服务器

2	填入test.py中用户名和密码

3	`python test.py`