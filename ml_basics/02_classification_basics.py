"""
================================================================
BEGINNER'S GUIDE: CLASSIFICATION (Predicting Categories)
================================================================
Last time we predicted a NUMBER (house price).
This time we predict a CATEGORY (which type of flower?).

Instead of drawing a line through data, classification draws
BOUNDARIES between different groups.

RUN THIS:   python 02_classification_basics.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# ================================================================
# STEP 1: Load a REAL dataset — Iris flowers
# ================================================================
print("=" * 60)
print("STEP 1: Loading a real-world dataset (Iris flowers)")
print("=" * 60)

# The Iris dataset is the "Hello World" of ML
# It has 3 types of flowers and 4 measurements
iris = datasets.load_iris()

# Features: sepal length, sepal width, petal length, petal width
X = iris.data
# Labels: 0=Setosa, 1=Versicolor, 2=Virginica
y = iris.target

print(f"Number of flowers: {X.shape[0]}")
print(f"Number of measurements per flower: {X.shape[1]}")
print(f"Measurements: {iris.feature_names}")
print(f"Types of flowers: {iris.target_names}")
print()

# Show first 3 flowers
print("First 3 flowers (measurements → type):")
for i in range(3):
    print(f"  Flower {i+1}: {X[i]} → {iris.target_names[y[i]]}")

# ================================================================
# STEP 2: Split & Train
# ================================================================
print()
print("=" * 60)
print("STEP 2: Training a classifier (K-Nearest Neighbors)")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# K-Nearest Neighbors: "Show me the 3 most similar flowers,
# and I'll predict the same type as the majority"
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

print("KNN Model trained! How it works:")
print("  To classify a new flower, find the 3 most similar")
print("  flowers in the training data, and pick the most")
print("  common type among them.")
print()

# ================================================================
# STEP 3: Predict & Evaluate
# ================================================================
print("=" * 60)
print("STEP 3: Testing the classifier")
print("=" * 60)

y_pred = model.predict(X_test)

# Accuracy = correct predictions / total predictions
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy:.2%}")
print(f"   → Correctly classified {int(accuracy * len(y_test))} out of {len(y_test)} flowers")
print()

# Confusion Matrix: shows WHICH mistakes the model makes
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix (rows=actual, columns=predicted):")
print("           Setosa  Versicolor  Virginica")
for i, name in enumerate(iris.target_names):
    row = f"{name:<10}"
    for j in range(3):
        row += f"  {cm[i][j]:<8}"
    print(row)
print()
print("  → Diagonal numbers = correct predictions")
print("  → Off-diagonal      = mistakes")
print()

# ================================================================
# STEP 4: Test with a NEW, completely unseen flower
# ================================================================
print("=" * 60)
print("STEP 4: Predicting a brand new flower!")
print("=" * 60)

# Let's describe a rose-like flower and see what the model predicts
# Measurements: [sepal length, sepal width, petal length, petal width]
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # Looks like Setosa
prediction = model.predict(new_flower)
probabilities = model.predict_proba(new_flower)

print(f"New flower measurements: {new_flower[0]}")
print(f"Model predicts: {iris.target_names[prediction[0]]}")
print()
print("Confidence for each type:")
for i, name in enumerate(iris.target_names):
    bar = "█" * int(probabilities[0][i] * 20)
    print(f"  {name:<10}: {probabilities[0][i]:.1%} {bar}")
print()

# ================================================================
# SUMMARY
# ================================================================
print("=" * 60)
print("🎉 Two Types of ML Problems")
print("=" * 60)
print("""
  REGRESSION (previous script):   Predict a NUMBER
    Example: House size → House price ($412k)
    Metric:  Mean Absolute Error ($12k off on avg)

  CLASSIFICATION (this script):   Predict a CATEGORY
    Example: Flower measurements → Flower type (Setosa)
    Metric:  Accuracy (96.7% correct)

  NEXT STEPS TO LEARN:
    • Overfitting: When a model memorizes instead of learns
    • Feature engineering: Creating better measurements
    • More models: Decision Trees, Neural Networks, etc.
""")