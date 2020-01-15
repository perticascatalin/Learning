class Work:
	def __init__(self, name, time = 0, rate = 0, frame = False, adjustment = 1.0):
		self.name = name
		# self.tricks = []    # creates a new empty list for each dog
		self.time = time
		self.rate = rate
		self.frame = frame
		self.adjustment = adjustment

	# def add_trick(self, trick):
	# 	self.tricks.append(trick)

	def price(self):
		val = self.time * self.rate * self.adjustment + (30 if self.frame else 0)
		return val

	def gain(self):
		val = self.time * self.rate + (30 if self.frame else 0)
		return val

print ("Hello AW!")

# Rate 30
a = Work('Michelangelo\'s Dream', 26, 30, False, 1.54)
b = Work('Energy Transform Hand', 18, 30, False, 1.54)
c = Work('Universal Shaman', 50, 30, True, 1.54)
d = Work('Divide et Impera', 40, 30, True, 1.54)
e = Work('Mind Zoom-In', 30, 30, True, 1.54)
f = Work('Cranium Universalis', 40, 30, True, 1.54)
i = Work('Afterlife & Creation',16, 30, False, 1.54)
j = Work('Death',10,30,True, 1.54)

# Rate 10
g = Work('Notebook 2019', 36, 10, False, 1.54)
l = Work('Euler', 6, 10, False, 1.54)

# Rate 20
h = Work('Tineretea', 20, 20, True, 1.54)
k = Work('Meteor Collide', 2, 20, False, 1.54)

works = [a,b,c,d,e,f,g,h,i,j,k,l]

works.sort(key=lambda x: x.gain(), reverse = True)

total_sum = 0

for work in works:
	print work.name, work.gain(), '/', work.price()
	# print work.price()
	# print work.gain()
	total_sum += work.gain()

print '==========================='
print 'Total Sum:', total_sum
print 'Number of Works:', len(works)

# d = Work('Fido')
# e = Work('Buddy')

# d.add_trick('roll over')
# e.add_trick('play dead')

# print d.tricks
# print e.tricks

