"""
===============================================================
TRY IT YOURSELF — Practice Variables
===============================================================
EDIT the lines marked with 👉 and run:
   python ml_basics/00b_try_variables_yourself.py
"""

print("=" * 60)
print("YOUR TURN! Try changing the numbers below.")
print("=" * 60)

# ================================================================
# EXERCISE 1: Create your own variables
# ================================================================
print()
print("--- EXERCISE 1: Create your own variables ---")
print()

# 👉 CHANGE the numbers below to anything you want
my_favorite_number = 7        # Change 7 to your favorite number
my_age = 25                   # Change 25 to your age
money_in_pocket = 100         # Change 100 to however much money you have

# (Don't change these lines — they just show what you did)
print(f"Your favorite number: {my_favorite_number}")
print(f"Your age: {my_age}")
print(f"Money in pocket: ${money_in_pocket}")
print()

# ================================================================
# EXERCISE 2: Do math with variables
# ================================================================
print("--- EXERCISE 2: Do math with variables ---")
print()

# 👉 Change the num1 and num2 to any numbers you want
num1 = 10
num2 = 5

# These lines will calculate using whatever numbers you chose
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} × {num2} = {product}")
print()

# ================================================================
# EXERCISE 3: Change a variable
# ================================================================
print("--- EXERCISE 3: Change what's inside a variable ---")
print()

# 👉 Start with any number
my_score = 10
print(f"Starting score: {my_score}")

# 👉 Change this number. Try adding to it: my_score = my_score + 50
my_score = 10    # ← CHANGE THIS LINE

print(f"New score: {my_score}")
print()

# ================================================================
# EXERCISE 4: Create a simple dataset (ML connection!)
# ================================================================
print("--- EXERCISE 4: Make your own mini ML dataset ---")
print()

# 👉 Change these house sizes (list of numbers)
X = [30, 50, 100, 150, 200]

# 👉 Change these prices to match however you want
#    (Try: small house = low price, big house = high price)
y = [140, 200, 350, 500, 650]

print("Your dataset:")
print(f"  FEATURES (house sizes): {X}")
print(f"  LABELS   (house prices): {y}")
print()

print("✅ Now try changing the numbers and running again!")
print("   python ml_basics/00b_try_variables_yourself.py")