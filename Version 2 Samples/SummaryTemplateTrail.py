from random import shuffle


features = ['display','battery','processor','sound','storage','price']
scores = [1,7,9,3,5,'?']
words = ['unclear','great','fast','clear','enough']

def SummaryTemplate(features,scores,words):
    partOne = ['While ','Whereas ','Although, ','Nevertheless, ','Nonetheless, ','Yet ','At the same time, ']
    partTwoNeutral = ['people ','customers ','purchasers ','shoppers ','buyers ','consumers ','reviewers ']
    partTwoPositive = ['advocates ','patrons ','backers ','exponents ','endosers ']
    partTwoNegative = ['opposers ','critics ','opposers ','critics ','opposers ','critics ']
    partThreeNeutral = ['found ','felt ','deduced ','considered ','recognized ','surmised that','infered that ','believed that ','perceived that ']
    partThreePositive = ['appreciated  ','agreed that ','recoginzed ','certified ','applauded ','commended ','praised ','lauded ','endosered ','extolled ','raved about ']
    partThreeNegative = ['criticized ','depreciated ','decried  ','rebuked ','censured ','undervalued ']
    partFour = ['it\'s ','the product\'s ','the ','it\'s ','the product\'s ','the ']
    #partFive = ['<<!f!>>']
    partFive = ['processor']
    partSix = ['was ','to be ']
    #partSeven = ['<<!e!>>']
    partSeven = ['fast']

    shuffle(partOne)
    shuffle(partTwoNeutral)
    shuffle(partTwoPositive)
    shuffle(partTwoNegative)
    shuffle(partThreeNeutral)
    shuffle(partThreePositive)
    shuffle(partThreeNegative)
    shuffle(partFour)
    shuffle(partFive)
    #shuffle(partSix)
    shuffle(partSeven)

    i1 = 0
    i2Neu = 0
    i2Pos = 0
    i2Neg = 0
    i3Neu = 0
    i3Pos = 0
    i3Neg = 0
    i4 = 0
    i5 = 0
    #i6 = 0
    i7 = 0
    regretCount = scores.count('?')
    regretLine = ''
    summaryReport = ''
    for i in range(6):
        #print(regretCount,' < ',scores.count('?'), ' && ',regretCount,' > 1')
        if scores[i] == '?':
            if regretLine == '':
                regretLine = str(features[i])
                regretCount -=1
            elif (regretCount < scores.count('?')) & (regretCount > 1):
                regretLine = regretLine + ", " + str(features[i])
                regretCount -=1
            else:
                regretLine = regretLine + " and " + str(features[i])
            
        elif partTwoNeutral[i2] in ['found ','considered ','recognized ',]:
            print(partOne[i1],partTwoNeutral[i2],partThreeNeutral[i3],partFour[i4],partFive[i5],partSix[1],partSeven[i7],'.')
            i1 += 1
            i2 += 1
            i3 += 1
            i4 += 1
        else:
            print(partOne[i1],partTwoNeutral[i2],partThreeNeutral[i3],partFour[i4],partFive[i5],partSix[0],partSeven[i7],'.')
            i1 += 1
            i2 += 1
            i3 += 1
            i4 += 1
    if len(features) == scores.count('?'):
        regretLine = regretLine.capitalize() + ' were not mentioned by customers in their reviews.'
    else
        regretLine = 'However ' + regretLine +  ' were not mentioned by customers in their reviews.'
    print(regretLine)

SummaryTemplate(features,scores,words)
