
import urllib
from urllib.request import urlopen
import re
import http.cookiejar
from http.cookiejar import CookieJar
import time
import html5lib
from bs4 import BeautifulSoup

cj=http.cookiejar.CookieJar()
#opener = urllib.build_opener(urllib2.HTTPCookieProcessor(cj))
#opener.addheaders = [('User-agent','Mozilla/5.0')]



page = 'http://www.flipkart.com/google-nexus-5/product-reviews/ITMDZKKQHQXYC64R?pid=MOBDQ9VXZMHXZGBP&type=top'

soup = BeautifulSoup(open("http://www.flipkart.com/google-nexus-5/product-reviews/ITMDZKKQHQXYC64R?pid=MOBDQ9VXZMHXZGBP&type=top"))

soup = BeautifulSoup("<html>data</html>")


import urllib.request
with urllib.request.urlopen("http://www.python.org") as url:
    sourceCode = url.read()
#print(sourceCode)

sourceCode = str(sourceCode)

#titles = re.findall(r'<span class=\"review-text\">[a-z A-Z \n , \d . <>\':;() \/ ]*</span>',sourceCode,re.DOTALL)
#titles = re.findall(r'<span class=\"review-text\">(.)*</span>',sourceCode,re.DOTALL)


#p = re.compile(ur'<span class=\"review-text\">(.*)</span>',re.DOTALL)
#test_str = u"<span class=\"review-text\">I agree that the technical specs of the product and great, pricewise I am not sure if 30K is cheap as what every one feels is really cheap.<br </span><br />\nBut anyways, my biggest concern with this device is call quality. If you read on the net, you will find enough issues and google doesn't seem to know/have any clue on the fix. What I have faced:<br />\n1. People whom I call say they hear hissing noise, words get broken/go missing<br />\n2. Can't hear or the voice feels muffled.<br />\n3. This happens especially when you are connected via headset provided with the device or while connected through the incar BT audio (like in Figo)<br />\n4. I have tried Samsung S4 headset and even those seem to have same problems with this device<br />\n<br />\nI complained and google did replace the device with a new one, but unfortunately the problems are not gone. I have been using a Nokia N8, S4 and iPhone and have never faced these issues. The calls I make have been on the same locality, so we can rule out signal issues. <br />\n<br />\nSo if you are planning to buy this device paying 30K, keep in mind these call related issues. I would suggest you read the other writeups on the net and you will know this is not a one off case and there are generic call related issues with this device. <br />\n<br />\nSo a great phone with best specs but cannot make good quality phone calls. BTW, google offers refund policy in USA but not in India. </span>"
 
#titles = re.findall(p, sourceCode)

#regex = re.compile("<span class=\"review-text\">[a-z A-Z \n , \d . <>\':;() \/ ]*</span>", re.DOTALL)
#titles = regex.findall(sourceCode)


st = '''<span class=\"review-text\">I'm some
               fancy text that needs
               to be found</span>'''

pattern = re.compile(r'<span class=\"review-text\">[a-z A-Z \n , \d . <>\':;() \/ ]*</span>', re.DOTALL)
titles = pattern.findall(sourceCode)
print(sourceCode)
for title in titles:
    print(title)





for title in titles:
    print (title)
#links  = re.findall(r'<link.*?href=\"(.*?)\"',sourceCode)
#for link in links:
#    if '.rdf' in link:
#        pass
#    else:
#        print ('lets \'s visit:',link)
#        linkSource = opener.open(link).read()
#        content = re.findall(r'<p>(.*?)</p>',linkSource)
#        for theContent in content:
#            print (theContent)
#
#time.sleep(555)
