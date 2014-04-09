#coding=Utf8
import re
import urllib2
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
input = [str(raw_input('>>>>請輸入名稱以搜尋:'))]
searchResult=re.findall('<a href=\"(http://comic.sfacg.com/HTML/\w+)\" id="SearchResultList\d___ResultList_ctl\d+_LinkInfo" class="orange_link2">(.+)</a>',readUrl('http://s.sfacg.com/?Key='+Utf8toBig5(input[0])+'&S=&SS='))
for i in range(len(searchResult)):
    print str(i)+'.'+searchResult[i][1]
choice=[str(raw_input('>>>>請輸入代號:'))][0]
chList=re.findall('/HTML/\w+/(\w+)/',readUrl(searchResult[int(choice)][0]))
print chList
