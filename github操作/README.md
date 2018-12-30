# python
python学习笔记 准备操作参考 https://blog.csdn.net/helloworld19970916/article/details/75252085 http://www.runoob.com/w3cnote/git-guide.html
准备账号 
线上平台建立项目

本地下载git 
建立仓库git init
配置Git 
    $ ssh-keygen -t rsa -C "your_email@youremail.com"    //建立ssh key
    线上仓库配置相应的ssh key
    设置username和email
           $ git config --global user.name "your name"
           $ git config --global user.email "your_email@youremail.com"
    git bash cd进入指定本地仓库
   
  
1.git pull 
   $ git pull origin master --allow-unrelated-histories 从线上库下载
   https://segmentfault.com/q/1010000006036782 关于git pull 总提示让输入merge 信息
   输入merge 信息  按 i 插入内容  esc 结束 之后输入 :wq 返回命令行

2. git add
  添加修改

3. git commit 
  提交

4 git push
 上传线上库
 $ git push --set-upstream origin master

