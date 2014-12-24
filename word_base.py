import re
import requests
import sqlite3
import nltk
import time
from bs4 import BeautifulSoup

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()
c.execute('SELECT * from wordVals')
word_list = c.fetchall()
#print (word_list[0])


def main(word,rating):
    try:
        url = 'http://www.thesaurus.com/browse/' + str(word) + '?s=t'
        req = requests.get(url)
        soup = BeautifulSoup(req.content)
        temp = soup.find_all("div",{"class":"heading-block oneClick-disabled"})
        no_of_syn = re.findall(r'<strong>(.*)</strong>',str(temp[0]))
        no_of_syn = int(no_of_syn[0])
        relevant_list = soup.find_all("span",{"class":"text"},limit = no_of_syn)
        for list_item in relevant_list:
            c.execute('SELECT * from wordVals WHERE word=?',(list_item.string,))
            check_fetch = c.fetchone()
            if check_fetch is None:
                c.execute('INSERT into wordVals values (?,?)',(list_item.string,rating))
            else:
                new_rating = int(rating) + int(check_fetch[1])
                c.execute('UPDATE wordVals SET value=? WHERE word=?',(new_rating,check_fetch[0]))
            
            
        
        





    except Exception as e:
        print (str(e))
        print ('Failed in first try')



for words in word_list:
    temp_word = str(words[0])
    c.execute('SELECT * from doneWords WHERE word=?',(temp_word,))
    check_fetch = c.fetchone()
    if check_fetch is None:
        print ('Getting new words')
        main(words[0],words[1])
        c.execute('INSERT into doneWords values (?)',(temp_word,))
    else: 
        print ('Already have this word')



conn.commit()
