from __future__ import print_function


class DecisionTree:
    def __init__(self, attribute, treshold, attrname=None, default_child=None, branches=None):
        "Initialize by saying what attribute this node tests."
        self.attr = attribute
        self.treshold = treshold
        self.attrname = attrname or attribute
        self.default_child = default_child
        self.branches = branches or {}

    def __call__(self, example):
        "Given an example, classify it using the attribute and the branches."
        attrvalue = example[self.attr]
        if float(attrvalue) > self.treshold:
            return self.branches[(self.treshold, True)](example)
        else:
            return self.branches[(self.treshold, False)](example)

    def add(self, val, is_greater, subtree):
        "Add a branch seeing if val is greater or not then treshold."
        self.branches[(val, is_greater)] = subtree

    def display(self, indent=0):
        'print the tree'
        name = self.attrname
        print('Test', name)
        for (val, subtree) in self.branches.items():
            if val[1] is True:
                print(' ' * 4 * indent, name, '>', val[0], '==>', end=' ')
            else:
                print(' ' * 4 * indent, name, '<=', val[0], '==>', end=' ')
            subtree.display(indent + 1)