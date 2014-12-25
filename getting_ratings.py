import sqlite3
import nltk
import time
import re

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

'''
def createDB():
    c.execute("")
'''

exampleReview = """Have been Using this phone for more than a Week Now, must say I am very impressed with it.The processor is Super fast and the 2GB RAM makes sure, apps never Lag no matter what. The touch is one of the best in a smartphone. Android Kitkat is simply awesome, very smooth UI and Nexus will b always first to get the Updates, what more can you ask for?
The Display is FULL HD (445 ppi), the clarity is simply superb. The battery lasts about a Day with Moderate usage, but with heavy usage will last for about 12-15 Hours. All in all, you can't ask for a better phone under 30k. Did I also mention how light the phone is? It's so light that u don't even feel it in you hands! 
If your Budget is 30k, go get this phone, don't even think twice!"""


#spec_list =['Brand','Handset Color','Form','Call Features','Touch Screen','SIM Type','Model ID','In the Box','Sound Enhancement','Video Player','Music Player','Secondary Camera','Other Camera Features','Primary Camera','Audio Jack','Preinstalled Browser','Bluetooth','Navigation Technology','NFC','Internet Features','Wifi','USB Connectivit','3G','Sensors','Phone Book Memory','Call Memory','SMS Memory','Important Apps','Additional Features','Warranty Summary','Weight','Size','Resolution','Other Display Features','Size','Talk Time','Standby Time','Type','Memory','Internal','Operating Freq','Graphics','OS','Processor']
spec_list =['Battery','Touch','Display','Budget','Price','Processor']
#print(spec_list)

def processor(data):
    try:
        tokenized = nltk.word_tokenize(data)
        tagged = nltk.pos_tag(tokenized)
        namedEnt = nltk.ne_chunk(tagged, binary=True)
        #print (namedEnt)
        #time.sleep(55)

        entities = re.findall(r'NE\s(.*?)/',str(namedEnt))
        descriptives_adj = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'',str(tagged))
        '''if len(entities) > 1:
            pass
        elif len(entities) == 0:
            pass
        else: '''
        print ('Sentence with POS-tagging : ')
        print (str(tagged))
        print ('-----------------------------------------------')
        print ('Named Entity of the Sentence : ',entities)
        print ('Descriptions : ')
        for desc in descriptives:
          print (desc)

 
    except Exception as e:
        print ('Failed in the first loop of processor')  
        print (str(e))

'''
sentences = re.findall(r'(.*?)[\.|\?|!+]',exampleReview)
for sent in sentences:
    print ('******************************************************')
    print ('******************************************************')
    print('The Sentence : ',sent)
    print ('-----------------------------------------------')
    processor(sent)    

'''

rating_for_spec_list = [0]*len(spec_list)
hits_for_spec_list = [0]*len(spec_list)

sentences = re.findall(r'(.*?)[\.|\?|!+]',exampleReview)
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
        if attr in spec_list:
             for adj_item  in adj_list:
                 c.execute('SELECT value from wordVals where word=?',(adj_item.lower(),))
                 query_result = c.fetchone()   
                 if query_result is None:
                     pass
                 else:
                     rating_for_spec_list[spec_list.index(attr)] += int(query_result[0])
                     hits_for_spec_list[spec_list.index(attr)] += 1
            
        else:
            pass

for spec in spec_list:
    if hits_for_spec_list[spec_list.index(spec)] == 0:
        print (spec + ' : NA ')
    else:
        temp_rating = rating_for_spec_list[spec_list.index(spec)]/hits_for_spec_list[spec_list.index(spec)]
        print (spec + ' :  ',temp_rating)
    
    '''
    print ('---------------------------------------------------------------------------------------------------------------------')
    print ('*** The Sentence : ***')
    print (sent)
    print ('*** POS-tagged Sentence : ***')
    print (str(tagged))
    print ('*** Named Entity : ***')
    for entity in entities:
        print(entity)
    print ('*** Nouns : ***')    
    for desc in descriptives_noun:
          print (desc)
    print ('*** Verbs : ***')    
    for desc in descriptives_verbs:
          print (desc)
    print ('*** Adjectives : ***')
    for desc in descriptives_adj:
          print (desc)
    print ('*** Adverbs : ***')
    for desc in descriptives_adverb:
          print (desc)  
    '''
