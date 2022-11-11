from sklearn import datasets


cancer_data = datasets.load_breast_cancer()
print(cancer_data.data[5])

print(cancer_data.data.shape)
print(cancer_data.target)

from sklearn.model_selection import train_test_split
cancer_data = datasets.load_breast_cancer()
x_train,x_test,y_train,y_test = train_test_split(cancer_data.data,cancer_data.target,test_size=0.4,random_state=109)

from sklearn import svm
cls = svm.SVC(kernel="linear")
cls.fit(x_train,y_train)
pred = cls.predict(x_test)

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

letters = datasets.load_digits()
clf = svm.SVC(gamma=0.001,C=100)
X,y=letters.data[:-10],letters.target[:-10]
clf.fit(X,y)
print(clf.predict(letters.data[:-10]))
plt.imshow(letters.images[6],interpolation='nearest')
plt.show()
