import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random
import os # listing files and directories

header_index = 0

def print_header(header):
    global header_index
    print ('====================================')
    print (str(header_index) + '. ' + header)
    print ('====================================')
    header_index += 1

def print_subheader(header):
    print ('------------------------------------')
    print (header)
    print ('------------------------------------')

def walk_the_input():
    print_header("WALK THE INPUT:")
    for dirname, _, filenames in os.walk('./input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))

def map_to_name(label):
    # check in class labels
    if label in class_name_dict.keys():
        return class_name_dict[label]

    # check in attr labels
    if label in attr_name_dict.keys():
        return attr_name_dict[label]

    # check in relat labels
    if label in rel_name_dict.keys():
        return rel_name_dict[label]

    return 'unknown label'

def map_to_tag(name):
    # check in classes
    if name in classes.keys():
        return classes[name]

    # check in attributes
    if name in attributes.keys():
        return attributes[name]

    # check in relations
    if name in relations.keys():
        return relations[name]

    return 'unknown name'

# START PROGRAM

walk_the_input()
print_header("READ & PRINT TABLES:")

print_subheader('RELATIONS')
df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')
print (df_rel.sample(5))

print_subheader('CLASSES:')
df_classes = pd.read_csv('./input/challenge-2019-classes-vrd.csv')
print (df_classes)

print_subheader('ATTR:')
df_attr = pd.read_csv('./input/challenge-2019-attributes-description.csv')
print(df_attr)

print_subheader('RELATIONS:')
df_relat = pd.read_csv('./input/challenge-2019-relationships-description.csv')
print(df_relat)

print_header('DATA HELPER')

class_name_dict = dict(zip(df_classes.Label, df_classes.LabelName))
attr_name_dict = dict(zip(df_attr.Label, df_attr.LabelName))
rel_name_dict = dict(zip(df_relat.Label, df_relat.LabelName))
classes = dict(zip(df_classes.LabelName, df_classes.Label))
attributes = dict(zip(df_attr.LabelName, df_attr.Label))
relations = dict(zip(df_relat.LabelName, df_relat.Label))

def list_classes():
    print_subheader('CLASS NAMES:')
    for key, val in classes.items():
        print (str(key) + ' ' + str(val))

def list_attributes():
    print_subheader('ATTR NAMES:')
    for key, val in attributes.items():
        print (str(key) + ' ' + str(val))

def list_relations():
    print_subheader('RELATION NAMES:')
    for key, val in relations.items():
        print (str(key) + ' ' + str(val))

list_classes()
list_attributes()
list_relations()

print_subheader('SEARCH TRIPLET:')
# A, B, C label
A = 'Man'
B = 'Car'
C = 'inside of'

tag_A = map_to_tag(A)
tag_B = map_to_tag(B)
tag_C = map_to_tag(C)

print (tag_A, tag_B, tag_C)

triplets = df_rel
triplets = triplets[triplets.LabelName1 == tag_A][triplets.LabelName2 == tag_B][triplets.RelationshipLabel == tag_C]
print (triplets.head())


print_subheader('LOOK AT LABEL:')
# Complement label (label name 2)
# TARGET_LABEL = '/m/04dr76w' # Bottle
# TARGET_LABEL = '/m/02hj4' # Hamster
# TARGET_LABEL = '/m/09tvcd' # Wine Glass
# TARGET_LABEL = '/m/083vt' # Wooden
# TARGET_LABEL = '/m/04yx4' # Man
# TARGET_LABEL = '/m/0k4j' # Car

LABEL = 'Car'
TARGET_LABEL = map_to_tag(LABEL)
print (TARGET_LABEL)

# Select required data
same_thing_repeated = df_rel[['LabelName1', 'LabelName2', 'RelationshipLabel']][df_rel.LabelName2 == TARGET_LABEL]
print(same_thing_repeated.head())

translated = same_thing_repeated
translated['LabelName1'] = translated[['LabelName1']].apply(lambda x : map_to_name(x.all()), axis = 1)
translated['LabelName2'] = translated[['LabelName2']].apply(lambda x : map_to_name(x.all()), axis = 1)
#print(translated.sample(50))

print (translated['RelationshipLabel'].value_counts())
print (translated['LabelName1'].value_counts())

print_header('DATA ANALYSIS:')

print_subheader('Tag Occurences')
print (df_rel['RelationshipLabel'].value_counts())
#df_rel['RelationshipLabel'].head()
print (df_rel['LabelName1'].value_counts())
#df_rel['LabelName1'].head()
print (df_rel['LabelName2'].value_counts())
#df_rel['LabelName2'].head()

print_subheader('Relations per image')
print (df_rel['ImageID'].value_counts())

# Distribution of relationships around image
#numerical = ['XMin1', 'XMax1', 'YMin1', 'YMax1', 'XMin2', 'XMax2', 'YMin2', 'YMax2']
#df_rel[numerical].hist(bins=15, figsize=(20, 10), layout=(2, 4));