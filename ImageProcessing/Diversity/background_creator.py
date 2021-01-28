# Input: 
# how_many_class_1 no_rows_class_1 no_cols_class_1 
# how_many_class_2 no_rows_class_2 no_cols_class_2
# ...
# Run: python background_creator.py <input>


import cv2
import sys
import math
import numpy as np

def get_next():
	global ind_arg
	ind_arg += 1
	return int(sys.argv[ind_arg])

def produce_image(how_many, no_rows, no_cols, border_len):

	mat_len = int(math.sqrt(how_many)) + 1

	# place mat_len * mat_len rectangles of no_rows * no_cols elements

	real_size_rows = mat_len * (no_rows + border_len)
	real_size_cols = mat_len * (no_cols + border_len)

	mat = np.zeros((real_size_rows, real_size_cols, 3), np.uint8)
	white = 255 * np.ones((no_rows, no_cols, 3), np.uint8)

	for lin in range(mat_len):
		for col in range(mat_len):
			start_row = lin * (no_rows + border_len)
			end_row = start_row + no_rows + border_len

			start_col = col * (no_cols + border_len)
			end_col = start_col + no_cols + border_len
			
			mat[start_row + border_len: end_row, start_col + border_len:end_col] = white.copy()

	return mat

def concatenate_horizontally(image1, image2):
	no_rows_1 = image1.shape[0]
	no_rows_2 = image2.shape[0]
	if no_rows_1 > no_rows_2:
		image2 = cv2.copyMakeBorder(image2, 0, no_rows_1 - no_rows_2, 0, 0, cv2.BORDER_CONSTANT,value = 0)
	elif no_rows_2 > no_rows_1:
		image1 = cv2.copyMakeBorder(image1, 0, no_rows_2 - no_rows_1, 0, 0, cv2.BORDER_CONSTANT,value = 0)

	res = np.append(image1, image2, axis = 1)
	return res

def occupy(image):
	global factory
	factory = concatenate_horizontally(factory, image)

no_categ = (len(sys.argv) - 1)/3

#print no_categ

ind_arg = 0
border_len = 3
factory = np.zeros((1,1,3), np.uint8)

for i in range(no_categ):
	how_many = get_next()
	no_rows = get_next()
	no_cols = get_next()
	occupy(produce_image(how_many, no_rows, no_cols, border_len))

#cv2.imshow('The Factory', factory)
#cv2.waitKey()

factory[0,0] = (0,0,255)
cv2.imwrite('groundback.jpg', factory)

