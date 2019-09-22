import helpers as help
import pandas as pd

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')
df_bbox = pd.read_csv('./input/challenge-2019-train-vrd-bbox.csv')

IMAGE_ID = '00031197fb7b015d'

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