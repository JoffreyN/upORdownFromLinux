# Linux、Windows文件互传
## 说明
1、从linux各文件夹挑选一些文件下载到windows；<br>
2、从Windows上传文件到linux各文件夹；<br>
3.使用的库：paramiko,os,argparse

## 使用
- 显示帮助
~~~
upORdownFromLinux.py -h

程序功能：1、从linux各文件夹挑选一些文件下载到windows；2、从Windows上传文件到linux各文件夹

positional arguments:
  upordown    up:从Windows上传到Linux; down:从Linux下载到Windows

optional arguments:
  -h, --help  show this help message and exit
  -t HOST     Linux主机:ssh用户名:ssh密码，如 192.168.184.133:root:123
  -f FPATH    txt文档的路径，内容为linux中需要传送的所有文件名全路径，一行一个
  -w WPATH    windows保存的目录
~~~
- 下载
~~~
upORdownFromLinux.py down -l 192.168.184.133:root:123 -f E:\ZP\Desktop\test\test.txt -w E:\ZP\Desktop\test
~~~
- 上传
~~~
upORdownFromLinux.py up -l 192.168.184.133:root:123 -f E:\ZP\Desktop\test\test.txt -w E:\ZP\Desktop\test
~~~
