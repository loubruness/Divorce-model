import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, log_loss

from sklearn.ensemble import RandomForestClassifier

# Step 1: Read the CSV file
file_path = 'c:/Users/pauli/Documents/M1/S8/ML/Projet/divorce.csv'
data = pd.read_csv(file_path)

# Clean the dataset
data = data.dropna()

# Select relevant columns for regression (assuming 'X' is the feature and 'Y' is the target)
X = data.drop(['Divorce'], axis=1)
Y = data['Divorce']

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

X_train = X_train[['Q1', 'Q3',  'Q6', 'Q8', 'Q9', 'Q11', 'Q14', 'Q15', 'Q17', 'Q18', 'Q20', 'Q25', 'Q26','Q30', 'Q31', 'Q32', 'Q33', 'Q34', 'Q36', 'Q37', 'Q38', 'Q39', 'Q40', 'Q41', 'Q44', 'Q49', 'Q50', 'Q52', 'Q53', 'Q54']]
X_test = X_test[['Q1', 'Q3',  'Q6', 'Q8', 'Q9', 'Q11', 'Q14', 'Q15', 'Q17', 'Q18', 'Q20', 'Q25', 'Q26','Q30', 'Q31', 'Q32', 'Q33', 'Q34', 'Q36', 'Q37', 'Q38', 'Q39', 'Q40', 'Q41', 'Q44', 'Q49', 'Q50', 'Q52', 'Q53', 'Q54']]

# Train the linear regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Evaluate the model
Y_pred = model.predict(X_test)
Y_pred_proba = model.predict_proba(X_test)[:, 1]

# Confusion Matrix
cm = confusion_matrix(Y_test, Y_pred)

# Metrics
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred)
f1 = f1_score(Y_test, Y_pred)
roc_auc = roc_auc_score(Y_test, Y_pred_proba)
log_loss_value = log_loss(Y_test, Y_pred_proba)

# Print Metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'ROC AUC: {roc_auc}')
print(f'Log-Loss: {log_loss_value}')

joblib.dump(model, "divorceclassificationreduced.joblib")

# Function to predict a value
def predict_value(input_features):
    # Convert input features to DataFrame 
    input_data = pd.DataFrame([input_features], columns=X.columns)
    prediction = model.predict(input_data)
    return prediction[0]