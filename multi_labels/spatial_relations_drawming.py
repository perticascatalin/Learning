from skimage import io, img_as_float
from drawing import principle_component, secondary_component
from random import randint

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

INPUT_DIR = '../figures/'
OUTPUT_DIR = '../relational_figures/'

filenames = [filename for filename in os.listdir(INPUT_DIR) if filename.endswith('.png')]

files_by_shape_color = {}

for filename in filenames:
	fig_id = id(filename)
	fig_shape = shape(filename)
	fig_color = color(filename)
	fig_filename = INPUT_DIR + filename
	if not files_by_shape_color.has_key(fig_shape + fig_color):
		files_by_shape_color[fig_shape + fig_color] = []
	files_by_shape_color[fig_shape + fig_color].append(fig_filename)

	#img = img_as_float(io.imread(fig_filename))
	#print img

for i in range(10):
	relation = randint(0,1)
	if relation == 0:
		# vertical
		conn_word = 'above'
	else:
		# horizontal
		conn_word = 'next to'
	print conn_word


#print filenames