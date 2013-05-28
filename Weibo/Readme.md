###关于微博模拟认证
`说明：`该目录存在两个文件夹

*	`local`:local提供了本地的认证方法，只要提供微博用户名、密码、app_key、app_secret、callback uri即可本地的完成所有认证流程，直接得到可用的token。
*	`server`:将微博用户名和密码发回到服务器，服务器端进行认证和获取授权，而后返回token。