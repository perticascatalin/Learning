import pickle

print ('load data')

with open('./pickles/class_name_dict.pickle', 'rb') as handle:
    class_name_dict = pickle.load(handle)

with open('./pickles/attr_name_dict.pickle', 'rb') as handle:
    attr_name_dict = pickle.load(handle)

with open('./pickles/rel_name_dict.pickle', 'rb') as handle:
    rel_name_dict = pickle.load(handle)

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