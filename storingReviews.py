#Headers
import re
import requests
import sqlite3
import nltk
import time
from bs4 import BeautifulSoup

#Declare productReview class
class productReview:
    def __init__(self):
        self.pid = ''
        self.userReviews = []
        self.userScores = []
        self.productFeatures = []
        self.featureScore = []
        self.featureOccurence = []
        self.count = 0

    def addReview(self,review,score):
        self.userReviews.append(str(review))
        self.userScores.append(str(score))
        self.count += 1

    def displayList(self,limit=-1):
        if limit == -1:
            span = self.count
        else:
            span = limit
        for itemno in range(span):
            print('----------------------------------------------------')
            print('User Score : ', self.userScores[itemno])
            print('User Review : ')
            print(self.userReviews[itemno])

    def updateFeature(self,feature,score):
        index = self.productFeatures.index(feature)
        self.featureScore[index] += score
        self.featureOccurence[index] += 1

    def addFeatures(self):
            noSpec = int(input('Enter no.of specifications : '))
            print (' Choose specifications : ')
            for i in range(noSpec):
                feature = input()
                self.productFeatures.append(str(feature))
                self.featureOccurence.append(0)
                self.featureScore.append(0)

    def displayFeature(self):
            print('***************  Product Summary ***************')
            for item in self.productFeatures:
                index = self.productFeatures.index(item)
                if self.featureOccurence[index] == 0:
                    print(str(item),' : -NA- ')
                else:
                    totalScore = int(self.featureScore[index])/int(self.featureOccurence[index])
                    print(str(item),' : ',str(totalScore))


#Initialize productReview class
reviewList = productReview()



#Connecting to knowledgeBase
conn = sqlite3.connect('ReviewStore.db')
c = conn.cursor()


#Assigning Website
url = 'http://www.flipkart.com/search'
MAIN_SITE = 'http://www.flipkart.com'


#Feeding Product Name and passing it to website's search
QUERY = input('Product Name : ')
#r = requests.get(url)
payload = {'q': QUERY, 'as' : 'off' , 'as-show' : 'off' , 'otracker' : 'start'}
r = requests.get(url , params=payload)



#Getting product listings
soup =  BeautifulSoup(r.content)
item_list = soup.find_all("a",{"class":"fk-display-block"})
count = 0
for item in item_list:
    count = count + 1
    print(str(count)+". "+item.get('title'))


#Choice product from listing
choice = input('Choose product : ')
item = item_list[int(choice)-1]

item_url = MAIN_SITE + item.get('href')


'''Getting Specifications
req_item_url = requests.get(item_url)
soup_item = BeautifulSoup(req_item_url.content)
spec_list = soup_item.find_all("td",{"class":"specsKey"})
specificationList = ['']*len(spec_list)
 for spec in spec_list:
    specificationList[spec_list.index(spec)] = spec.string
'''




pid = re.findall(r'pid=(.*)\&otracker',item_url)

temp_url = re.sub(r'\/p\/','/product-reviews/',item_url)
review_url = re.sub(r'&otracker.+','&type=all',temp_url)

#print(review_url)





req_url = requests.get(review_url)
soup = BeautifulSoup(req_url.content)


review_statement = soup.find_all("span",{"class":"nav_bar_result_count"})
review_statement = str(review_statement[0])
reg_number = re.compile(r'\d+')
list_review_info = reg_number.findall(review_statement)
total_no_of_reviews = int(list_review_info[0])
reviews_per_page = int(list_review_info[1])


temp_url = re.sub(r'type=all','rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=',review_url)

for i in range(0,(total_no_of_reviews + 1),10):
    print(i)
    
    if i > total_no_of_reviews:
        break
    else:
        section_number = str(i)

        req_temp_url = requests.get(temp_url+section_number)
        soup_temp = BeautifulSoup(req_temp_url.content)


        fullReview = soup_temp.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})
        for item in fullReview:
            m = re.search(r'<span class=\"review-text\">(.*) </span>',str(item),re.DOTALL)
            tempSoup = BeautifulSoup(m.group(0))
            sco = re.findall(r'<div class=\"fk-stars\" title=\"(\d) stars?\">',str(item))
            reviewList.addReview(tempSoup.text,sco[0])



print('No.of reviews found : ' + str(reviewList.count))


c.execute('delete from productList where productID =(?)',(pid[0],))
conn.commit()
c.execute('delete from userReviews where pid =(?)',(pid[0],))
conn.commit()

reviewList.pid = pid
timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
c.execute('insert into productList values (?,?,?)',(QUERY,pid[0],timestamp,))
conn.commit()


for i in range(reviewList.count):
    c.execute('insert into userReviews values(?,?,?)',(reviewList.pid[0],reviewList.userScores[i],reviewList.userReviews[i],))

conn.commit()