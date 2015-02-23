import nltk
import re
import time

exampleArray = ['''i have being using this phone for a month now.. and i must say i just love it..
it can process anything in not in a second but in millisecond

screen is awesome, with a very crisp display with 441ppi
with adreno 330 gpu the gaming experience is top class..

with the barometer support phone gives the location accurate by a metre and makes navigation easy.

charging time is good, it can get fully charged in about 2 hours using standard travel charger, never tried wireless charging though

and the headphones are pretty good and can hear it clearly even during travelling in a bus or train.. the loudspeakers are also loud enough with about 68db

WiFi signal locking on pretty good, it can catch on the signal at 30-40 ft from router.
the tethering speed on all modes (USB,WiFi,Bluetooth) is pretty fast

if any calls from unknown number is received it shows the location of number searching from Google instantaneously..at-least you can guess who it might be..that is a pretty nice feature.. don't know if it is available in other phones

slimport support is far more better than MHL. you dont need an additional power cable like in the case of MHL.. you just need to plug in an go..

google voice search is correct most of the time and i am enjoying this feature..

only downside is the battery. it last only for about 12 hours. it is mainly due to powerfull screen..
camera options are less.nevertheless you can download the camera app from google play store

thats it for now. will let you know more later..''']


exampleArray = ['''Sarthak is faggy pussy. Lick lick Rohit.''']

for item in exampleArray:
    tokenized = nltk.word_tokenize(item)
    #print (tokenized)
    tagged = nltk.pos_tag(tokenized)
    print (tagged)

    chunkGram = r"""
Chunk:
{<NN\w?>}
"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print (chunked)
    chunked.draw()

    time.sleep(555)

#}<RB|NNS>{
#{<RB\w?>*<VB\w?>*<NNP>}
