import pandas as pd
ori = pd.read_csv('crop_recommendation.csv')

df = ori.copy()
df = df.dropna()

x = df.drop('label', axis=1)
y = df['label']

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(x,y)

#saving the model
import pickle
pickle.dump(clf, open('croprec_clf.pkl', 'wb'))
