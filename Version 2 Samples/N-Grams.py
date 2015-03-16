import nltk
from nltk import bigrams


textlong = """Have been Using this phone for more than a Week Now, must say I am very impressed with it.The processor is Super fast and the 2GB RAM makes sure, apps never Lag no matter what. The touch is one of the best in a smartphone. Android Kitkat is simply awesome, very smooth UI and Nexus will b always first to get the Updates, what more can you ask for?
The Display is FULL HD (445 ppi), the clarity is simply superb. The battery lasts about a Day with Moderate usage, but with heavy usage will last for about 12-15 Hours. All in all, you can't ask for a better phone under 30k. Did I also mention how light the phone is? It's so light that u don't even feel it in you hands! 
If your Budget is 30k, go get this phone, don't even think twice!"""


'''
text = 'Not The screen is not very good not'
tokenized = nltk.word_tokenize(text)
print(list(nltk.ngrams(tokenized,5)))
'''





tokenized = nltk.word_tokenize(textlong.lower())
ngramList = list(nltk.ngrams(tokenized,5))
features = ['battery','processor','display']
for gram in ngramList:
    if '.' in gram:
        pass
    elif features[0] in gram:
        print(gram)
    elif features[1] in gram:
        print(gram)
    elif features[2] in gram:
        print(gram)

'''
tagged = nltk.pos_tag(tokenized)
print ('Before Tagged : ',tagged)
sentenceLength = len(tokenized)
for i in range(sentenceLength):
    if tokenized[i].lower() == 'not' :
        if i == 0:
            tokenized[i+1] = '!' + str(tokenized[i+1])
        elif i == sentenceLength-1:
            tokenized[i-1] = '!' + str(tokenized[i-1])
        else:
            tokenized[i-1] = '!' + str(tokenized[i-1])
            tokenized[i+1] = '!' + str(tokenized[i+1])


tagged = nltk.pos_tag(tokenized)
sent_tagged = nltk.pos_tag_sents(text)
namedEnt = nltk.ne_chunk(tagged, binary=True)



print ('Tokenized :',tokenized)
print ('After Tagged : ',tagged)
print ('Sentence Tagged : ',sent_tagged)
print ('Named Entity : ',namedEnt)
'''
