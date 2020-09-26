#coding:utf-8
#only this file works!!!
from tkinter import *
import urllib.request
import urllib.error
import re
import os
import time
import pyperclip
import threading

class App:
	def __init__(self):
		self.loadInf()
		self.gotoMenu()
	def loadInf():
		pass
	def gotoMenu():
		pass
	def gotoSafariLocal(string):
		if string=='avxcl':
			return
		else:
			return
	def gotoSprider(string):
		if string=='avxcl':
			return
		else:
			return
	def gotoSettings():
		pass

class myThread (threading.Thread):
    def __init__(self, link):
        threading.Thread.__init__(self)
        self.link=link
    def run(self):
        downloadWithXfplayLink(self.link)

avxcl = 'http://www.laolulu5.com'
xfplay = '\'D:\\Program_Files\\xfplay\\xfplay.exe\''
selfpath=os.path.split(os.path.abspath(__file__))[0]

def getXfplayLinkAndName(url):
	'例如 http://www.avscj009.com/?q=909/juru/53217_0_1.html 即播放页面'
	time.sleep(0.5)
	try:
		print(url)
		htmlText = urllib.request.urlopen(url).read().decode('utf-8')
		link = re.search(r'"xfplay://.*"',htmlText).group()
		print(link)
		name = re.search(r'《.*》',htmlText).group()
		print(name)
		return [link,name.strip('《》')]
	except urllib.error.HTTPError as e:
		print(e.code)
		return None
	except:
		print('Wasted.')
		return None

def findXfplayLinksAndNames(url):
	'http://www.avscj009.com/?q=909/juru/53217.html'
	'注意到有些链接是旧网址，需要替换新网址'
	global avxcl
	tmpstr=re.split(r'/',url)
	if len(tmpstr)<2:
		return
	url=avxcl+'/'+tmpstr[-2]+'/'+tmpstr[-1]
	'替换完成'
	k=1
	linksAndNames=[]
	tmpstr=re.split(r'(\.html)',url)
	while(True):
		url2=tmpstr[0]+'_0_'+str(k)+tmpstr[1]
		linkAndName=getXfplayLinkAndName(url2)
		if linkAndName==None:
			return linksAndNames
		else:
			linksAndNames.append(linkAndName)
			k+=1

def downloadWithXfplayLink(link):
	os.system('""D:\\Program_Files\\xfplay\\xfplay.exe" %s'%link)
	#十分诡异的一点是，这里开头需要两个引号。

def stractNames(linkAndName):
	tmp=re.search(r'\|mz=[^|]*\|',linkAndName[0]).group()
	name0=tmp[4:-1]#链接中显示的名称，也是软件直接下载时创建的文件名，往往是番号名
	if isContainChineseChar(name0):
		name1=name0
	else:
		name1=linkAndName[1]+' '+name0#加上影片的正式名称，即艺名而非番号
	return [name0,name1]

def isContainChineseChar(string):
	for ch in string:
		if u'\u4e00' <= ch <= u'\u9fff':
			return True
	return False

# ~ os.system('D:')
# ~ os.system('cd "D:\\Program Files\\xfplay"')
# ~ os.system('"D:\\Program Files\\xfplay\\xfplay.exe" '+'"xfplay://dna=BGbfAHHWAeMdmGxYBeMfAGIdAGpWmxD2AZEgmwx4mdt4m0L4DZxZDD|dx=659236876|mz=突然SEX得手現在是不是在這裡中出.rmvb|zx=nhE0pdOVl3P5mF5xqzD5Ac5wo206BGa4mc94MzXPozS|zx=nhE0pdOVl3Ewpc5xqzD4AF5wo206BGa4mc94MzXPozS"')

#os.system('cd "D:\\Program Files\\xfplay"')
#os.system('"D:\\Program Files\\xfplay\\xfplay.exe"')
#os.system('""D:\\Program Files\\xfplay\\xfplay.exe" %s'%'"xfplay://dna=BGbfAHHWAeMdmGxYBeMfAGIdAGpWmxD2AZEgmwx4mdt4m0L4DZxZDD|dx=659236876|mz=突然SEX得手現在是不是在這裡中出.rmvb|zx=nhE0pdOVl3P5mF5xqzD5Ac5wo206BGa4mc94MzXPozS|zx=nhE0pdOVl3Ewpc5xqzD4AF5wo206BGa4mc94MzXPozS"')

while(True):
	s=input('paste urls ? (\'q\' to quit)\n')
	if s=='q':
		break
	urls=re.split(r'\s',pyperclip.paste())
	f = open(selfpath+'\\nameLog.txt','a',encoding='gbk')
	#print(urls)
	for u in urls:
		linksAndNames=findXfplayLinksAndNames(u)
		try:
			for l in linksAndNames:
				downloadWithXfplayLink(l[0])
				# threading._start_new_thread(downloadWithXfplayLink,(l[0],))
				tmpThread=myThread(l[0])
				names=stractNames(l)
				f.write('"'+names[0]+'":"'+names[1].replace('/','=')+'"\n')
				tmpThread.join()
		except:
			pass
		# ~ for l in linksAndNames:
			# ~ downloadWithXfplayLink(l[0])
			# ~ names=stractNames(l)
			# ~ f.write("'"+names[0]+"' '"+names[1]+"'")
	f.close()

'''http://www.avscj009.com/zhifu/53328.html
http://www.avscj009.com/juru/53334.html
http://www.avscj009.com/nvtong/53337.html
http://www.avscj009.com/shaonv/53341.html
http://www.avscj009.com/shaonv/53342.html
http://www.avscj009.com/zhifu/53343.html
http://www.avscj009.com/zhifu/53344.html'''
