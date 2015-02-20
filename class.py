class productReview:
	def __init__():
		userReviews = []
		userScores = []
		length = 0
	def addReview(review,score):
		userReviews.append(str(review))
		userScores.append(str(review))
		length += 1
	def displayList(limit=-1):
		if limit == -1:
			span = length
		else:
			span = limit
		for itemno in range(span):
			print('----------------------------------------------------')
			print('User Score : ',userScores[itemno])
			print('User Review : ')
			print(userReviews[itemno])
