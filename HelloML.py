# This program Predicts whether it is orange or Apple Baesd Two features Weight and smoothy or bumpy
#0-Represent Bumpy ,1-represent smothy

from sklearn import tree
features=[[140,1],[130,1],[150,0],[170,0]]
labels=["Apple","Apple","Orange","Orange"]
clf=tree.DecisionTreeClassifier()
clf.fit(features,labels)
print(clf.predict([[160,0]]))
