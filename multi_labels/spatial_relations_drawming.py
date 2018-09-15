from skimage import io, img_as_float
from drawing import principle_component, secondary_component
from random import randint

import matplotlib.pyplot as plt
import numpy as np
import os

IMG_SZ = 28

def id(filename):
	return filename.split('.')[0].split('_')[0]

def shape(filename):
	return filename.split('.')[0].split('_')[1]

def color(filename):
	return filename.split('.')[0].split('_')[2]

def blank_image():
	img = np.zeros((IMG_SZ, IMG_SZ, 3), dtype = float)
	for row in range(IMG_SZ):
		for col in range(IMG_SZ):
			make_noise = randint(0,9)
			if make_noise == 0:
				img[row, col] = [secondary_component(), secondary_component(), secondary_component()]
	return img

INPUT_DIR = '../figures/'
OUTPUT_DIR = '../relational_figures/'

filenames = [filename for filename in os.listdir(INPUT_DIR) if filename.endswith('.png')]

files_by_color_shape = {}

for filename in filenames:
	fig_id = id(filename)
	fig_shape = shape(filename)
	fig_color = color(filename)
	fig_filename = INPUT_DIR + filename
	if not files_by_color_shape.has_key(fig_color + ' ' + fig_shape):
		files_by_color_shape[fig_color + ' ' + fig_shape] = []
	files_by_color_shape[fig_color + ' ' + fig_shape].append(fig_filename)

	#img = img_as_float(io.imread(fig_filename))
	#print img

for i in range(100,200):
	relation = randint(0,1)
	if relation == 0:
		# vertical
		conn_word = 'above'
	else:
		# horizontal
		conn_word = 'next_to'

	# 0 - circle, 1 - square, 2 - triangle
	shape_id_2_name = {0 : 'circle', 1 : 'square', 2 : 'triangle'}
	first_shape = randint(0,2)
	second_shape = randint(0,2)

	# 0 - red, 1 - green, 2 - blue
	color_id_2_name = {0 : 'red', 1 : 'green', 2 : 'blue'}
	first_color = randint(0,2)
	second_color = randint(0,2)

	first_figure = color_id_2_name[first_color] + ' ' + shape_id_2_name[first_shape]
	second_figure = color_id_2_name[second_color] + ' ' + shape_id_2_name[second_shape]
	figure_type = first_figure + ' ' + conn_word + ' ' + second_figure
	print figure_type

	# How many figures available for a type
	first_count = len(files_by_color_shape[first_figure])
	second_count = len(files_by_color_shape[second_figure])

	# Sample a figure from the available ones
	first_id = randint(0, first_count-1)
	second_id = randint(0, second_count-1)
	first_img = img_as_float(io.imread(files_by_color_shape[first_figure][first_id]))
	second_img = img_as_float(io.imread(files_by_color_shape[second_figure][second_id]))

	side = randint(0,1)
	if side == 0:
		if conn_word == 'above':
			'''
			1#
			2#
			'''
			up_img = np.concatenate((first_img, blank_image()), axis = 1)
			down_img = np.concatenate((second_img, blank_image()), axis = 1)
			whole_img = np.concatenate((up_img, down_img), axis = 0)
		elif conn_word == 'next_to':
			'''
			12
			##
			'''
			up_img = np.concatenate((first_img, second_img), axis = 1)
			down_img = np.concatenate((blank_image(), blank_image()), axis = 1)
			whole_img = np.concatenate((up_img, down_img), axis = 0)
	else:
		if conn_word == 'above':
			'''
			#1
			#2
			'''
			up_img = np.concatenate((blank_image(), first_img), axis = 1)
			down_img = np.concatenate((blank_image(), second_img), axis = 1)
			whole_img = np.concatenate((up_img, down_img), axis = 0)
		elif conn_word == 'next_to':
			'''
			##
			12
			'''
			up_img = np.concatenate((blank_image(), blank_image()), axis = 1)
			down_img = np.concatenate((first_img, second_img), axis = 1)
			whole_img = np.concatenate((up_img, down_img), axis = 0)
	# Option to visualize generated figure
	# plt.figure(1, figsize = (10,8))
	# plt.imshow(whole_img)
	# plt.show()
	io.imsave(OUTPUT_DIR + str(i) + ' ' + figure_type + '.png', whole_img)

#print filenames