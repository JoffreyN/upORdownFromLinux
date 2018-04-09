import paramiko,os,argparse

parser=argparse.ArgumentParser(description='程序功能：1、从linux各文件夹挑选一些文件下载到windows；2、从Windows上传文件到linux各文件夹')
parser.add_argument(dest='upordown',help="up:从Windows上传到Linux; down:从Linux下载到Windows")
parser.add_argument('-l',dest='host',help="Linux主机:ssh用户名:ssh密码，如 192.168.184.133:root:123",required=True)
parser.add_argument('-f',dest='fpath',help="txt文档的路径，内容为linux中需要传送的所有文件名全路径，一行一个",required=True)
parser.add_argument("-w",dest='wpath',help="windows保存的目录",required=True)
args=parser.parse_args()

def main():
	host,username,password=args.host.split(':')
	trans=paramiko.Transport((host,22))
	trans.connect(username=username,password=password)
	sftp=paramiko.SFTPClient.from_transport(trans)
	for line in open(args.fpath,'r'):
		rpath=line.rstrip('\n')#linux中单个文件或文件夹名称
		lpath=os.path.join(args.wpath,os.path.split(rpath)[1])#Windows保存的文件全路径,如：E:/ZP/Desktop/kvm1.nasl
		if args.upordown=='up':
			sftp.put(localpath=lpath, remotepath=rpath)
		elif args.upordown=='down':			
			sftp.get(remotepath=rpath,localpath=lpath)
		else:
			print('无效操作！输入up或down')
			break
	trans.close()

if __name__ == '__main__':
	main()