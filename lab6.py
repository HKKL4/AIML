import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
data = pd.read_csv('teenis.csv')
print("The first 5 Values of data is :\n", data.head())
X = data.iloc[:, :-1]
print("\nThe First 5 values of the train attributes is\n", X.head())
Y = data.iloc[:, -1]
print("\nThe First 5 values of target values is\n", Y.head())
obj1= LabelEncoder()
X.Outlook = obj1.fit_transform(X.Outlook)
print("\n The Encoded and Transformed Data in Outlook \n",X.Outlook)
obj2 = LabelEncoder()
X.Temperature = obj2.fit_transform(X.Temperature)
obj3 = LabelEncoder()
X.Humidity = obj3.fit_transform(X.Humidity)
obj4 = LabelEncoder()
X.Wind = obj4.fit_transform(X.Wind)
print("\n The Encoded and Transformed Training Examples \n", X.head())
obj5 = LabelEncoder()
Y = obj5.fit_transform(Y)
print("The class Label encoded in numerical form is",Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.20)
#Training the classification Model using Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)
from sklearn.metrics import accuracy_score
print("Accuracy is:", accuracy_score(classifier.predict(X_test), Y_test))