import Leaf
import DecisionTree
import math
import CreateDatasets


def DecisionTreeLearner(dataset):
    target, value = dataset.target, dataset.values
    values_list = CreateDatasets.get_values('iris.txt', 4)

    def decisionTreeLearning(examples, attributes, parents_examples=()):
        if len(examples) == 0:
            return PluralityValue(parents_examples)
        elif sameClassification(examples):
            return Leaf.Leaf(examples[0][target])
        elif len(attributes) == 0:
            return PluralityValue(examples)
        else:
            A, treshold = Importance(attributes, examples)
            tree = DecisionTree.DecisionTree(A, treshold, dataset.attrnames[A])
            less_or_equal, greater = split_continuous(A, treshold, examples)
            subtree_less_equal = decisionTreeLearning(less_or_equal, removeall(A, attributes), examples)
            tree.add(treshold, False, subtree_less_equal)
            subtree_greater = decisionTreeLearning(greater, removeall(A, attributes), examples)
            tree.add(treshold, True, subtree_greater)
            return tree

    def sameClassification(examples):
        "Return True if examples have the same class"
        class_ = examples[0][target]
        for e in examples:
            if e[target] != class_:
                return False
        return True

    def count(attribute, value, example):
        "count the number of examples that have e[attribute]= value"
        c = 0
        for e in example:
            if e[attribute] == value:
                c += 1
        return c

    def removeall(item, seq):
        "Return a copy of seq with all occurences of item removed."
        rem = []
        for x in seq:
            if x != item:
               rem.append(x)
        return rem


    def PluralityValue(examples):
        "Select the most common class value among this set of examples"
        i = 0
        for v in value[target]:
            if count(target, v, examples) > i:
                i = count(target, v, examples)
                popular = v
        return Leaf.Leaf(popular)

    def information_gain(attribute, treshold, examples):

        def entropy(examples):
            e = 0
            for v in value[target]:
                if len(examples) != 0:
                    p = float(count(target, v, examples)) / len(examples)
                    if p != 0:
                        e += (-p) * math.log(p, 2.0)
            return float(e)

        def remainder(examples):
            r_less_equal = 0
            r_greater = 0
            r = 0
            N = float(len(examples))
            min_exe, max_exe = split_continuous(attribute, treshold, examples)
            r_less_equal += (float((len(min_exe))) / N) * entropy(min_exe)
            r_greater += (float((len(max_exe))) / N) * entropy(max_exe)
            r = r_greater + r_less_equal
            return r

        return entropy(examples) - remainder(examples)

    def Importance(attributes, examples):
        "Found the most important attribute according to information gain"
        imp = 0
        treshold = 0

        for at in attributes:
            t = split_point(at, examples)
            if information_gain(at, t, examples) >= imp:
                imp = information_gain(at, t, examples)
                most_importance_attr = at
                treshold = t
        return most_importance_attr, treshold

    def split_continuous(attribute, treshold, examples):
        'return two list of examples that have values of attribute <= or > of treshold'
        less_or_equal = []
        greater = []
        for e in examples:
            if float(e[attribute]) <= treshold:
                less_or_equal.append(e)
            else:
                greater.append(e)
        return less_or_equal, greater

    def split_point(attr, examples):
        'return the treshold according to information gain'
        max = 0
        treshold = 0
        for i in range(len(values_list[attr]) - 1):
            v = (float(values_list[attr][i]) + float(values_list[attr][i + 1])) / 2
            if information_gain(attr, v, examples) > max:
                max = information_gain(attr, v, examples)
                treshold = v
        return treshold

    return decisionTreeLearning(dataset.examples, dataset.inputs)
