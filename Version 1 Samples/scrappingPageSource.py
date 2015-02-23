import re
import requests
from bs4 import BeautifulSoup
url = "http://www.flipkart.com/sony-playstation-4-ps4/product-reviews/ITMDRNSHTHV9EGMF?pid=GMCDNZCHPFVHKGAT&type=all"
r = requests.get(url)
soup = BeautifulSoup(r.content)

g_data = soup.find_all("span",{"class":"review-text"})
count = 0

for review in g_data:
    count = count  + 1
    
print(count)

result = soup.find_all("span",{"class":"nav_bar_result_count"})

print (result[0])

result = str(result[0])

print (result)

review_statement = soup.find_all("span",{"class":"nav_bar_result_count"})
reg_number = re.compile(r'\d+')
list_review_info = reg_number.findall(review_statement)
total_no_of_reviews = list_review_info[0]
reviews_per_page = list_review_info[1]


temp_url = re.sub(r'type=all','rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=',string)

for i in range(10,(total_no_of_reviews + 1),10):
    if i > total_no_of_reviews:
        break
    else:
        print(temp_url+str(i))
    
    


                           

pages = soup.find_all("span",{"class":"fk-navigation"})




function(str,count){
    pages = soup.find_all("span",{"class":"fk-navigation"})
    pages.get
