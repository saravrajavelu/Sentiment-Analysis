import nltk
import re
import time

exampleReview = """Have been Using this phone for more than a Week Now, must say I am very impressed with it.The processor is Super fast and the 2GB RAM makes sure, apps never Lag no matter what. The touch is one of the best in a smartphone. Android Kitkat is simply awesome, very smooth UI and Nexus will b always first to get the Updates, what more can you ask for?
The Display is FULL HD (445 ppi), the clarity is simply superb. The battery lasts about a Day with Moderate usage, but with heavy usage will last for about 12-15 Hours. All in all, you can't ask for a better phone under 30k. Did I also mention how light the phone is? It's so light that u don't even feel it in you hands! 
If your Budget is 30k, go get this phone, don't even think twice!"""

def processLanguage():
    try:
        tokenized = nltk.word_tokenize(exampleReview)
        tagged = nltk.pos_tag(tokenized)
        #print(tagged)
        namedEnt = nltk.ne_chunk(tagged)
        namedEnt.draw()

    

        
        #chunkGram = r""" Chunk: {<NNP?>*}                 """
        '''  chunkGram = r"""
    Chunk:
        {<.*>}
        }<RB|NNS>{
        """
        '''


        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)

        print(chunked)
        #chunked.draw()
        

        time.sleep(1)
            




    except Exception as e:
        print (str(e))


processLanguage()
