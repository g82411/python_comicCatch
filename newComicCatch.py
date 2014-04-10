#coding=utf8
import urllib2
import os
import re
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
def catchComic(cs,ti):
    urls=[]
    def ss(a,b,c,d):
        e=a[b:b+c]
        if d==None:
            return re.sub('[a-z]','',e)
        else:
            return e
    def mm(p):
        return (int((p - 1) / 10) % 10) + (((p - 1) % 10) * 3);
    def sp(cs):
        c=''
        cc = len(cs)
        for i in range(cc / f):
        #f未定義
            if ss(cs,i * f , 4, None) == ch:
                #ch未定義
                c=ss(cs, i * f, f, f);
                break
        if c == '':
            c = ss(cs, cc - f, f,None)
        si(c)
    def si(c):
        #ti是漫畫代號
        urls.append('http://img' + ss(c, 4, 2,None) + '.8comic.com/' + ss(c, 6, 1,None) + '/' + ti + '/' + ss(c, 0, 4,None) + '/' + nn(p) + '_' + ss(c, mm(p) + 10, 3, f) + '.jpg')
