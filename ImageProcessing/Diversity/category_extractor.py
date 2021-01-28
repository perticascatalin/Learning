# Input: 
# what image to extract categories from
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

	mat = np.zeros((real_size_rows, real_size_cols), np.uint8)
	white = 255 * np.ones((no_rows, no_cols), np.uint8)

	for lin in range(mat_len):
		for col in range(mat_len):
			start_row = lin * (no_rows + border_len)
			end_row = start_row + no_rows + border_len

			start_col = col * (no_cols + border_len)
			end_col = start_col + no_cols + border_len
			
			mat[start_row + border_len: end_row, start_col + border_len:end_col] = white.copy()

	return mat

def extract_next_category(image1, image2, samples):
	no_rows_1 = image1.shape[0]
	no_rows_2 = image2.shape[0]


	if no_rows_1 > no_rows_2:
		image2 = cv2.copyMakeBorder(image2, 0, no_rows_1 - no_rows_2, 0, 0, cv2.BORDER_CONSTANT,value = 0)
	elif no_rows_2 > no_rows_1:
		image1 = cv2.copyMakeBorder(image1, 0, no_rows_2 - no_rows_1, 0, 0, cv2.BORDER_CONSTANT,value = 0)

	res = np.append(image1, image2, axis = 1)

	no_rows = image1.shape[0]
	no_cols = image1.shape[1]
	
	add_rows = image2.shape[0]
	add_cols = image2.shape[1]

	# need to create mask
	mask = 255 * np.ones((add_rows, add_cols), np.uint8)
	mask = mask - image2
	mask = cv2.copyMakeBorder(mask, 0, 2, 0, 2, cv2.BORDER_CONSTANT, value = 255)

	no_samples = 0

	wanted_samples = samples[:,no_cols:no_cols + add_cols].copy()	

	category = []

	for row in range(add_rows):
		for col in range(add_cols):
			if mask[row, col] == 0:
				no_samples += 1
				ret, (cl, lin, d_cl, d_lin) = cv2.floodFill(wanted_samples, mask, (col, row), (no_samples,0,0), (255,255,255), (255,255,255))
				sample = samples[lin : lin+d_lin, no_cols+cl : no_cols+cl+d_cl]
				category.append(sample)

	return res, category

def retrieve(image, samples):
	global factory
	factory, category = extract_next_category(factory, image, samples)
	# category is a list of images belonging to it
	return category

samples_location = sys.argv[1]
samples = cv2.imread(samples_location)

no_categ = (len(sys.argv) - 2)/3

#print no_categ

ind_arg = 1
border_len = 3
factory = np.zeros((1,1), np.uint8)

for i in range(no_categ):
	how_many = get_next()
	no_rows = get_next()
	no_cols = get_next()
	category = retrieve(produce_image(how_many, no_rows, no_cols, border_len), samples)
	for j in range(len(category)):
		f_name = str(i) + str(j) + '.jpg'
		cv2.imwrite(f_name, category[j])


