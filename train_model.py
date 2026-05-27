import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# SAMPLE DATASET
# Replace later with real dataset if needed

data = {
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'age': [45, 30, 50, 25, 60],
    'bmi': [32, 22, 35, 20, 40],
    'blood_pressure': [140, 120, 150, 110, 160],
    'glucose_level': [180, 90, 200, 85, 220],
    'family_history': [1, 0, 1, 0, 1],
    'risk': ['HIGH', 'LOW', 'HIGH', 'LOW', 'HIGH']
}


df = pd.DataFrame(data)


# ENCODE GENDER

encoder = LabelEncoder()

df['gender'] = encoder.fit_transform(df['gender'])


# FEATURES

X = df[
    [
        'gender',
        'age',
        'bmi',
        'blood_pressure',
        'glucose_level',
        'family_history'
    ]
]


# TARGET

y = df['risk']


# SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# MODEL

model = DecisionTreeClassifier()


# TRAIN

model.fit(X_train, y_train)


# TEST

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy}")


# SAVE MODEL

joblib.dump(model, 'diabetes_model.pkl')

print("Model saved successfully.")