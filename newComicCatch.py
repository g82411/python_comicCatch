#coding=big5
import gevent
import urllib2
import os
import re
from gevent import monkey
def Big5toUtf8(str):
    return str.decode('big5', 'ignore').encode('utf-8', 'ignore')
def Utf8toBig5(str):
    return str.decode('utf-8', 'ignore').encode('big5', 'ignore')
def readUrl(url):
        req = urllib2.urlopen(url)
        html_src = req.read()
        return html_src
        pass
def creatPath(pathName):
        if not os.path.exists(pathName):
            os.mkdir(pathName)
        pass
def downloadImg(url):
        print url
        try:
            img=readUrl(url)
        except Exception as e:
            log=open('log.txt','w+')
            log.write(str(e)+'\r\n')
            log.close
        filename=re.findall('/(\d+)/(\d+)_\w+.jpg',url)[0]
        f = open (filename[0].zfill(3)+'_'+filename[1]+'.jpg','wb')
        f.write(img)
        f.close
        print filename[0]+'_'+filename[1]
        pass
def catchComic(url):
    urls=[]
    htmlText=readUrl(url)
    ti=re.findall('ti=(\d+)',htmlText)[0]
    chs=re.findall('chs=(\d+)',htmlText)[0]
    cs = re.findall('cs=\'(\w+)\'',htmlText)[0]
    comicHash=[]
    for i in range (len(cs)/50):
        comicHash.append(cs[i*50:(i+1)*50])
    def mm(p):
        return (int((p - 1) / 10) % 10) + (((p - 1) % 10) * 3)
    def comicHashDecode(comicHashString):
        resultUrl=[]
        numberOfPages=re.findall('(\d+)',comicHashString[7:10])[0]
        for page in range(1,int(numberOfPages)+1):
            urls.append('http://img'+re.findall('(\d+)',comicHashString[4:6])[0]+'.8comic.com'+'/'+re.findall('(\d+)',comicHashString[6:7])[0]+'/'+ti+'/'+re.findall('(\d+)',comicHashString[0:4])[0]+'/'+ str(page).zfill(3)+'_'+comicHashString[mm(page)+10:mm(page)+13]+'.jpg')
    for j in range(len(comicHash)):
        comicHashDecode(comicHash[j])
    f = open('test.txt','w+')
    monkey.patch_all()
    jobs = [gevent.spawn(downloadImg, url) for url in urls]
    gevent.joinall(jobs)
def cview(catid,number):
        baseurl=''
        if(catid==4 or catid==6 or catid==12 or catid==22 ):
            baseurl="http://new.comicvip.com/show/cool-"
        if(catid==1 or catid==17 or catid==19 or catid==21):
            baseurl="http://new.comicvip.com/show/cool-"
        if(catid==2 or catid==5 or catid==7 or catid==9):
            baseurl="http://new.comicvip.com/show/cool-"
        if(catid==10 or catid==11 or catid==13 or catid==14):
            baseurl="http://new.comicvip.com/show/best-manga-"
        if(catid==3 or catid==8 or catid==15 or catid==16 or catid==18 or catid==20):
            baseurl="http://new.comicvip.com/show/best-manga-"
        return baseurl+str(number)+'.html?ch=1'
txdata = None
txheaders = {
    'Host': 'www.8comic.com\r\n',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cookie': 'comichistory=8323%7C%25u6E90%25u541B%25u7269%25u8A9E%2C102%7C%25u706B%25u5F71%25u5FCD%25u8005%2C6942%7C%25u5496%25u83F2%25u5075%25u63A2%25u90E8%2C8792%7C%25u8056%25u9B25%25u58EB%25u661F%25u77E2%25u03A9; __atuvc=5%7C8\r\n'
}
input = [str(raw_input('>>>>:'))]
req = urllib2.Request('http://www.8comic.com/member/search.aspx?k='+Utf8toBig5(input[0])+'&button=%B7j%B4M', txdata, txheaders)
searchResult =  re.findall('<a href="/html/(\d+)\.html">',Big5toUtf8(urllib2.urlopen(req).read()))
resultUrl='http://www.8comic.com/html/'
comicDir=[]
for i in range(len(searchResult)):
    comicDir.append(Big5toUtf8(re.findall('<font color="#FF6600" style="font:12pt;font-weight:bold;">(.+)</font> <b><font color="#999900">',readUrl(resultUrl+searchResult[i]+'.html'))[0]))	
    print str(i+1)+comicDir[i]
numberwant = [str(raw_input('>>>>:'))]
catid=re.findall('cview\(\'(\d+)-1\.html\',(\d+)\)',readUrl('http://www.8comic.com/html/'+searchResult[int(numberwant[0])-1]+'.html'))[0]
creatPath(comicDir[int(numberwant[0])-1])
os.chdir(comicDir[int(numberwant[0])-1])
catchComic(cview(int(catid[1]),catid[0]))