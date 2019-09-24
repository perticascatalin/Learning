from skimage import io
import matplotlib.pyplot as plt
import helpers as help
import pandas as pd
import os

# Write number relations per image available and total
def stats_img_avail():
	num_images = 0
	num_images_w_rel = 0
	total_relations = 0
	for dirname, _, filenames in os.walk('./train'):
	    for filename in filenames:
	        # print(filename)
	        image_id = filename.split('.')[0]
	        num_images += 1
	        rel_in_image = df_rel[df_rel.ImageID == image_id]
	        total_relations += len(rel_in_image)
	        if len(rel_in_image) > 0:
	            print (image_id, len(rel_in_image))
	            num_images_w_rel += 1

	print ('Total relations:', total_relations)
	print ('Images with relations:', num_images_w_rel)
	print ('Total images:', num_images)

def show_image(image_id):
	filename = './train/' + image_id + '.jpg'
	img = io.imread(filename)
	plt.imshow(img)
	plt.show()

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')

IMAGE_ID = '0000c33c6f4b8518'
IMAGE_ID = '0000bee39176697a'
IMAGE_ID = '0001b181d51bfa19'
IMAGE_ID = '00031197fb7b015d'


rel_in_image = df_rel[df_rel.ImageID == IMAGE_ID]
print (rel_in_image)

# iterate rows
for index, row in rel_in_image.iterrows():
    subject = help.map_to_name(row['LabelName1'])
    complement = help.map_to_name(row['LabelName2'])
    relation = help.map_to_name(row['RelationshipLabel'])
    print(subject, relation, complement)

# test image selection
# show_image(IMAGE_ID)

# test map to tag
# LABEL = 'Car'
# TARGET_LABEL = help.map_to_tag(LABEL)
# print (LABEL, TARGET_LABEL)

stats_img_avail()

