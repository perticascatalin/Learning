import helpers as help
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

# 2. General object (eg. Chair)

objects = ["Chair", "Car", "Man", "Woman"]

for object_name in objects:
	label_name = help.map_to_tag(object_name)
	print label_name
	objects = df_bbox[df_bbox.LabelName == label_name]

	print objects.sample(5)

	# Distribution of locations and size for objects of given type (eg. Chair)

	numerical = ['XMin', 'XMax', 'YMin', 'YMax', 'dX', 'dY', 'dYdX']
	fig_name = './loc_size/' + object_name + '_loc_size.png'
	objects[numerical].hist(bins=15, figsize=(20, 10), layout=(2, 4))
	plt.savefig(fig_name)
	print objects['ImageID'].value_counts()
