import helpers as help
from skimage import io, transform
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')
df_bbox = pd.read_csv('./input/challenge-2019-train-vrd-bbox.csv')

image_ids = [
	'00031197fb7b015d',
	'001156eb13f37194',
	'00114337b89792cc']

# 0. Objects in Image

def analyze_image(IMAGE_ID):
	rel_in_image = df_rel[df_rel.ImageID == IMAGE_ID]
	print (rel_in_image)

	for index, row in rel_in_image.iterrows():
	    subject = help.map_to_name(row['LabelName1'])
	    complement = help.map_to_name(row['LabelName2'])
	    relation = help.map_to_name(row['RelationshipLabel'])
	    print(subject, relation, complement)

	bbox_in_image = df_bbox[df_bbox.ImageID == IMAGE_ID]
	print bbox_in_image
	objects = bbox_in_image

	# 1. Show heat map for current bbox

	LIMIT = 10000
	num_objects = len(objects)
	print num_objects

	num_rows = 0
	step = max(num_objects / 10, 100)
	s = 10
	img = np.zeros((s,s), dtype = np.float64)
	for index, row in objects.iterrows():
		for r in range(s):
			for c in range(s):
				min_r = r / float(s)
				max_r = (r + 1) / float(s)
				min_c = c / float(s)
				max_c = (c + 1) / float(s)
				# hmin = 1.0 - row['YMax']
				# hmax = 1.0 - row['YMin']
				hmin = row['YMin']
				hmax = row['YMax']
				if row['XMin'] < max_c and row['XMax'] > min_c and hmin < max_r and hmax > min_r:
					img[r,c] += 1.0
		num_rows += 1
		if num_rows % step == 0:
			print 'step ', num_rows/step
		if num_rows > LIMIT:
			break

	for r in range(s):
		for c in range(s):
			img[r,c] = img[r,c] / num_objects

	print img

	sns.heatmap(img, cmap='RdYlGn_r', linewidths=0.5, annot=True)
	fig_name = IMAGE_ID + '_heatmap.png'
	plt.savefig(fig_name)
	plt.clf()

def show_image(IMAGE_ID):
	filename = './train/' + IMAGE_ID + '.jpg'
	img = io.imread(filename)
	plt.imshow(img)
	plt.show()
	plt.clf()

# 2. Resize images
def resize_image(IMAGE_ID):
	filename = './train/' + IMAGE_ID + '.jpg'
	img = io.imread(filename)

	print img.shape

	no_rows = img.shape[0]/4
	no_cols = img.shape[1]/4
	if no_rows % 32 != 0:
		no_rows = 32 * round(float(no_rows)/32)
	if no_cols % 32 != 0:
		no_cols = 32 * round(float(no_cols)/32)	

	res_img = transform.resize(img, (no_rows,no_cols,3))
	print res_img.shape

	res_filename = './train_resized/' + IMAGE_ID + '.jpg'
	io.imsave(res_filename, res_img)


for image_id in image_ids:
	#analyze_image(image_id)
	#show_image(image_id)
	resize_image(image_id)