import re
import requests
import sqlite3
import nltk
import time
from bs4 import BeautifulSoup
url = 'http://www.thesaurus.com/browse/' + 'bad' + '?s=t'
req = requests.get(url)
soup = BeautifulSoup(req.content)
temp = soup.find_all("div",{"class":"heading-block oneClick-disabled"})
no_of_syn = re.findall(r'<strong>(.*)</strong>',str(temp[0]))
no_of_syn = int(no_of_syn[0])
relevant_list = soup.find_all("span",{"class":"text"},limit = no_of_syn)
for list_item in relevant_list:
    
    print(list_item)
    

print(no_of_syn)
