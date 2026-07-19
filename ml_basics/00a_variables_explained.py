"""
===============================================================
VARIABLES — Explained Like You're 5 Years Old
===============================================================
No Machine Learning. No formulas. Just variables.

Run this:   python 00a_variables_explained.py
"""

print("=" * 60)
print("WHAT IS A VARIABLE?")
print("=" * 60)
print()

# ================================================================
# ANALOGY: Variables are like BOXES with labels
# ================================================================

print("""Imagine you have a BOX.
You write a LABEL on the box: "age"
Then you put a NUMBER inside the box: 25

In Python, you write:
   age = 25

That's it! That's a variable!
""")

# ================================================================
# DEMO 1: Creating variables
# ================================================================
print("=" * 60)
print("DEMO 1: Creating variables")
print("=" * 60)

# I'm creating variables. Watch carefully:
my_age = 25            # Box labeled "my_age" → contains 25
my_name = "Juan"       # Box labeled "my_name" → contains "Juan"
my_height = 5.9        # Box labeled "my_height" → contains 5.9

print("I just created 3 variables:")
print(f"   my_age    = {my_age}     (a number)")
print(f"   my_name   = {my_name}   (text)")
print(f"   my_height = {my_height}   (a decimal number)")
print()

# ================================================================
# DEMO 2: Using variables
# ================================================================
print("=" * 60)
print("DEMO 2: Using variables — what's inside?")
print("=" * 60)

# When I write the variable name, Python shows what's inside
print(f"Inside the box 'my_age' is: {my_age}")
print()

# I can do math with variables
print(f"Next year, I'll be: {my_age + 1}")
print(f"My age in dog years: {my_age * 7}")
print()

# ================================================================
# DEMO 3: Changing what's inside a variable
# ================================================================
print("=" * 60)
print("DEMO 3: Changing the value")
print("=" * 60)

pocket_money = 10
print(f"I have ${pocket_money}")

pocket_money = 20      # I changed the value!
print(f"I got more! Now I have ${pocket_money}")

pocket_money = pocket_money - 5   # I spent 5
print(f"I spent $5. Now I have ${pocket_money}")
print()

# ================================================================
# DEMO 4: Two variables together
# ================================================================
print("=" * 60)
print("DEMO 4: Two variables can interact")
print("=" * 60)

apples = 5
oranges = 3
total_fruits = apples + oranges

print(f"I have {apples} apples")
print(f"I have {oranges} oranges")
print(f"Total fruits = {apples} + {oranges} = {total_fruits}")
print()

# ================================================================
# DEMO 5: How Python sees variables
# ================================================================
print("=" * 60)
print("DEMO 5: Think of it this way...")
print("=" * 60)
print()
print("""  In your brain:              In Python:
  
  ┌───────────────┐           ┌───────────────┐
  │ "price"       │           │ price = 350   │
  │ ──────────    │           │               │
  │   350         │           │   350         │
  └───────────────┘           └───────────────┘
  
  You say: "price"             Python stores 350
  You think: 350               in memory
""")

# ================================================================
# DEMO 6: This is ALL a variable is
# ================================================================
print("=" * 60)
print("DEMO 6: A variable is just...")
print("=" * 60)
print()
print("""  variable_name = value
  
  ╔══════════════╗
  ║  Left side   ║   The LABEL (name of the box)
  ║  "age"       ║
  ╚══════════════╝
        =
  ╔══════════════╗
  ║  Right side  ║   The VALUE (what's inside the box)
  ║  25          ║
  ╚══════════════╝
""")

# ================================================================
# Now let's connect to ML
# ================================================================
print("=" * 60)
print("BONUS: How this connects to Machine Learning")
print("=" * 60)
print()
print("""In our ML script, we have:

  X = [30, 50, 100, 150, 200]    ← House sizes
  y = [140, 200, 350, 500, 650]  ← House prices

  "X" is a variable. "y" is a variable.
  They're just BOXES containing LISTS of numbers.
  
  Nothing magical. Just boxes with labels!
""")

X = [30, 50, 100, 150, 200]
y = [140, 200, 350, 500, 650]

print(f"  Inside box X: {X}")
print(f"  Inside box y: {y}")
print()
print("✅ Next: PART 2 (the pattern/formula)")