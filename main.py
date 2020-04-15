import csv
from math import sqrt

csvfile = open ("training.csv", "r")
csvfile2 = open ("predict.csv", "r")
lines = csv.reader (csvfile)
lines2 = csv.reader (csvfile2)
dataset_train = list (lines)
dataset_test = list(lines2)

for x in range(len(dataset_train)-1):
  for y in range (4):
    dataset_train[x][y] = float(dataset_train[x][y])
    
for x in range(len(dataset_test)-1):
  for y in range (4):
    dataset_test[x][y] = float(dataset_test[x][y])

def distance (a, b):
    somme = 0
    for i in range (len (a)):
        try:
            somme += (a [i] - b [i]) * (a [i] - b [i])
        except:
            pass
    return (sqrt (somme))

def lePlusProcheVoisin (x):
    lePlusPres = 0
    distanceMin = float("inf")
    for i in range(len(dataset_train)-1):
        di = distance (x, dataset_train[0:4])
        if di != 0 and di < distanceMin:
            lePlusPres = i
            distanceMin = di
    return (lePlusPres)

def lesKplusProchesVoisins (x, k):
  listeDesDistances = []
  for i in range (len (dataset_train)):
    listeDesDistances.append (distance (x, dataset_train[i] )) 
  Kppv = []
  for i in range (k):
    p = float ("inf")
    for j in range (len (dataset_train)-1):
      if listeDesDistances [j] != 0 and listeDesDistances [j] < p and j not in Kppv:
        p = listeDesDistances [j]
        indice = j
    Kppv. append (indice)
  return (Kppv)



def qui_est_majoritaire(Kppv):
    nature = []
    for i in Kppv:
        nature += [dataset_train[i][4]]
    return max(set(nature))
    
for i in dataset_test[0:len(dataset_test)-1]:
    print(qui_est_majoritaire(lesKplusProchesVoisins(i,12)))


