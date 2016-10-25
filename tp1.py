#!/usr/bin/python2.7
# -*- coding: ISO-8859-1 -*-
import numpy as np
import random
import sys

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

    def calculDistance(self, iris_2, a, b, c, d):
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

#Algorithme KNN avec pondération des paramètres et pondérations des voisins par leur distance (multiplication par l'inverse de la distance)
def KNN_Ponderation_Distance_Params(iris1, k, base, a, b, c, d, coeff_distance):
    tableau_distance = []
    for iris in base:
        tableau_distance.append((iris, iris.calculDistance(iris1, a, b, c, d)))
    tableau_distance = sorted(tableau_distance, key=lambda tup: tup[1])
    results = tableau_distance[0:k]
    classes = dict()
    for res in results:
        classes[res[0].class_] = classes.get(res[0].class_, 0) + coeff_distance/res[1]
    distance_minimum = float('inf')
    classe_ = ""
    for classe in classes.keys():
        if classes[classe] < distance_minimum:
            distance_minimum = classes[classe]
            classe_ = classe
    return classe_

flowers = {"Iris-setosa" : [], "Iris-versicolor" : [], "Iris-virginica" : [] };
with open('./iris.data', 'r') as f:
    for line in f:
        splitted_value = line.split(',')
        classe = splitted_value[4].replace("\n", "");
        flowers[classe].append(Iris(float(splitted_value[0]),
                            float(splitted_value[1]),
                            float(splitted_value[2]),
                            float(splitted_value[3]),
                            classe));

base_apprentissage = [];
base_test = [];
proportion_apprentissage = 0.7;
for classe in flowers:
    random.shuffle(flowers[classe])
    limite = int(len(flowers[classe])*proportion_apprentissage)
    for index in range(1,limite):
        base_apprentissage.append(flowers[classe][index])
    for index in range(limite+1, len(flowers[classe])):
        base_test.append(flowers[classe][index])
# On teste différents facteur de pondération sur les paramètres, l'importance de la distance et le k

# Facteurs sur les paramètres
a = np.arange(0.5, 5, 1)
b = np.arange(0.5, 5, 1)
c = np.arange(0.5, 5, 1)
d = np.arange(0.5, 5, 1)

# Facteur sur l'importance de la distance
coeff_distance = np.arange(0, 5, 0.5)

#Facteur k
Ks = np.arange(1, 5)

resultats = []

taille_test = len(base_test)
nbTour = len(a)*len(b)*len(c)*len(d)*len(Ks)*len(coeff_distance)
nbDone = 0
#Tests
for a1 in a:
    for b1 in b:
        for c1 in c:
            for d1 in d:
                coeff = 1
                for k in Ks:
                    for coeff in coeff_distance:
                        well_guess = 0
                        for test in base_test:
                            result = KNN_Ponderation_Distance_Params(test, k, base_apprentissage, a1, b1, c1, d1, coeff)
                            if(result == test.class_):
                                well_guess = well_guess + 1
                        nbDone = nbDone + 1
                        sys.stdout.write("\r%f%%" % (float(nbDone)/float(nbTour)))
                        sys.stdout.flush()
                        resultats.append({ "taux_reussite" : float(well_guess) / float(taille_test), "a" : a1, "b" : b1, "c" : c1, "d" : d1, "coeff_distance" : coeff, "k" : k });
resultats = sorted(resultats, key=lambda tup: tup["taux_reussite"], reverse=True)
for index in range(1,10):
    print(resultats[index])
