"""
===============================================================
THE PATTERN (FORMULA) — How ML "Learns"
===============================================================
Run this:   python ml_basics/00c_pattern_explained.py
"""

print("=" * 60)
print("THE BIG IDEA: What is a 'pattern'?")
print("=" * 60)
print()

print("""Imagine you're a real estate agent.
You notice something: BIGGER houses cost MORE money.

That's a PATTERN. Let's see it in numbers.
""")

# ================================================================
# DEMO 1: The pattern is just a formula
# ================================================================
print("=" * 60)
print("DEMO 1: The pattern as a formula")
print("=" * 60)
print()

print("  Formula:  price = size × 3 + 50")
print()
print("  Let's test it:")
print("  ─────────────────────────────────────")
for size in [30, 50, 100, 150, 200]:
    price = size * 3 + 50
    print(f"  Size {size:>3} sq m  →  {size} × 3 + 50  =  ${price}k")
print("  ─────────────────────────────────────")
print()

# ================================================================
# DEMO 2: The formula has TWO important numbers
# ================================================================
print("=" * 60)
print("DEMO 2: The two numbers in the formula")
print("=" * 60)
print()

print("""  price = size × 3 + 50
                   ↑       ↑
                   │       └── INTERCEPT (starting price)
                   │
                   └── SLOPE (how much price increases per sq meter)
""")

print("""  SLOPE = 3     → Each extra sq meter adds $3k to the price
  INTERCEPT = 50 → Even a 0 sq meter house costs $50k (land value)
""")
print()

# ================================================================
# DEMO 3: What if the numbers were different?
# ================================================================
print("=" * 60)
print("DEMO 3: Different patterns = different formulas")
print("=" * 60)
print()

print("""  If houses were CHEAPER:  price = size × 2 + 30
  If houses were EXPENSIVE: price = size × 5 + 100
  If land was FREE:         price = size × 3 + 0
""")

print("  Compare for a 100 sq meter house:")
print(f"    Cheap:    100 × 2 + 30   = $230k")
print(f"    Normal:   100 × 3 + 50   = $350k")
print(f"    Expensive: 100 × 5 + 100  = $600k")
print()

# ================================================================
# DEMO 4: THIS is what ML does
# ================================================================
print("=" * 60)
print("DEMO 4: What Machine Learning actually does")
print("=" * 60)
print()

print("""  You give the computer:
     ┌─────────────────────────────┐
     │  Size → Price               │
     │  30   → $140k               │
     │  50   → $200k               │
     │  100  → $350k               │
     │  150  → $500k               │
     │  200  → $650k               │
     └─────────────────────────────┘

  The computer figures out:
     ┌─────────────────────────────┐
     │  The pattern is:            │
     │  price = size × 3 + 50      │
     └─────────────────────────────┘

  Then you ask: "What about a 75 sq meter house?"
  The computer answers: 75 × 3 + 50 = $275k
""")

# ================================================================
# DEMO 5: Let's actually DO it with code
# ================================================================
print("=" * 60)
print("DEMO 5: Let's find the pattern with code!")
print("=" * 60)
print()

# Our data
sizes = [30, 50, 100, 150, 200]
prices = [140, 200, 350, 500, 650]

print("  Our dataset:")
print(f"  Sizes:  {sizes}")
print(f"  Prices: {prices}")
print()

# Let's GUESS the pattern
print("  Can YOU see the pattern?")
print("  Hint: Try size × 3 + 50")
print()

# Test our guess
test_size = 75
guess_price = test_size * 3 + 50
print(f"  If size = {test_size} sq m")
print(f"  Using pattern: {test_size} × 3 + 50 = ${guess_price}k")
print()

# ================================================================
# SUMMARY
# ================================================================
print("=" * 60)
print("📌 SUMMARY: The Pattern")
print("=" * 60)
print("""
  • A pattern is just a FORMULA connecting two things
  • price = size × 3 + 50  is a pattern
  • The formula has two numbers: SLOPE and INTERCEPT
  • ML finds these two numbers automatically
  • Once found, you can PREDICT new values

  NEXT: How does ML find these numbers?
  → By looking at EXAMPLES (training data)
""")