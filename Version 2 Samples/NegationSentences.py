import nltk
text = 'Not The screen is not very good not'
tokenized = nltk.word_tokenize(text)
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

