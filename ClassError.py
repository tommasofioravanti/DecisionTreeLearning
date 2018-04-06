import random
import numpy as np
import DecisionTreeLearning


def error_rate(decision_tree, examples, target):
    'calculate the class error'
    err = 0
    for e in examples:
        if e[target] != decision_tree(e):
            err += 1
    return (float(err) / len(examples)) * 100


def create_class_list(dataset):
    'create a list of list that contains the examples with the same class'
    bounds = []
    bounds.append(0)
    examples_list = []
    for i in range(len(dataset.examples) - 1):
        if dataset.examples[i][dataset.target] != dataset.examples[i + 1][dataset.target]:
            bounds.append(i + 1)
    bounds.append(len(dataset.examples))
    for b in range(len(bounds) - 1):
        examples_list.append(dataset.examples[bounds[b]:bounds[b + 1]])
    return examples_list


def stratified_k_fold_cross_validation(dataset, k, target):
    'return average and deviation standard of class error with a stratified 10-fold cross validation'
    training_error = 0
    test_error = 0
    examples = dataset.examples
    training_e = np.array([])
    test_e = np.array([])
    ex_list = create_class_list(dataset)
    for i in range(len(ex_list)):
        random.shuffle(ex_list[i])
    for i in range(0, k):
        test_set = []
        training_set = []
        for j in range(len(ex_list)):
            if i == k - 1:
                test_set += (ex_list[j][i * ((len(ex_list[j])) / k):])
                training_set += (ex_list[j][0: i * ((len(ex_list[j])) / k)])
            else:
                test_set += (ex_list[j][i * ((len(ex_list[j])) / k): i * (len(ex_list[j]) / k) + ((len(ex_list[j])) / k)])
                training_set += (
                    ex_list[j][:i * ((len(ex_list[j])) / k)] + ex_list[j][
                                                             i * ((len(ex_list[j])) / k) + ((len(ex_list[j])) / k):])
        dataset.examples = training_set
        tree = DecisionTreeLearning.DecisionTreeLearner(dataset)
        training_error = error_rate(tree, dataset.examples, target)
        training_e = np.append(training_e, training_error)
        test_error = error_rate(tree, test_set, target)
        test_e = np.append(test_e, test_error)
        dataset.examples = examples
    print 'Average training error: ', np.mean(training_e), 'Average test error: ', np.mean(
        test_e), 'Standard deviation training error: ', np.std(training_e), 'Standard deviation test error: ', np.std(
        test_e)
