#Headers
import re
import requests
import sqlite3
import nltk
import time
from bs4 import BeautifulSoup

#Connecting to knowledgeBase
conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()


#Assigning Website
url = 'http://www.flipkart.com/search'
MAIN_SITE = 'http://www.flipkart.com'


#Feeding Product Name and passing it to website's search
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

'''Getting Specifications
req_item_url = requests.get(item_url)
soup_item = BeautifulSoup(req_item_url.content)
spec_list = soup_item.find_all("td",{"class":"specsKey"})
specificationList = ['']*len(spec_list)
 for spec in spec_list:
    specificationList[spec_list.index(spec)] = spec.string
'''






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
    if i > total_no_of_reviews:
        break
    else:
        section_number = str(i)
        
        req_temp_url = requests.get(temp_url+section_number)
        soup_temp = BeautifulSoup(req_temp_url.content)
        review_list = review_list + soup_temp.find_all("span",{"class":"review-text"})

print('No.of reviews found : ' + str(len(review_list)))



#print (review_list[1].text)


specificationList =['Battery','Touch','Display','Budget','Price','Processor','Screen']




def processor(review_list,specificationList):
    try:
        rating_for_spec_list = [0]*len(specificationList)
        hits_for_spec_list = [0]*len(specificationList)
        for exampleReview in review_list:
            try:
                
                sentences = re.findall(r'(.*?)[\.|\?|!+]',exampleReview.text)
                for sent in sentences:
                    tokenized = nltk.word_tokenize(sent)
                    tagged = nltk.pos_tag(tokenized)
                    namedEnt = nltk.ne_chunk(tagged, binary=True)
                    entities = re.findall(r'NE\s(.*?)/',str(namedEnt))
                        
                    descriptives_noun = re.findall(r'\(\'(\w*)\',\s\'NN\w?\'',str(tagged))
                    descriptives_verbs = re.findall(r'\(\'(\w*)\',\s\'VB\w?\'',str(tagged))
                    descriptives_adj = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'',str(tagged))
                    descriptives_adverb = re.findall(r'\(\'(\w*)\',\s\'RB\w?\'',str(tagged))


                    attr_list = descriptives_noun + entities
                    adj_list =  descriptives_adverb + descriptives_adj + descriptives_verbs
                    for attr in attr_list:
                        attr = attr.lower().capitalize()
                        if attr in specificationList:
                             for adj_item  in adj_list:
                                 c.execute('SELECT value from wordVals where word=?',(adj_item.lower(),))
                                 query_result = c.fetchone()   
                                 if query_result is None:
                                     pass
                                 else:
                                     rating_for_spec_list[specificationList.index(attr)] += int(query_result[0])
                                     hits_for_spec_list[specificationList.index(attr)] += 1
                            
                        else:
                            pass

            except Exception as e:
                print(str(e))
                print('Error - Processor - 2nd try')


        for spec in specificationList:
            if hits_for_spec_list[specificationList.index(spec)] == 0:
                print (spec + ' : NA ')
            else:
                temp_rating = rating_for_spec_list[specificationList.index(spec)]/hits_for_spec_list[specificationList.index(spec)]
                print (spec + ' :  ',temp_rating)
                
    except Exception as e:
        print(str(e))
        print('Error - Processor - 1st Try')

'''
def printRating():
    try:
        for spec in spec_list:
            if hits_for_spec_list[spec_list.index(spec)] == 0:
                print (spec + ' : NA ')
            else:
                temp_rating = rating_for_spec_list[spec_list.index(spec)]/hits_for_spec_list[spec_list.index(spec)]
                print (spec + ' :  ',temp_rating)

'''


processor(review_list,specificationList)
