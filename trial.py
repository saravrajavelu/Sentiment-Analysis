'''import requests
import re
from bs4 import BeautifulSoup

with requests.Session() as c:
    url = 'http://www.flipkart.com/'
    QUERY = 'nexus 5'
    c.get(url)
    search_data = dict(q=QUERY)
    page = c.get(url, data=search_data)
    soup =  BeautifulSoup(page.content)

url = 'http://www.flipkart.com/search'
MAIN_SITE = 'http://www.flipkart.com'
QUERY = 'nexus 5'
r = requests.get(url)
payload = {'q':QUERY,'as':'off','as-show':'off','otracker':'start'}
r = requests.get(url,params=payload)
#print(r.url)
soup =  BeautifulSoup(r.content)
item_list = soup.find_all("a",{"class":"fk-display-block"})
count = 0
for item in item_list:
    count = count + 1
    print(str(count)+". "+item.get('title'))


choice = input('Choose product : ')
item = item_list[int(choice)-1]
#print(MAIN_SITE + item.get('href'))

item_url = MAIN_SITE + item.get('href')

temp_url = re.sub(r'\/p\/','/product-reviews/',item_url)
review_url = re.sub(r'&otracker.+','$type=all',temp_url)

print(review_url)
'''
from numpy.ma.mrecords import openfile
import re
f = open("AFINN-111.txt","r")
temp = re.findall(r'(.*)',f.read())
for item in temp:
    if len(item) == 0:
        pass
    else:
        print(item.split("\t",2))
#print(temp)
#print(f.read())
