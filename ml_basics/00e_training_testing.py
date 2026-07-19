"""
===============================================================
TRAINING vs TESTING — The Most Important ML Concept
===============================================================
Run this:   python ml_basics/00e_training_testing.py
"""

print("=" * 60)
print("TRAINING vs TESTING — Why we split the data")
print("=" * 60)
print()

# ================================================================
# ANALOGY: Studying for an exam
# ================================================================
print("=" * 60)
print("ANALOGY: Studying for a Math Exam")
print("=" * 60)
print()

print("""  Imagine you have a math exam tomorrow.

  You have 20 practice problems.
  ─────────────────────────────────────

  BAD way to study:
  • Study all 20 problems
  • Then take a test with the SAME 20 problems
  • You get 100%! But did you actually LEARN?
  • No! You just MEMORIZED the answers.

  GOOD way to study:
  • Study 16 problems (TRAINING)
  • Take a test with 4 NEW problems (TESTING)
  • If you get them right → you actually LEARNED the pattern!
  • If you get them wrong → you just memorized, didn't learn
""")

print("  ┌─────────────────────────────────────────────┐")
print("  │  TRAINING set (80%):  Used to LEARN          │")
print("  │  TESTING set  (20%):  Used to CHECK learning │")
print("  └─────────────────────────────────────────────┘")
print()

# ================================================================
# DEMO: What happens if we DON'T split?
# ================================================================
print("=" * 60)
print("DEMO: What happens if we DON'T split?")
print("=" * 60)
print()

print("""  Let's say we have 5 houses:
  
  Size:   [30,  50,  100,  150,  200]
  Price:  [140, 200, 350,  500,  650]

  If we TRAIN on ALL 5 and TEST on ALL 5:
  → The model already SAW the answers!
  → It looks like it's perfect, but it might be USELESS
  → for new houses it hasn't seen.
""")

print("  This is called OVERFITTING — memorizing instead of learning.")
print()

# ================================================================
# DEMO: The actual split
# ================================================================
print("=" * 60)
print("DEMO: How the split works in our script")
print("=" * 60)
print()

from sklearn.model_selection import train_test_split
import numpy as np

# Our 100 houses
np.random.seed(42)
X = np.random.uniform(30, 200, 100).reshape(-1, 1)
noise = np.random.normal(0, 15, 100)
y = (X.flatten() * 3 + 50) + noise

# Split into 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"  Total houses:     {len(X)}")
print(f"  Training houses:  {len(X_train)}  (80%)  ← Model LEARNS from these")
print(f"  Testing houses:   {len(X_test)}   (20%)  ← We HIDE these to test later")
print()

print("  The testing houses are like the exam questions.")
print("  The model has NEVER seen them before.")
print("  If it predicts them well → it truly learned the pattern!")
print()

# ================================================================
# KEY INSIGHT
# ================================================================
print("=" * 60)
print("📌 WHY THIS MATTERS")
print("=" * 60)
print()


