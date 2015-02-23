class productReview:
	def __init__(self):
		self.userReviews = []
		self.userScores = []
		self.length = 0
	def addReview(self,review,score):
		self.userReviews.append(str(review))
		self.userScores.append(str(review))
		self.length += 1
	def displayList(self,limit=-1):
		if limit == -1:
			span = self.length
		else:
			span = limit
		for itemno in range(span):
			print('----------------------------------------------------')
			print('User Score : ',self.userScores[itemno])
			print('User Review : ')
			print(self.userReviews[itemno])
