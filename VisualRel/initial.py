import pickle
import pandas as pd

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')
df_classes = pd.read_csv('./input/challenge-2019-classes-vrd.csv')
df_attr = pd.read_csv('./input/challenge-2019-attributes-description.csv')
df_relat = pd.read_csv('./input/challenge-2019-relationships-description.csv')

class_name_dict = dict(zip(df_classes.Label, df_classes.LabelName))
attr_name_dict = dict(zip(df_attr.Label, df_attr.LabelName))
rel_name_dict = dict(zip(df_relat.Label, df_relat.LabelName))
classes = dict(zip(df_classes.LabelName, df_classes.Label))
attributes = dict(zip(df_attr.LabelName, df_attr.Label))
relations = dict(zip(df_relat.LabelName, df_relat.Label))

print ('restore data')

with open('./pickles/class_name_dict.pickle', 'wb') as handle:
    pickle.dump(class_name_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('./pickles/attr_name_dict.pickle', 'wb') as handle:
    pickle.dump(attr_name_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('./pickles/rel_name_dict.pickle', 'wb') as handle:
    pickle.dump(rel_name_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('./pickles/classes.pickle', 'wb') as handle:
    pickle.dump(classes, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('./pickles/attributes.pickle', 'wb') as handle:
    pickle.dump(attributes, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('./pickles/relations.pickle', 'wb') as handle:
    pickle.dump(relations, handle, protocol=pickle.HIGHEST_PROTOCOL)