import numpy as np
from skimage import draw, io, filters
from random import randint, uniform
import matplotlib.pyplot as plt

IMG_SZ = 28
OUT_DIR = './figures/'
UP_LIM = 8

# Sample principle color component
def principle_component():
	return round(uniform(0.6, 1.0),3)

# Sample secondary color component
def secondary_component():
	return round(uniform(0.0, 0.4),3)

# Converts index to color name
def strong_component_to_colorname(strong_component):
	if strong_component == 0:
		return 'red'
	elif strong_component == 1:
		return 'green'
	elif strong_component == 2:
		return 'blue'

# Samples a random nuance of red, green or blue
def get_random_color():
	red_component = secondary_component()
	green_component = secondary_component()
	blue_component = secondary_component()

	color = [secondary_component(), secondary_component(), secondary_component()]
	strong_component = randint(0, 2) # Whether red (0), green (1) or blue (2)
	color[strong_component] = principle_component()

	return strong_component, color	

# Generates a random image of a circle
def circle_image():
	image = np.zeros((IMG_SZ, IMG_SZ, 3), dtype = np.float32)
	min_radius = 4
	max_radius = IMG_SZ/2

	# Sample the radius
	radius = randint(min_radius, max_radius - UP_LIM)

	min_center = radius - 1
	max_center = IMG_SZ - radius

	# Sample the center of the circle
	center_row = randint(min_center, max_center)
	center_col = randint(min_center, max_center)

	rr, cc = draw.circle(center_row, center_col, radius)

	strong_component, color = get_random_color()

	image[rr, cc] = np.array(color)
	image = filters.gaussian(image, sigma = np.random.uniform(0.4,1.0))
	return strong_component, color, image

# Generates a random image of a square
def square_image():
	image = np.zeros((IMG_SZ, IMG_SZ, 3), dtype = np.float32)

	min_length = 4
	max_length = IMG_SZ

	# Sample length of square
	length = randint(min_length, max_length - UP_LIM)

	# Sample top-left point location (row + column)
	max_start = IMG_SZ - length
	top = randint(0, max_start)
	left = randint(0, max_start)

	bottom = top + length - 1
	right = left + length - 1

	r = np.array([top, top, bottom, bottom])
	c = np.array([left, right, right, left])
	rr, cc = draw.polygon(r, c)

	strong_component, color = get_random_color()

	image[rr, cc] = np.array(color)
	image = filters.gaussian(image, sigma = np.random.uniform(0.4,1.0))
	return strong_component, color, image

# Generates a random image of a triangle
def triangle_image():
	image = np.zeros((IMG_SZ, IMG_SZ, 3), dtype = np.float32)

	# Sample length of base edge
	min_edge = 6
	max_edge = IMG_SZ
	base_edge = randint(min_edge, max_edge - UP_LIM)

	# Sample length of height
	min_height = 6
	max_height = IMG_SZ/2
	height = randint(min_height, max_height - UP_LIM/2)

	# Sample starting point row
	min_start_r = height
	point1_r = randint(min_start_r, IMG_SZ - 1)

	# Sample starting point column
	max_start_c = IMG_SZ - base_edge
	point1_c = randint(0, max_start_c)

	projection = randint(4, base_edge)
	point2_r = point1_r - height + 1
	point2_c = point1_c + projection - 1

	point3_r = point1_r
	point3_c = point1_c + base_edge - 1

	r = np.array([point1_r, point2_r, point3_r])
	c = np.array([point1_c, point2_c, point3_c])
	rr, cc = draw.polygon(r, c)

	strong_component, color = get_random_color()

	image[rr, cc] = np.array(color)
	image = filters.gaussian(image, sigma = np.random.uniform(0.4,1.0))
	return strong_component, color, image

# Generate data
# Shape options: Circle, Square, Triangle
# Color options: Red, Green, Blue

index = 0

for i in range(1024):
	# Generate a circle
	strong_component, color, image = circle_image()
	colorname = strong_component_to_colorname(strong_component)
	print index, colorname, 'circle', 'exact color', color
	io.imsave(OUT_DIR + str(index) + '_circle_' + colorname + '.png', image)
	index += 1

	# Generate a square
	strong_component, color, image = square_image()
	colorname = strong_component_to_colorname(strong_component)
	print index, colorname, 'square', 'exact color', color
	io.imsave(OUT_DIR + str(index) + '_square_' + colorname + '.png', image)
	index += 1

	# Generate a triangle
	strong_component, color, image = triangle_image()
	colorname = strong_component_to_colorname(strong_component)
	print index, colorname, 'triangle', 'exact color', color
	io.imsave(OUT_DIR + str(index) + '_triangle_' + colorname + '.png', image)
	index += 1

	# Option to visualize generated figure
	#plt.figure(1, figsize = (10,8))
	#plt.imshow(image)
	#plt.show()