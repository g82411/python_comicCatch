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
k=readUrl('http://s.sfacg.com/?Key=%u6E90%u541B&S=&SS=')
print k
print re.findall('alt=\"(.+)\" />',k)[0].decode('utf8', 'ignore')
