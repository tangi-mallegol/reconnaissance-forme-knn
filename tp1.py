#!/usr/bin/python2.7
# -*- coding: ISO-8859-1 -*-

class Iris: # Définition de notre classe Personne


    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, class_=None): # Notre méthode constructeur
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.class_ = class_


    def calculDistance(self, iris_2):
        return abs(self.sepal_length - iris_2.sepal_length)
        + abs(self.sepal_width - iris_2.sepal_width)
        + abs(self.petal_length - iris_2.petal_length)
        + abs(self.petal_width - iris_2.petal_width)

    def calculDistance(self, iris2, a, b, c, d):
        return abs(self.sepal_length - iris_2.sepal_length) * a
        + abs(self.sepal_width - iris_2.sepal_width) * b
        + abs(self.petal_length - iris_2.petal_length) * c
        + abs(self.petal_width - iris_2.petal_width) * d;

def KNN(iris1, k, base):
    tableau_distance = []
    for iris in base:
        tableau_distance.append((iris, iris.calculDistance(iris1)))
    sorted(tableau_distance, key=lambda tup: tup[1])
    results = tableau_distance[0:k]
    classes = dict()
    for res in results:
        classes[res[0].class_] = classes.get(res[0].class_, 0) + 1
    print(classes)

def KNN_Params_Pondere(iris1, k, base, a, b, c, d):
    tableau_distance = []
    for iris in base:
        tableau_distance.append((iris, iris.calculDistance(iris1, a, b, c, d)))
    sorted(tableau_distance, key=lambda tup: tup[1])
    results = tableau_distance[0:k]
    classes = dict()
    for res in results:
        classes[res[0].class_] = classes.get(res[0].class_, 0) + 1
    print(classes);

#Algorithme KNN avec pondération des paramètres et pondérations des voisins par leur distance (multiplication par l'inverse de la distance)
def KNN_Ponderation_Distance_Params(iris1, k, base, a, b, c, d):
    tableau_distance = []
    for iris in base:
        tableau_distance.append((iris, iris.calculDistance(iris1, a, b, c, d)))
    sorted(tableau_distance, key=lambda tup: tup[1])
    results = tableau_distance[0:k]
    classes = dict()
    for res in results:
        classes[res[0].class_] = classes.get(res[0].class_, 0) + 1/tup[1];
    print(classes);

flowers = []
with open('./iris.data', 'r') as f:
    for line in f:
        splitted_value = line.split(',')
        flowers.append(Iris(float(splitted_value[0]),
                            float(splitted_value[1]),
                            float(splitted_value[2]),
                            float(splitted_value[3]),
                            splitted_value[4].replace("\n", "")))


test = Iris(4.9,3.1,1.5,0.1)
KNN(test, 5, flowers)
