import helpers as help
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')
df_bbox = pd.read_csv('./input/challenge-2019-train-vrd-bbox.csv')

IMAGE_ID = '00031197fb7b015d'

# 1. Bounding boxes in Image

rel_in_image = df_rel[df_rel.ImageID == IMAGE_ID]
print (rel_in_image)

for index, row in rel_in_image.iterrows():
    subject = help.map_to_name(row['LabelName1'])
    complement = help.map_to_name(row['LabelName2'])
    relation = help.map_to_name(row['RelationshipLabel'])
    print(subject, relation, complement)

print df_bbox.sample(5)

bbox_in_image = df_bbox[df_bbox.ImageID == IMAGE_ID]
print bbox_in_image

# 3. Compute dX, dY
df_bbox['dX'] = df_bbox['XMax'] - df_bbox['XMin']
df_bbox['dY'] = df_bbox['YMax'] - df_bbox['YMin']

# 4. Compute pseudo-ratio
df_bbox['dYdX'] = df_bbox['dY'] / (df_bbox['dX'] + 0.1)
df_bbox['dXdY'] = df_bbox['dX'] / (df_bbox['dY'] + 0.1)

# 2. General object (eg. Chair)

#objects = ["Chair", "Car", "Woman", "Man"]
#objects = ["Microwave oven", "Ski", "Racket", "Tennis ball"]
#objects = ["Piano", "Beer", "Chopsticks", "Cat"]

LIMIT = 10000
for object_name in objects:
	label_name = help.map_to_tag(object_name)
	print label_name
	objects = df_bbox[df_bbox.LabelName == label_name]

	print objects.sample(5)

	# Distribution of locations and size for objects of given type (eg. Chair)

	numerical = ['XMin', 'XMax', 'YMin', 'YMax', 'dX', 'dY', 'dYdX', 'dXdY']
	fig_name = './loc_size/' + object_name.replace(" ", "_") + '_loc_size.png'
	objects[numerical].hist(bins=15, figsize=(20, 10), layout=(2, 4))
	plt.savefig(fig_name)
	plt.clf()
	print object_name
	# how many times it appears per image
	#print objects['ImageID'].value_counts()
	# how many times it appears overall
	num_objects = len(objects)
	print num_objects

	# 5. Iterate rows:
	# 8. No not iterate more than LIMIT (200.000 rows)
	# (for more efficiency in heatmap generation)
	num_rows = 0
	step = min(num_objects, LIMIT) / 10
	step = max(step, 100)
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


	# 6. Divide by total number:
	for r in range(s):
		for c in range(s):
			img[r,c] = img[r,c] / num_objects

	print img

	# 7. Heat Map for object localization
	sns.heatmap(img, cmap='RdYlGn_r', linewidths=0.5, annot=True)
	fig_name = './heatmaps/' + object_name.replace(" ", "_") + '_heatmap.png'
	plt.savefig(fig_name)
	plt.clf()

# 7. Heat Map
# x = np.random.randn(5,4)
# sns.heatmap(x, cmap='RdYlGn_r', linewidths=0.5, annot=True)
# plt.savefig('./heatmap.png')
# plt.clf()
