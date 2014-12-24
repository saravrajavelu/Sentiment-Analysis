import re
import requests
import sqlite3
import nltk
import time
from bs4 import BeautifulSoup




url = 'http://www.flipkart.com/search'
MAIN_SITE = 'http://www.flipkart.com'



QUERY = input('Product Name : ')
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
review_url = re.sub(r'&otracker.+','&type=all',temp_url)

#print(review_url)





req_url = requests.get(review_url)
soup = BeautifulSoup(req_url.content)

review_list = soup.find_all("span",{"class":"review-text"})

review_statement = soup.find_all("span",{"class":"nav_bar_result_count"})
review_statement = str(review_statement[0])
reg_number = re.compile(r'\d+')
list_review_info = reg_number.findall(review_statement)
total_no_of_reviews = int(list_review_info[0])
reviews_per_page = int(list_review_info[1])


temp_url = re.sub(r'type=all','rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=',review_url)

for i in range(10,(total_no_of_reviews + 1),10):
    #if i > total_no_of_reviews:
    #For testing purpose only
    if i > 10:
        break
    else:
        section_number = str(i)
        
        req_temp_url = requests.get(temp_url+section_number)
        soup_temp = BeautifulSoup(req_temp_url.content)
        review_list = review_list + soup_temp.find_all("span",{"class":"review-text"})

print('No.of reviews found : ' + str(len(review_list)))


''' Remove this comment to print all the reviews

for i in review_list:
    print (i)

'''

#print (review_list[1].text)




conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

'''
def createDB():
    c.execute("")
'''

exampleReview = """Have been Using this phone for more than a Week Now, must say I am very impressed with it.The processor is Super fast and the 2GB RAM makes sure, apps never Lag no matter what. The touch is one of the best in a smartphone. Android Kitkat is simply awesome, very smooth UI and Nexus will b always first to get the Updates, what more can you ask for?
The Display is FULL HD (445 ppi), the clarity is simply superb. The battery lasts about a Day with Moderate usage, but with heavy usage will last for about 12-15 Hours. All in all, you can't ask for a better phone under 30k. Did I also mention how light the phone is? It's so light that u don't even feel it in you hands! 
If your Budget is 30k, go get this phone, don't even think twice!"""


def processor(data):
    try:
        tokenized = nltk.word_tokenize(data)
        tagged = nltk.pos_tag(tokenized)
        namedEnt = nltk.ne_chunk(tagged, binary=True)
        #print (namedEnt)
        #time.sleep(55)

        entities = re.findall(r'NE\s(.*?)/',str(namedEnt))
        descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'',str(tagged))
        if len(entities) > 1:
            pass
        elif len(entities) == 0:
            pass
        else:
            print ('______________________________________')
            print ('Named : ',entities[0])
            print ('Descriptions : ')
            for desc in descriptives:
                print (desc)

 
    except Exception as e:
        print ('Failed in the first loop of processor')  
        print (str(e))
        
for review_list_item in review_list:
    processor(review_list_item.text)
