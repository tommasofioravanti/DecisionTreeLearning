import DecisionTreeLearning
import CreateDatasets

# Iris dataset

iris_names = {0: 'sepal-length', 1: 'sepal-width', 2: 'petal-length', 3: 'petal-width', 4: 'class'}
iris_values = {4: ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']}
target = 4
iris_dataset=CreateDatasets.create_dataset('iris.txt', iris_names, target, iris_values)
iris_tree = DecisionTreeLearning.DecisionTreeLearner(iris_dataset)
iris_tree.display()
print ("\n\n")
'''
for e in iris_dataset.examples:
    print("EXAMPLE:", e)
    print("CLASS:", iris_tree(e))
'''

# Bankonote dataset
banknote_names = {0: 'variance', 1: 'asimmetria', 2: 'curtosi', 3: 'entropia', 4: 'class'}
banknote_values = {4: ['0', '1']}
target = 4
#banknote_dataset=CreateDatasets.create_dataset('data_banknote_authentication.txt', banknote_names, target, banknote_values)
#banknote_tree = DecisionTreeLearning.DecisionTreeLearner(banknote_dataset)
#banknote_tree.display()


# Sonar Dataset
sonar_names = {0: 'energy-freq-band1', 1: 'energy-freq-band2', 2: 'energy-freq-band3',
             3: 'energy-freq-band4',
             4: 'energy-freq-band5', 5: 'energy-freq-band6', 6: 'energy-freq-band7',
             7: 'energy-freq-band8',
             8: 'energy-freq-band9', 9: 'energy-freq-band10', 10: 'energy-freq-band11',
             11: 'energy-freq-band12', 12: 'energy-freq-band13', 13: 'energy-freq-band14',
             14: 'energy-freq-band15', 15: 'energy-freq-band16', 16: 'energy-freq-band17',
             17: 'energy-freq-band18',
             18: 'energy-freq-band19', 19: 'energy-freq-band20', 20: 'energy-freq-band21',
             21: 'energy-freq-band22', 22: 'energy-freq-band23',
             23: 'energy-freq-band24', 24: 'energy-freq-band25', 25: 'energy-freq-band26', 26: 'energy-freq-band27',
             27: 'energy-freq-band28',
             28: 'energy-freq-band29',
             29: 'energy-freq-band30', 30: 'energy-freq-band31', 31: 'energy-freq-band32',
             32: 'energy-freq-band33',
             33: 'energy-freq-band34', 34: 'energy-freq-band35', 35: 'energy-freq-band36',
             36: 'energy-freq-band37', 37: 'energy-freq-band38', 38: 'energy-freq-band39',
             39: 'energy-freq-band40', 40: 'energy-freq-band41', 41: 'energy-freq-band42',
             42: 'energy-freq-band43',
             43: 'energy-freq-band44', 44: 'energy-freq-band45', 45: 'energy-freq-band46',
             46: 'energy-freq-band47', 47: 'energy-freq-band48',
             48: 'energy-freq-band49', 49: 'energy-freq-band50', 50: 'energy-freq-band51', 51: 'energy-freq-band52',
             52: 'energy-freq-band53',
             53: 'energy-freq-band54',
             54: 'energy-freq-band55', 55: 'energy-freq-band56', 56: 'energy-freq-band57',
             57: 'energy-freq-band58',
             58: 'energy-freq-band59', 59: 'energy-freq-band60', 60: 'class'}
sonar_values = {60: ['R', 'M']}
target = 60
#sonar_dataset = CreateDatasets.create_dataset('sonar.txt', sonar_names, target, sonar_values)
#sonar_tree = DecisionTreeLearning.DecisionTreeLearner(sonar_dataset)
#sonar_tree.display()

#Ionosphere dataset
iono_names = {0: 'attr1', 1: 'attr2', 2: 'attr3',
              3: 'attr4',
              4: 'attr5', 5: 'attr6', 6: 'attr7',
              7: 'attr8',
              8: 'attr9', 9: 'attr10', 10: 'attr11',
              11: 'attr12', 12: 'attr13', 13: 'attr14',
              14: 'attr15', 15: 'attr16', 16: 'attr17',
              17: 'attr18',
              18: 'attr19', 19: 'attr20', 20: 'attr21',
              21: 'attr22', 22: 'attr23',
              23: 'attr24', 24: 'attr25', 25: 'attr26', 26: 'attr27',
              27: 'attr28',
              28: 'attr29',
              29: 'attr30', 30: 'attr31', 31: 'attr32',
              32: 'attr33',
              33: 'attr34', 34: 'class'}
iono_values = {34: ['b', 'g']}
target = 34
#iono_dataset=CreateDatasets.create_dataset_iono('ionosphere.txt',iono_names,target,iono_values)
#iono_tree=DecisionTreeLearning.DecisionTreeLearner(iono_dataset)
#iono_tree.display()

# Wine Dataset
wine_names = {0: 'alcohol', 1: 'Malic-acid', 2: 'ash',
              3: 'ash-alcalinity',
              4: 'magnesium', 5: 'total-phenols', 6: 'flavanoids',
              7: 'nonflavanoid-phenols',
              8: 'proanthocyanins', 9: 'color-intensity', 10: 'hue',
              11: 'OD280/OD/315', 12: 'proline', 13: 'class'}
wine_values = {13: ['1', '2', '3']}
target=13
#wine_dataset=CreateDatasets.create_dataset('wine.txt',wine_names,target,wine_values)
#wine_tree=DecisionTreeLearning.DecisionTreeLearner(wine_dataset)
#wine_tree.display()
