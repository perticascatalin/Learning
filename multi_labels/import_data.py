import tensorflow as tf
import os

# https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/5_DataManagement/build_an_image_dataset.py

shape_to_index = {}
shape_to_index['circle'] = 0
shape_to_index['square'] = 1
shape_to_index['triangle'] = 2

color_to_index = {}
color_to_index['red'] = 0
color_to_index['green'] = 1
color_to_index['blue'] = 2

# Import data - 4 options: 
# - shape
# - color
# - multi_label: shape + color
# - combo: shape x color
def read_images(input_directory, batch_size, img_height, img_width, mode = 'multi_label'):

	file_names = [file_name for file_name in os.listdir(input_directory) if file_name.endswith('.png')]
	image_paths, labels = list(), list()
	for file_name in file_names:
		#print (file_name)

		file_props = file_name.split('.')[0].split('_')
		#print ('File props', file_props)

		img_id = int(file_props[0])
		img_shape = file_props[1]
		img_color = file_props[2]
		#print (img_id, img_shape, img_color)

		image_paths.append(input_directory + file_name)
		shape_label = shape_to_index[img_shape] # 0, 1 or 2
		color_label = color_to_index[img_color] # 0, 1 or 2

		if mode == 'multi_label':
			labels.append([shape_label, color_label])
		elif mode == 'shape':
			labels.append(shape_label)
		elif mode == 'color':
			labels.append(color_label)
		elif mode == 'combo':
			labels.append(shape_label * 3 + color_label)

	image_paths = tf.convert_to_tensor(image_paths, dtype = tf.string)
	labels = tf.convert_to_tensor(labels, dtype = tf.int32)
	#print image_paths, labels

	image, label = tf.train.slice_input_producer([image_paths, labels], shuffle = True)

	image = tf.read_file(image)
	image = tf.image.decode_png(image, channels = 3)
	image = tf.image.resize_images(image, [img_height, img_width])

	X, Y = tf.train.batch([image, label], batch_size = batch_size, capacity = batch_size * 8, num_threads = 4)
	return X, Y