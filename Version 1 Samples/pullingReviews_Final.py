import re
import requests
from bs4 import BeautifulSoup

class productReview:
	def __init__(self):
		self.userReviews = []
		self.userScores = []
		self.length = 0
	def addReview(self,review,score):
		self.userReviews.append(str(review))
		self.userScores.append(str(score))
		self.length += 1
	def displayList(self,limit=-1):
		if limit == -1:
			span = self.length
		else:
			span = limit
		for itemno in range(span):
			print('----------------------------------------------------')
			print('User Score : ',self.userScores[itemno])
			print('User Review : ')
			print(self.userReviews[itemno])


reveiwList = productReview()

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
nom = 0

'''
fullReview = soup.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})
for item in fullReview:
    m = re.search(r'<span class=\"review-text\">(.*) </span>',str(item),re.DOTALL)
    tempSoup = BeautifulSoup(m.group(0))
    sco = re.findall(r'<div class=\"fk-stars\" title=\"(\d) stars\">',str(item))
    reveiwList.addReview(tempSoup.text,sco[0])
    nom += 1
    print(nom)
'''
'''
review_list = soup.find_all("span",{"class":"review-text"})
userScore = soup.find_all(attrs={"class":"fk-stars"})
for item in userScore:
    print(re.findall(r'<div class=\"fk-stars\" title=\"(\d) stars\">',str(item)))
'''


review_statement = soup.find_all("span",{"class":"nav_bar_result_count"})
review_statement = str(review_statement[0])
reg_number = re.compile(r'\d+')
list_review_info = reg_number.findall(review_statement)
total_no_of_reviews = int(list_review_info[0])
reviews_per_page = int(list_review_info[1])


temp_url = re.sub(r'type=all','rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=',review_url)

for i in range(0,(total_no_of_reviews + 1),10):
    if i > total_no_of_reviews:
        break
    else:
        section_number = str(i)
        
        req_temp_url = requests.get(temp_url+section_number)
        soup_temp = BeautifulSoup(req_temp_url.content)
        #review_list = review_list + soup_temp.find_all("span",{"class":"review-text"})


        fullReview = soup_temp.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})
        for item in fullReview:
            m = re.search(r'<span class=\"review-text\">(.*) </span>',str(item),re.DOTALL)
            tempSoup = BeautifulSoup(m.group(0))
            sco = re.findall(r'<div class=\"fk-stars\" title=\"(\d) stars?\">',str(item))
            reveiwList.addReview(tempSoup.text,sco[0])
            nom += 1
            print(nom)




        

print('No.of reviews found : ' + str(reveiwList.length))


''' Remove this comment to print all the reviews

for i in review_list:
    print (i)

'''

#print (review_list[1].text)
