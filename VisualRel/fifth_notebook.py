from skimage import io, transform
import tensorflow as tf
import helpers as help
import pdb
import os
import random

# 6. Process grid cell image

# 6.A Process grid cell classes
def process_grid_cell(filename):
	# do not forget to read as dirname + filename
	splits = filename.split('.')[0].split('_')
	splits = splits[:-1] # ignore "cell"
	image_id = splits[0]
	row = splits[1]
	col = splits[2]
	Y = [0] * 58 # num classes
	if splits[3] == '':
		print 'nada'
		#Y[0] = 1 # (just leave 0's for all in this case)
		# cell class will be 0
	else:
		for i in range(3, len(splits)):
			print '+', splits[i]
			class_label = int(splits[i])
			Y[class_label] = 1
			# compute uniques of ints
	return Y

# 6.B Process all grid cells
def read_images(input_directory, batch_size, limit_background = False):
	file_names = [file_name for file_name in os.listdir(input_directory) if file_name.endswith('.png')]
	image_paths, labels = list(), list()
	skipped = 0
	taken = 0
	for file_name in file_names:
		print (file_name)
		label = process_grid_cell(file_name)
		image_path = input_directory + file_name

		# 6.C Limit background class to 1 out of 10
		if limit_background:
			all_zeros = True
			for dig in label:
				if dig == 1:
					all_zeros = False
			#rnd = random.randint(0,10) # 1 out of 10 => 20-25% bckg
			rnd = random.randint(0,30) # 1 out of 30 => 7-8% bckg
			if all_zeros and rnd != 0:
				# do nothing
				skipped += 1
			else:
				labels.append(label)
				image_paths.append(image_path)
				if all_zeros:
					taken += 1
		else:
			labels.append(label)
			image_paths.append(image_path)

	print "Skipped ", skipped, " background cells"
	print "Took ", taken, " background cells"
	image_paths = tf.convert_to_tensor(image_paths, dtype = tf.string)
	labels = tf.convert_to_tensor(labels, dtype = tf.int32)
	#print image_paths, labels

	image, label = tf.train.slice_input_producer([image_paths, labels], shuffle = True)

	image = tf.read_file(image)
	image = tf.image.decode_png(image, channels = 3)
	image = tf.image.resize_images(image, [32, 32])

	X, Y = tf.train.batch([image, label], batch_size = batch_size, capacity = batch_size * 8, num_threads = 4)
	return X, Y


# dirname = './eye_grid_cells/'
# f1 = '001156eb13f37194_2_5_49_cell.png' # car
# f2 = '0007ad5c6245a41d_1_6_27_cell.png' # man
# f3 = '00031197fb7b015d_2_0_11_11_cell.png' # 2 chairs
# f4 = '00031197fb7b015d_0_2__cell.png' # nothing
# f5 = '00031197fb7b015d_2_3_11_11_37_cell.png' # 2 chairs and a table

#process_grid_cell(f5)
# read_images(dirname, 64)