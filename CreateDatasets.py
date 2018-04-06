from copy import deepcopy
import Dataset


def create_dataset(file, attrnames, target, values):
    'create dataset as list of dictionary'
    dataset = []
    r = []
    attributes = []
    for line in open(file).readlines():
        r = line.split(',')
        r = [p.rstrip() for p in r]
        dataset.append(r)
    examples = []
    for i in range(len(dataset)):
        example = {}
        for j in range(len(dataset[0])):
            example[j] = dataset[i][j]
        examples.append(example)
    for k in range(len(examples[0])):
        attributes.append(k)
    inputs = removeTarget(attributes, target)
    return Dataset.DataSet(file, examples, inputs, attributes, target, attrnames, values)


def create_dataset_iono(file, attrnames, target, values):
    'create a dataset for ionosphere file with examples sorted by class'
    dataset = []
    r = []
    examples = []
    attributes = []
    for line in open(file).readlines():
        r = line.split(',')
        r = [p.rstrip() for p in r]
        dataset.append(r)
    for i in range(len(dataset)):
        example = {}
        for j in range(len(dataset[0])):
            example[j] = dataset[i][j]
        examples.append(example)
    sorted_example1 = []
    sorted_example2 = []
    for e in examples:
        if e[target] == 'b':
            sorted_example1.append(e)
        if e[target] == 'g':
            sorted_example2.append(e)
    sorted_example = sorted_example1 + sorted_example2
    for k in range(len(examples[0])):
        attributes.append(k)
    inputs = removeTarget(attributes, target)
    return Dataset.DataSet(file, sorted_example, inputs, attributes, target, attrnames, values)


def get_values(file, n_attrs):
    'create a list of list with sorted and singles values of attributes'
    dataset = []
    r = []
    examples = []
    for line in open(file).readlines():
        r = line.split(",")
        r = [p.rstrip() for p in r]
        dataset.append(r)
    for i in range(len(dataset)):
        example = {}
        for j in range(len(dataset[0])):
            example[j] = dataset[i][j]
            examples.append(example)
    values_list = []
    for n in range(n_attrs):
        values_list.append(sorted(list(set([e[n] for e in examples]))))
    return values_list


def removeTarget(attributes, target):
    "return attribute without class"
    input = deepcopy(attributes)
    input.pop(input.index(target))
    return input
