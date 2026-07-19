"""
===============================================================
THE ABSOLUTE BASICS — No ML yet, just plain Python examples
===============================================================
Run each section one at a time.
"""

# ================================================================
# PART 1: What is a VARIABLE? (a named box that holds a value)
# ================================================================
print("=" * 60)
print("PART 1: Variables — just named boxes")
print("=" * 60)

# Think of a variable as a labeled box where you store something
house_size = 100       # A box labeled "house_size" holding the number 100
house_price = 350      # A box labeled "house_price" holding the number 350

print(f"house_size = {house_size}")
print(f"house_price = {house_price}")
print()

# ================================================================
# PART 2: The RELATIONSHIP between variables (simple math)
# ================================================================
print("=" * 60)
print("PART 2: Finding patterns — the relationship between numbers")
print("=" * 60)

# Let's say price is ALWAYS 3 times the size, plus 50
# This is a PATTERN (a formula)
size = 100
price = size * 3 + 50   # 100 * 3 + 50 = 350

print(f"If house size = {size} sq meters")
print(f"Using formula: price = size × 3 + 50")
print(f"Then price = {size} × 3 + 50 = {price}")
print()

# Let's try different sizes:
for size in [30, 50, 100, 150, 200]:
    price = size * 3 + 50
    print(f"  Size {size:>3} sq m → Price ${price}k")

print()
print("This formula (size × 3 + 50) is called the PATTERN.")
print("Machine Learning tries to find this pattern automatically.")
print()

# ================================================================
# PART 3: What is a DATASET? — just a table of numbers
# ================================================================
print("=" * 60)
print("PART 3: What is a DATASET?")
print("=" * 60)
print()
print("""A dataset is just a TABLE with two columns:

   FEATURE (X)        LABEL (y)
   ───────────        ──────────
   What we know       What we want to predict
   ─────────────────────────────────────
   House size         House price
   30 sq m            $140k
   50 sq m            $200k
   100 sq m           $350k
   150 sq m           $500k
   200 sq m           $650k

   X = FEATURES (the inputs, what you already know)
   y = LABELS   (the answers, what you want to predict)
""")
print()

# ================================================================
# PART 4: Let's CREATE a fake dataset (like in ML script 1)
# ================================================================
print("=" * 60)
print("PART 4: Creating our own simple dataset")
print("=" * 60)
print()

# A list of house sizes (5 houses)
sizes = [30, 50, 100, 150, 200]
print(f"Our FEATURES (X): {sizes}")
print(f"   → These are the house sizes we KNOW")

# The prices (following our formula: size × 3 + 50)
prices = [size * 3 + 50 for size in sizes]
print(f"Our LABELS   (y): {prices}")
print(f"   → These are the prices we WANT TO PREDICT")
print()

print("Let's look at houses side by side:")
print(f"  {'Size':>6} → {'Price':>6}")
print(f"  {'─────':>6}   {'─────':>6}")
for size, price in zip(sizes, prices):
    print(f"  {size:>6} → ${price:>5}k")
print()

# ================================================================
# PART 5: The ML question
# ================================================================
print("=" * 60)
print("PART 5: The Machine Learning QUESTION")
print("=" * 60)
print()
print("""Now imagine this:

  1. I show you a table of 5 houses (size → price)
  2. You see the pattern: price = size × 3 + 50
  3. Then I ask: "What would a 75 sq meter house cost?"

  You would answer: 75 × 3 + 50 = $275k ✓

  THAT is what Machine Learning does!
  
  But instead of a human figuring it out,
  the COMPUTER figures out the pattern automatically.
""")
print()

# ================================================================
# PART 6: REAL vs PERFECT data
# ================================================================
print("=" * 60)
print("PART 6: Real data has NOISE (random fuzz)")
print("=" * 60)
print()

import random
random.seed(42)

print("""In the real world, data is never perfect.
Even if the general pattern is price = size × 3 + 50,
real prices might be a little higher or lower.

For example:""")
print()

for size in [30, 50, 100, 150, 200]:
    perfect_price = size * 3 + 50
    noise = random.randint(-20, 20)  # Random fuzz
    real_price = perfect_price + noise
    print(f"  Size {size:>3} → Perfect: ${perfect_price}k,  Real: ${real_price}k  (noise: {noise})")

print()
print("""  The RANDOM FUZZ (noise) is what makes ML interesting!
  If data were perfectly clean, no ML would be needed — 
  you could just use a calculator.

  ML's job: find the PATTERN (size × 3 + 50) even when 
  the data has NOISE (random fuzz).
""")

print("=" * 60)
print("✅ NOW you're ready for 01_intro_to_ml.py!")
print("=" * 60)