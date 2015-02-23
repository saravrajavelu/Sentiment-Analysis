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

review_url = 'http://www.flipkart.com/google-nexus-6/product-reviews/ITME3H5VHKYTQGNF?pid=MOBEFAGFZHG7SRZU&type=all'

req_url = requests.get(review_url)
soup = BeautifulSoup(req_url.content)

nom = 0


fullReview = soup.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})
for item in fullReview:
    m = re.search(r'<span class=\"review-text\">(.*) </span>',str(item),re.DOTALL)
    tempSoup = BeautifulSoup(m.group(0))
    sco = re.findall(r'<div class=\"fk-stars\" title=\"(\d) stars\">',str(item))
    reveiwList.addReview(tempSoup.text,sco[0])
    nom += 1
    print(nom)
    #print(item)


'''
score = soup.find_all(attrs={"class":"fk-stars"})

for item in score:
    print(re.findall(r'<div class=\"fk-stars\" title=\"(\d) stars\">',str(item)))
'''
