from random import shuffle


partOne = ['While ','Whereas ','Although, ','Nevertheless, ','Nonetheless, ','Yet ','At the same time, ']
partTwoNeutral = ['people ','customers ','purchasers ','shoppers ','buyers ','consumers ','reviewers ']
partTwoPositive = ['advocates ','patrons ','backers ','exponents ','endosers ']
partTwoNegative = ['opposers ','critics ']
partThreeNeutral = ['found ','felt ','feel ','deduces ','consider ','recognizes ','surmise ','infer that ','conceive that ','believe that ','perceive that ']
partThreePositive = ['appreciate  ','agree that ','recoginzed ','certify ']
partThreeNegative = ['criticize ','depreciate ','castigate ','condemn ','decry ','rebuke ','censure ','undervalue']
partFour = ['it\'s ','the product\'s ','the ']
#partFive = ['<<!f!>>']
partFive = ['processor']
partSix = ['was ','was considered ','was found to be ']
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
shuffle(partSix)
shuffle(partSeven)

print(partOne[0],partTwoNeutral[0],partThreeNeutral[0],partFour[0],partFive[0],partSix[0],partSeven[0],'.')
