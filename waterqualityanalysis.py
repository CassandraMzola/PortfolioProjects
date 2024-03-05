# -*- coding: utf-8 -*-
"""WaterQualityAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VNCgTwGYJpxTOrL5FrvEwIJyzyYZuhC_
"""

#Load Data
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

import pandas as pd

# Load the dataset from Google Drive
file_path = '/content/drive/MyDrive/water_potability.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
df.head()

#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

df.head()

#Data Exploration

# Summary statistics
summary_stats = df.describe()

# Pairplot for visualizing relationships between variables
sns.pairplot(df, hue='Potability', diag_kind='kde')
plt.show()

# Data Cleaning
df.info()

# Display the count of missing values in each column
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)

# Handle missing values (we'll use mean imputation)
df.fillna(df.mean(), inplace=True)

# Display updated information after handling missing values
df.info()

# Display the first few rows of the cleaned dataframe
df.head()

# Correlation matrix
correlation_matrix = df.corr()

# Heatmap for visualization
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()

# Distribution of pH
plt.figure(figsize=(10, 6))
sns.histplot(df['ph'], bins=30, kde=True)
plt.title('Distribution of pH')
plt.xlabel('pH Value')
plt.show()

# Explore the distribution of potable and non-potable water
plt.figure(figsize=(6, 4))
sns.countplot(x='Potability', data=df)
plt.title('Distribution of Water Potability')
plt.xlabel('Potability (1: Potable, 0: Not Potable)')
plt.show()

# Split the data into features (X) and target variable (y)
X = df.drop('Potability', axis=1)
y = df['Potability']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the logistic regression model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Display feature importance
feature_importance = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_[0]})
feature_importance = feature_importance.sort_values(by='Coefficient', ascending=False)
print(feature_importance)

import matplotlib.pyplot as plt
import seaborn as sns

# Display feature importance as a horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=feature_importance, palette='viridis')
plt.title('Feature Importance for Predicting Water Potability')
plt.xlabel('Coefficient')
plt.ylabel('Feature')
plt.show()

# Boxplots for feature distribution by Potability
for feature in X.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Potability', y=feature, data=df)
    plt.title(f'Distribution of {feature} by Potability')
    plt.show()

# Boxplots to identify outliers
for feature in X.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()

from sklearn.model_selection import cross_val_score

# Perform cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())

from sklearn.metrics import roc_curve, roc_auc_score

# Get predicted probabilities
probs = model.predict_proba(X_test)[:, 1]

# Compute ROC curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, probs)
auc = roc_auc_score(y_test, probs)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

