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
print (word_list[0])

'''
def main(word,rating):
    try:
        





    except Exception as e:
        print (str(e))
        print ('Failed in first try')

'''

for words in word_list:
    print (words)
