import numpy as np
import pdb

def to_one_hot(arr, n):
	one_hot = []
	for item in arr:
		one_hot_item = np.zeros((n,), dtype = int)
		one_hot_item[item] = 1
		one_hot.append(one_hot_item)
	return np.array(one_hot)

def from_one_hot(arr):
	categ = []
	for item in arr:
		categ.append(np.argmax(item))
	return np.array(categ)

pred = np.array([0, 1, 2, 3, 4])
gt = np.array([8, 1, 2, 8, 4])

print pred
print gt

#pdb.set_trace()

print pred == gt
print np.sum(pred == gt)

one_hot = to_one_hot(pred, 10)
categ =  from_one_hot(one_hot)

print one_hot
print categ