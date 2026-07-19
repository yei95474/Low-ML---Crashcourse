"""
================================================================
BEGINNER'S GUIDE TO MACHINE LEARNING
================================================================
This script teaches you the CORE CONCEPTS of Machine Learning
in the simplest possible way. No fancy terms — just real code.

WHAT YOU'LL LEARN:
  1. What is a "dataset" (features + labels)
  2. What is "training" vs "testing"
  3. What is a "model" (just a math formula!)
  4. What is "predicting" vs "actual answer"
  5. How to measure "accuracy"

RUN THIS:   python 01_intro_to_ml.py
"""

# ================================================================
# STEP 0: Import the tools we need
# ================================================================
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend (no GUI needed)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ================================================================
# STEP 1: Create a DATASET
# ================================================================
# In ML, a dataset is just a TABLE of numbers.
#
#   - FEATURES (X): The inputs → what you already know.
#   - LABELS   (y): The answers → what you want to predict.
#
# We'll make a fake dataset about HOUSES:
#   X = house size (square meters)
#   y = house price (in $1000s)
#
# The rule we'll HIDE from the model:
#   price = size * 3 + 50   (plus some random noise)

print("=" * 60)
print("STEP 1: Creating a simple dataset")
print("=" * 60)

np.random.seed(42)  # Fix random numbers so results are repeatable

# Create 100 random house sizes between 30 and 200 sq meters
X = np.random.uniform(30, 200, 100).reshape(-1, 1)

# Create prices with a HIDDEN PATTERN: price ≈ size × 3 + 50
# (plus some random noise so it's not perfectly predictable)
noise = np.random.normal(0, 15, 100)  # random noise
y = (X.flatten() * 3 + 50) + noise

print(f"Dataset: {len(X)} houses")
print(f"Features (house sizes): {X[:5].flatten()} ...")
print(f"Labels  (house prices): {y[:5]} ...")
print()

# Visualize the data
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X, y, alpha=0.7)
plt.xlabel("House Size (sq m)")
plt.ylabel("Price ($1000s)")
plt.title("Our Dataset: Size vs Price")
plt.grid(True, alpha=0.3)

# ================================================================
# STEP 2: Split into TRAINING set and TESTING set
# ================================================================
#   TRAINING set: what the model learns from
#   TESTING set:  what we use to CHECK if the model learned well
#
# If you test on data the model already saw, it's CHEATING!
# You want to see if it can PREDICT new data it hasn't seen.

print("=" * 60)
print("STEP 2: Splitting data into TRAINING and TESTING sets")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training data:  {len(X_train)} houses")
print(f"Testing data:   {len(X_test)} houses")
print()

# ================================================================
# STEP 3: Create and TRAIN a model
# ================================================================
# A model is just a MATH FORMULA.
# For this simple problem, the formula is a straight line:
#
#   price = slope × size + intercept
#
# "Training" = finding the best slope and intercept
#             so the line fits our data well.

print("=" * 60)
print("STEP 3: Creating and TRAINING a model")
print("=" * 60)

# Create the model (this is our "brain" we'll teach)
model = LinearRegression()

# Train the model (find the best line through the data)
model.fit(X_train, y_train)

# The model learned TWO numbers:
slope = model.coef_[0]
intercept = model.intercept_

print(f"Model learned these values:")
print(f"  slope     = {slope:.2f}")
print(f"  intercept = {intercept:.2f}")
print()
print(f"The TRUE formula was: price = size × 3 + 50")
print(f"The LEARNED formula:   price = size × {slope:.2f} + {intercept:.2f}")
print()

# Visualize the trained model
plt.subplot(1, 2, 2)
plt.scatter(X_train, y_train, alpha=0.6, label="Training data", color="blue")
plt.scatter(X_test, y_test, alpha=0.6, label="Testing data", color="green")

# Plot the model's predictions as a line
x_line = np.linspace(20, 210, 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color="red", linewidth=2, label="Model (learned line)")

plt.xlabel("House Size (sq m)")
plt.ylabel("Price ($1000s)")
plt.title("Model Trained on Data")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("01_model_training.png", dpi=150)
print("📊 Chart saved as: 01_model_training.png")
print()

# ================================================================
# STEP 4: Make PREDICTIONS and EVALUATE
# ================================================================

print("=" * 60)
print("STEP 4: Making PREDICTIONS on unseen data")
print("=" * 60)

# Predict prices for the test houses
y_pred = model.predict(X_test)

# Show the first 5 predictions vs actual values
print(f"{'House':<8} {'Actual Price':<16} {'Predicted':<16} {'Error':<10}")
print("-" * 50)
for i in range(min(5, len(X_test))):
    actual = y_test[i]
    predicted = y_pred[i]
    error = abs(actual - predicted)
    print(f"{i+1:<8} ${actual:<8.2f}k      ${predicted:<8.2f}k      ${error:<.2f}k")

# ================================================================
# STEP 5: Measure ACCURACY
# ================================================================

print()
print("=" * 60)
print("STEP 5: Measuring accuracy with metrics")
print("=" * 60)

# METRIC 1: Mean Absolute Error (MAE)
# How wrong are we on average? (in same units as price)
mae = mean_absolute_error(y_test, y_pred)
print(f"📏 Mean Absolute Error (MAE): ${mae:.2f}k")
print(f"   → On average, predictions are off by ${mae:.2f}k")
print()

# METRIC 2: R² Score (0 to 1)
# How much of the pattern did the model capture?
#   0 = model learned nothing
#   1 = model learned everything perfectly
r2 = r2_score(y_test, y_pred)
print(f"📈 R² Score: {r2:.3f}")
print(f"   → 0 = model is useless,  1 = model is perfect")
print(f"   → Our model scored {r2:.3f}, which means it learned the pattern well!")
print()

# ================================================================
# STEP 6: Real-world usage — predict a NEW house
# ================================================================

print("=" * 60)
print("STEP 6: Using the model to predict a new house!")
print("=" * 60)

new_house_size = [[85]]  # A new 85 sq meter house
predicted_price = model.predict(new_house_size)

print(f"🏠 New house size: {new_house_size[0][0]} sq m")
print(f"💰 Predicted price: ${predicted_price[0]:.2f}k")
print()

# ================================================================
# SUMMARY — What you just learned
# ================================================================
print("=" * 60)
print("🎉 SUMMARY: Machine Learning in 5 Steps")
print("=" * 60)
print("""
  1️⃣  DATASET    — Collect examples (features + labels)
  2️⃣  SPLIT      — Divide into training data & testing data
  3️⃣  TRAIN      — Let the model find patterns in the training data
  4️⃣  PREDICT    — Use the model to guess answers for new data
  5️⃣  EVALUATE   — Check how accurate the predictions are

  KEY INSIGHT: The model never saw the test data during training!
  If it predicts well on unseen data → it ACTUALLY learned the pattern.
  If it only memorized the training data → it will FAIL on new data.
""")