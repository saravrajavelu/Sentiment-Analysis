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



#Declare productReview class
class productReview:
    def __init__(self):
        self.userReviews = []
        self.userScores = []
        self.productFeatures = []
        self.featureScore = []
        self.featureOccurence = []
        self.count = 0
        self.featureDescribers = []

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

    def updateFeature(self,feature,score,describer):
        index = self.productFeatures.index(feature)
        self.featureDescribers[index].append(str(describer))
        self.featureScore[index] += score
        self.featureOccurence[index] += 1

    def addFeatures(self):
            noSpec = int(input('Enter no.of specifications : '))
            print (' Choose specifications : ')
            self.featureDescribers = [[] for i in range(noSpec)]
            for i in range(noSpec):
                feature = input()
                self.productFeatures.append(str(feature))
                self.featureOccurence.append(0)
                self.featureScore.append(0)

    def displaySummary(self):
            print('***************  Product Summary ***************')
            summary = ''
            for item in self.productFeatures:
                index = self.productFeatures.index(item)
                summary = summary + ' ' + str(item)  + ' was considered to be ' + str(max(set(self.featureDescribers[index]), key=self.featureDescribers[index].count)) + '.'
                if self.featureOccurence[index] == 0:
                    print(str(item),' : -NA- ')
                else:
                    totalScore = int(self.featureScore[index])/int(self.featureOccurence[index])
                    print(str(item),' : ',str(totalScore))
            print('Overview : ',summary)


#Initialize productReview class
reviewList = productReview()



exampleReview = """Have been Using this phone for more than a Week Now, must say I am very impressed with it.The processor is Super fast and the 2GB RAM makes sure, apps never Lag no matter what. The touch is one of the best in a smartphone. Android Kitkat is simply awesome, very smooth UI and Nexus will b always first to get the Updates, what more can you ask for?
The Display is FULL HD (445 ppi), the clarity is simply superb. The battery lasts about a Day with Moderate usage, but with heavy usage will last for about 12-15 Hours. All in all, you can't ask for a better phone under 30k. Did I also mention how light the phone is? It's so light that u don't even feel it in you hands! 
If your Budget is 30k, go get this phone, don't even think twice!"""

reviewList.addReview(exampleReview,5)

reviewList.addFeatures()

def processor(productReview):
    try:
        for exampleReview in productReview.userReviews:
            try:

                sentences = re.findall(r'(.*?)[\.|\?|!+]',exampleReview)
                '''sentences = re.findall(r'(.*?)[\.|\?|!+]',exampleReview)'''
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
                        if attr in productReview.productFeatures:
                             for adj_item  in adj_list:
                                 c.execute('SELECT value from wordVals where word=?',(adj_item.lower(),))
                                 query_result = c.fetchone()
                                 if query_result is None:
                                     pass
                                 else:
                                     productReview.updateFeature(attr , int(query_result[0]),adj_item)

                        else:
                            pass

            except Exception as e:
                print(str(e))
                print('Error - Processor - 2nd try')

        productReview.displaySummary()

    except Exception as e:
        print(str(e))
        print('Error - Processor - 1st Try')

processor(reviewList)
