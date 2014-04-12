#coding=Utf8
import re
import urllib2
import os
import gevent
from gevent import monkey
def readUrl(url):
        req = urllib2.urlopen(url)
        html_src = req.read()
        return html_src
        pass
def creatPath(pathName):
        if not os.path.exists(pathName):
            os.mkdir(pathName)
        pass
#http://comic.sfacg.com/Utility/1506/013.js
#http://comic.sfacg.com/Utility/(comicPar)/(ch.).js
def Utf8toBig5(str):
    return str.decode('big5', 'ignore').encode('utf-8', 'ignore')
def downloadImg(url):
        try:
            img=readUrl(url)
        except Exception as e:
            f.close
            downloadImg(url)
        filename=re.findall('(\w+)/(\d+)_\w+.jpg',url)[0]
        f = open (filename[0].zfill(3)+'_'+filename[1]+'.jpg','wb')
        f.write(img)
        f.close
        pass
input = [str(raw_input('>>>>請輸入名稱以搜尋:'))]
searchResult=re.findall('<a href=\"(http://comic.sfacg.com/HTML/\w+)\" id="SearchResultList\d___ResultList_ctl\d+_LinkInfo" class="orange_link2">(.+)</a>',readUrl('http://s.sfacg.com/?Key='+Utf8toBig5(input[0])+'&S=&SS='))
for i in range(len(searchResult)):
    print str(i)+'.'+searchResult[i][1]
choice=[str(raw_input('>>>>請輸入代號:'))][0]
creatPath(searchResult[int(choice)][1].decode('utf-8','ignore'))
os.chdir('./'+searchResult[int(choice)][1].decode('utf-8','ignore')+'/')
comicCounterID = re.findall('var comicCounterID = (\d+)',readUrl(searchResult[int(choice)][0]))[0]
chList=re.findall('/HTML/\w+/(\w+)/',readUrl(searchResult[int(choice)][0]))
urls=[]
for i in range (len(chList)):
        hosts=re.findall('http://(\w+).sfacg.com',readUrl('http://comic.sfacg.com/Utility/'+comicCounterID+'/'+chList[i]+'.js'))[0]
        picUrl=re.findall('(/Pic/OnlineComic\d+/\w+/\w+/\d+_\w+\.jpg)',readUrl('http://comic.sfacg.com/Utility/'+comicCounterID+'/'+chList[i]+'.js'))
        for j in range (len(picUrl)):
                 urls.append('http://'+hosts+'.sfacg.com'+picUrl[i])
print urls
monkey.patch_all()
jobs = [gevent.spawn(downloadImg, url) for url in urls]
gevent.joinall(jobs)
