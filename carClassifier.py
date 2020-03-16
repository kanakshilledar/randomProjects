# This is a crude program to classify between sports car and van
# By: Kanak Shilledar
# Training models

#   hp          seats           lbl
# 300           2               sport
# 450           2               sport
# 200           8               van
# 150           9               van

from sklearn import tree

features = [[300, 0], [450, 0], [200, 1], [150, 1]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

hp = int(input('Enter HP: '))
seat = int(input('Enter Seats: '))

a = clf.predict([[hp, seat]])
if a == 0:
    print('Sports Car')
else:
    print('Van')