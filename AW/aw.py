class Work:
	def __init__(self, name, time = 0, rate = 0, frame = False, adjustment = 1.0):
		self.name = name
		self.time = time
		self.rate = rate
		self.frame = frame
		self.adjustment = adjustment

	def price(self):
		val = self.time * self.rate * self.adjustment + (30 if self.frame else 0)
		return val

	def gain(self):
		val = self.time * self.rate + (30 if self.frame else 0)
		return val

# Alternative idea: split into p_rate: 32, g_rate: 24, s_rate: 16, b_rate: 8

print ("Hello AW!")
print '==========================='

g_rate = 30
s_rate = 20
b_rate = 10
tax_adj = 1.54

# Gold Rate
c = Work('Universal Shaman', 50, g_rate, True, tax_adj)
f = Work('Cranium Universalis', 40, g_rate, True, tax_adj)
d = Work('Divide et Impera', 40, g_rate, True, tax_adj)
e = Work('Mind Zoom-In', 30, g_rate, True, tax_adj)
a = Work('Michelangelo\'s Dream', 26, g_rate, False, tax_adj)
r = Work('Althea', 20, g_rate, True, tax_adj)
i = Work('Afterlife & Creation',16, g_rate, False, tax_adj)
m = Work('Octopus', 12, g_rate, False, tax_adj)
j = Work('Death', 10, g_rate, True, tax_adj)
s = Work('Still Mona', 6, g_rate, False, tax_adj)

# Silver Rate
x = Work('Entailed Coincidences', 20, s_rate, True, tax_adj)
h = Work('Tineretea', 20, s_rate, True, tax_adj)
b = Work('Energy Transform Hand', 18, s_rate, False, tax_adj)
n = Work('The Room', 12, s_rate, False, tax_adj)
o = Work('Gamma Particle 31', 10, s_rate, False, tax_adj)
a1 = Work('Kol Blast', 10, s_rate, False, tax_adj)
y = Work('Banknote 100 pieces', 10, s_rate, False, tax_adj)
q = Work('Fire Angel', 8, s_rate, False, tax_adj)
z = Work('King', 6, s_rate, False, tax_adj)
k = Work('Meteor Collide', 2, s_rate, False, tax_adj)
u = Work('Surreal Rat Horse', 2, s_rate, False, tax_adj)
v = Work('Surreal Cat Shaman', 2, s_rate, False, tax_adj)
w = Work('Shaman-Portrait', 2, s_rate, False, tax_adj)

# Bronze Rate
g = Work('Notebook 2019', 36, b_rate, False, tax_adj)
l = Work('Euler', 6, b_rate, False, tax_adj)
p = Work('Smile', 6, b_rate, False, tax_adj)
t = Work('Flying Cat-Dog', 4, b_rate, False, tax_adj)

works = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,y,x,z,a1]

works.sort(key=lambda x: x.gain(), reverse = True)

total_sum = 0
total_time = 0

for work in works:
	print work.name, work.gain(), '/', work.price()
	total_sum += work.gain()
	total_time += work.time

print '==========================='
print 'Total Sum:', total_sum
print 'Total Time', total_time
print 'Number of Works:', len(works)