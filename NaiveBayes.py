# Naive Bayes
import pandas as pd
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# Classifier Model (Naive Bayes)
from sklearn.naive_bayes import BernoulliNB
import joblib

start_time = time.time()
data = pd.read_csv('data.csv')
features = data.values[:, 1].astype('str')
labels = data.values[:, -1].astype('int')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(features,labels,test_size=0.25,random_state=0)
classifier_model = Pipeline([
                ('tfidf', TfidfVectorizer(analyzer='char')),
                ('bernoulliNB',BernoulliNB()),
])

classifier_model.fit(X_train, y_train)
y_pred = classifier_model.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report
cm=confusion_matrix(y_test,y_pred)
print(classification_report(y_test, y_pred, digits=4))
print("Confusion Matrix: \n", cm)
accuracy = (cm[0][0]+cm[1][1]+cm[2][2])/(cm[0][0]+cm[0][1]+cm[0][2]+cm[1][0]+cm[1][1]+cm[1][2]+cm[2][0]+cm[2][1]+cm[2][2])
print('Training Accuracy: ',classifier_model.score(features, labels))
print("Testing Accuracy = ", accuracy)
print("Time Taken to train the model = %s seconds" % round((time.time() - start_time),2))
# Save model
joblib.dump(classifier_model, 'NaiveBayes_Model.joblib')