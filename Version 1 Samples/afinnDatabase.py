from PIL.WmfImagePlugin import word

__author__ = 'sarav rajavelu'
import sqlite3
import re

conn = sqlite3.connect('wordBase.db')
c = conn.cursor()


def createDB():
    c.execute("DROP TABLE IF EXISTS wordVals")
    c.execute("CREATE TABLE wordVals (word TEXT, value REAL)")


createDB()


file = open("AFINN-111.txt","r")
matchedRegex = re.findall(r'(.*)',file.read())
for item in matchedRegex:
    if len(item) == 0:
        pass
    else:
        tempSplit = item.split("\t",2)
        word = str(tempSplit[0])
        value = int(tempSplit[1])+5
        c.execute('INSERT into wordVals values (?,?)',(word,value))

conn.commit()
