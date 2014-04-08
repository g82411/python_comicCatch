#coding=utf8
import urllib2
import os
import re
import gevent
from gevent import monkey
#ch是章節
#f是每組字典的長度=50
#c是字典指標
def readUrl(url):
        req = urllib2.urlopen(url)
        html_src = req.read()
        return html_src
        pass
def creatPath(pathName):
        if not os.path.exists(pathName):
            os.mkdir(pathName)
        pass
def sp():
	cc = len(global cs)
	for i in range(cc / f):
		if(ss(cs,i*f,4)==ch)
global cs=re.findall('cs=\'(\w+)\'?',readUrl(url))
global f=50