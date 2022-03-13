# pylint: disable=no-member
from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
import random

# [height, weight, shoe size]
X = [[178, 65, 43], [167, 50, 38], [150, 40, 36], [190, 90, 45], [185, 84, 44], [180, 70, 40], [170, 50, 36], [160, 45, 36], [175, 55, 38], [182, 78, 40]]

# gender labels
Y = ['male',        'female',      'female',      'male',        'male',        'male',         'female',     'female',      'female',      'male']

myClassifierTree = tree.DecisionTreeClassifier()
myClassifierTree = myClassifierTree.fit(X,Y)

myClassifierAdaBoost = ensemble.AdaBoostClassifier()
myClassifierAdaBoost = myClassifierAdaBoost.fit(X,Y)

myClassifierRandforest = ensemble.RandomForestClassifier()
myClassifierRandforest = myClassifierRandforest.fit(X,Y)


for i in range(5):
    random.seed(i)
    randHeight = random.randint(140, 200)
    randWeight = random.randint(40, 110)
    randShoesize = random.randint(35,45)

    randPerson = [[randHeight, randWeight, randShoesize]]

    predictionTree = myClassifierTree.predict(randPerson)
    predictionAdaBoost = myClassifierAdaBoost.predict(randPerson)
    predictionRandForest= myClassifierRandforest.predict(randPerson)

    print(randPerson)
    print("Tree:")
    print(predictionTree)

    print("AdaBoost:")
    print(predictionAdaBoost)

    print("Random forest:")
    print(predictionRandForest)
