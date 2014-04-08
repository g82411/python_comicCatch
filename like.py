#coding=utf-8
import urllib2
import re
import io
import os
import gevent
from gevent import monkey
def big5(str):
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
        try:
            img=readUrl(url)
        except Exception as e:
            f.close
            downloadImg(url)
        filename=re.findall('(\d)/(\d+)_\w+.jpg',url)[0]
        f = open (filename[0].zfill(3)+_+filename[1],'wb')
        f.write(img)
        f.close
        print 'Ch.'+str(i)+'/'+str(len(k))+'page:'+str(p)+'/'+str(dict.get('pageNumber'))
        pass
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
def catchComic(url):
    def ss(a,b,c,d):
        e = a[b:b+c]
        if d == None:
            e=re.sub('[a-zA-z]*gi','')
            return e
        else:
            return e
        pass
    
    p = 1
    f = 50
    cs = re.findall('cs=\'(\w+)\'',readUrl(url))
    cc=len(cs)
    for i in range(cc/f):
        if()


    '''k = re.findall('(\d+.\d+.\d+.\d+.\w{40})',readUrl(url))
    number = re.findall ('(\d+).html',url)[0]
    creatPath(number)
    os.chdir('./'+number+'/')
    urls=[]
    for i in range (len(k)):
        dict={'ch':k[i].split(' ')[0],'server':k[i].split(' ')[1],'index':k[i].split(' ')[2],'pageNumber':k[i].split(' ')[3],'pageID':k[i].split(' ')[4]}
        for p in range (int(dict.get('pageNumber'))+1):
            if p == 0 or os.path.exists(str(i)+'_'+str(p)+'.jpg'):
                print 'File'+str(i)+'_'+str(p)+'.jpg'+'exists'
                continue
            m = (int((p - 1) / 10) % 10) + (((p - 1) % 10) * 3);
            urls.append('http://img'+str(dict.get('server'))+'.8comic.com/'+str(dict.get('index'))+'/'+str(number)+'/'+str(dict.get('ch'))+'/'+str(p).zfill(3)+'_'+str(dict.get('pageID')[m:m+3])+'.jpg')

    jobs = [gevent.spawn(downloadImg, url,filename) for url in urls]
    gevent.joinall(jobs)'''
    pass

monkey.patch_all()
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
input = [str(raw_input('>>>>請輸入名稱以搜尋:'))]
req = urllib2.Request('http://www.8comic.com/member/search.aspx?k='+input[0]+'&button=%B7j%B4M', txdata, txheaders)
searchResult = re.findall('href=\"/html/(\d+)\.html',urllib2.urlopen(req).read())
for i in range (len(searchResult)):
    print str(i+1)+'.'+re.findall('<font color="#FF6600" style="font:12pt;font-weight:bold;">(.+)</font> <b><font color="#999900"?',readUrl('http://www.8comic.com/html/'+str(searchResult[i])+'.html'))[0].decode('big5', 'ignore')+'\r'
numberwant = [str(raw_input('>>>>請輸入要下載的漫畫:'))]
catid=re.findall('cview\(\''+searchResult[int(numberwant[0])-1]+'-1\.html\',(\d+)',readUrl('http://www.8comic.com/html/'+searchResult[int(numberwant[0])-1]+'.html'))[0]
#print cview(int(re.findall('cview\(\'\d+-\d+\.html\',(\d+)',readUrl('http://www.8comic.com/html/'+searchResult[int(numberwant[0])]+'.html')[0])),searchResult[int(numberwant[0])])
catchComic(cview(int(catid),searchResult[int(numberwant[0])-1]))
