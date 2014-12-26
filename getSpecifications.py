import re
import requests
from bs4 import BeautifulSoup




url = 'http://www.flipkart.com/search'
MAIN_SITE = 'http://www.flipkart.com'



#QUERY = input('Product Name : ')
QUERY = 'nexus 5'

r = requests.get(url)
payload = {'q':QUERY,'as':'off','as-show':'off','otracker':'start'}
r = requests.get(url,params=payload)
#print(r.url)
soup =  BeautifulSoup(r.content)
item_list = soup.find_all("a",{"class":"fk-display-block"})
count = 0
'''for item in item_list:
    count = count + 1
    print(str(count)+". "+item.get('title'))
'''

#choice = input('Choose product : ')
choice = '1'

item = item_list[int(choice)-1]
#print(MAIN_SITE + item.get('href'))

item_url = MAIN_SITE + item.get('href')

req_item_url = requests.get(item_url)
soup_item = BeautifulSoup(req_item_url.content)
spec_list = soup_item.find_all("td",{"class":"specsKey"})
#<td class="specsKey">Secondary Camera</td>

print ('Specifications : ')
for specs in spec_list:
    print(specs.string)
