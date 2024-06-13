import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, log_loss

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

# Train the linear regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Evaluate the model
Y_pred = model.predict(X_test)
Y_pred_proba = model.predict_proba(X_test)[:, 1]

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

joblib.dump(model, "divorceclassification.joblib")

# Function to predict a value
def predict_value(input_features):
    # Convert input features to DataFrame 
    input_data = pd.DataFrame([input_features], columns=X.columns)
    prediction = model.predict(input_data)
    return prediction[0]