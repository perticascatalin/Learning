import pickle

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

print ('load data')
with open('./pickles/class_name_dict.pickle', 'rb') as handle:
    class_name_dict = pickle.load(handle)
with open('./pickles/attr_name_dict.pickle', 'rb') as handle:
    attr_name_dict = pickle.load(handle)
with open('./pickles/rel_name_dict.pickle', 'rb') as handle:
    rel_name_dict = pickle.load(handle)
with open('./pickles/classes.pickle', 'rb') as handle:
    classes = pickle.load(handle)
with open('./pickles/attributes.pickle', 'rb') as handle:
    attributes = pickle.load(handle)
with open('./pickles/relations.pickle', 'rb') as handle:
    relations = pickle.load(handle)

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