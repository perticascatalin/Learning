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

    return 'milk'

def map_to_tag(name):
    # check in classes
    if label in classes.keys():
        return classes[label]

    # check in attributes
    if label in attributes.keys():
        return attributes[label]

    return 'unknown'

# START PROGRAM

walk_the_input()
print_header("READ & PRINT TABLES:")

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')

#print (df_rel['RelationshipLabel'].value_counts())
#df_rel['RelationshipLabel'].head()
#print (df_rel['LabelName1'].value_counts())
#df_rel['LabelName1'].head()
#print (df_rel['LabelName2'].value_counts())
#df_rel['LabelName2'].head()

df_rel['ImageID'].value_counts()
df_rel.sample(5)

print_subheader('CLASSES:')
df_classes = pd.read_csv('./input/challenge-2019-classes-vrd.csv')
print (df_classes)

print_subheader('ATTR:')
df_attr = pd.read_csv('./input/challenge-2019-attributes-description.csv')
print(df_attr)

class_name_dict = dict(zip(df_classes.Label, df_classes.LabelName))
attr_name_dict = dict(zip(df_attr.Label, df_attr.LabelName))
classes = dict(zip(df_classes.LabelName, df_classes.Label))
attributes = dict(zip(df_attr.LabelName, df_attr.Label))

#print (class_name_dict)
#print (len(class_name_dict))
#print (attr_name_dict)
#print (len(attr_name_dict))

# Not existing
# print (map_to_name('alpha'))
# print (map_to_name('beta'))
# print (map_to_name('gamma'))

def list_class_labels():
    print_header("CLASS LABELS:")
    for key, val in class_name_dict.items():
        print (str(key) + ' ' + str(val))
    print('')

def list_attr_labels():
    print_header("ATTR LABELS:")
    for key, val in attr_name_dict.items():
        print (str(key) + ' ' + str(val))
    print('')

def list_classes():
    print_header("CLASS NAMES:")
    for key, val in classes.items():
        print (str(key) + ' ' + str(val))

def list_attributes():
    print_header("ATTR NAMES:")
    for key, val in attributes.items():
        print (str(key) + ' ' + str(val))

#list_class_labels()
#list_attr_labels()
list_classes()
list_attributes()
exit()

# SEARCH PART

# complement style (label name 2)
TARGET_LABEL = '/m/04dr76w' # Bottle
TARGET_LABEL = '/m/02hj4' # Hamster
TARGET_LABEL = '/m/09tvcd' # Wine Glass
TARGET_LABEL = '/m/083vt' # Wooden
TARGET_LABEL = '/m/04yx4' # Man
TARGET_LABEL = '/m/0k4j' # Car

print (map_to_name(TARGET_LABEL))

# Select required data
same_thing_repeated = df_rel[['LabelName1', 'LabelName2', 'RelationshipLabel']][df_rel.LabelName2 == TARGET_LABEL]
print(same_thing_repeated.head())

translated = same_thing_repeated
translated['LabelName1'] = translated[['LabelName1']].apply(lambda x : map_to_name(x.all()), axis = 1)
translated['LabelName2'] = translated[['LabelName2']].apply(lambda x : map_to_name(x.all()), axis = 1)
#print(translated.sample(50))

print (translated['RelationshipLabel'].value_counts())
print (translated['LabelName1'].value_counts())

#numerical = ['XMin1', 'XMax1', 'YMin1', 'YMax1', 'XMin2', 'XMax2', 'YMin2', 'YMax2']
#df_rel[numerical].hist(bins=15, figsize=(20, 10), layout=(2, 4));