"""
===============================================================
SLOPE vs INTERCEPT — Explained with Everyday Life
===============================================================
Run this:   python ml_basics/00d_slope_intercept.py
"""

print("=" * 60)
print("SLOPE vs INTERCEPT — The Easiest Explanation")
print("=" * 60)
print()

# ================================================================
# ANALOGY 1: A RAMP
# ================================================================
print("=" * 60)
print("ANALOGY 1: Think of a RAMP (like for wheelchairs)")
print("=" * 60)
print()

print("""  Imagine a ramp going up from the ground to a door.

  ┌────────────────────────────────────────┐
  │                                        │
  │   ┌─────────────────────────┐          │
  │   │                         │   DOOR   │
  │   │                         │   🚪     │
  │   │    RAMP                 │          │
  │   │                         │          │
  │   └─────────────────────────┘          │
  │   ↑                       ↑            │
  │  START                  END            │
  └────────────────────────────────────────┘

  SLOPE     = How STEEP the ramp is
  INTERCEPT = How HIGH the starting point is off the ground

  If slope = 0 → flat ground (no incline)
  If slope = big → very steep ramp
  If intercept = 0 → starts at ground level
  If intercept = 10 → starts 10 feet in the air!
""")
print()

# ================================================================
# ANALOGY 2: A TAXI RIDE
# ================================================================
print("=" * 60)
print("ANALOGY 2: Think of a TAXI RIDE")
print("=" * 60)
print()

print("""  You take a taxi. The fare works like this:

  INTERCEPT = $3  ← The BASE FARE (just for getting in)
  SLOPE     = $2 per kilometer ← How much it adds per km

  Total fare = $3 (base) + $2 × (kilometers traveled)

  If you travel 0 km:    $3 + $2 × 0  = $3   (just the base fare)
  If you travel 5 km:    $3 + $2 × 5  = $13
  If you travel 10 km:   $3 + $2 × 10 = $23
""")

print("  Now let's connect this to HOUSES:")
print()
print("""  INTERCEPT = $50k  ← The BASE PRICE (land value, permits, etc.)
                               Even a 0 sq meter "house" costs $50k

  SLOPE     = $3k per sq meter ← Price INCREASE for each extra sq meter

  House price = $50k (base) + $3k × (size in sq meters)
""")
print()

# ================================================================
# DEMO: See how changing SLOPE changes the line
# ================================================================
print("=" * 60)
print("DEMO: What happens when SLOPE changes?")
print("=" * 60)
print()

print("  Same INTERCEPT (50), different SLOPES:")
print()

for size in [0, 50, 100, 150]:
    price_slope_1 = 50 + 1 * size   # slope = 1
    price_slope_3 = 50 + 3 * size   # slope = 3
    price_slope_5 = 50 + 5 * size   # slope = 5
    
    print(f"  Size {size:>3}:  Slope=1 → ${price_slope_1:>4}k  |  Slope=3 → ${price_slope_3:>4}k  |  Slope=5 → ${price_slope_5:>4}k")

print()
print("  Bigger SLOPE = price goes up FASTER as size increases")
print()

# ================================================================
# DEMO: See how changing INTERCEPT changes the line
# ================================================================
print("=" * 60)
print("DEMO: What happens when INTERCEPT changes?")
print("=" * 60)
print()

print("  Same SLOPE (3), different INTERCEPTS:")
print()

for size in [0, 50, 100, 150]:
    price_int_0  = 0   + 3 * size   # intercept = 0
    price_int_50 = 50  + 3 * size   # intercept = 50
    price_int_100 = 100 + 3 * size  # intercept = 100
    
    print(f"  Size {size:>3}:  Int=0  → ${price_int_0:>4}k  |  Int=50 → ${price_int_50:>4}k  |  Int=100 → ${price_int_100:>4}k")

print()
print("  Bigger INTERCEPT = ALL prices are higher, regardless of size")
print()

# ================================================================
# VISUAL: ASCII graph
# ================================================================
print("=" * 60)
print("VISUAL: See SLOPE as steepness")
print("=" * 60)
print()

print("""  Think of a GRAPH:

  Price ↑
    650 │                                    ●
        │                                 ●
    500 │                            ●
        │                         ●
    350 │                    ●
        │                 ●
    200 │           ●
        │        ●
    140 │   ●
     50 ├──●─────────────────────────────────→ Size
        │   30  50   100   150   200
  
  The LINE shows the pattern.
  SLOPE = how TILTED the line is (steep vs flat)
  INTERCEPT = where the line hits the left side (at size=0)
""")

# ================================================================
# THE ML CONNECTION
# ================================================================
print("=" * 60)
print("HOW THIS CONNECTS TO MACHINE LEARNING")
print("=" * 60)
print()

print("""  In 01_intro_to_ml.py, the model learned:

  TRUE pattern:    price = size × 3 + 50
  LEARNED pattern: price = size × 2.96 + 53.21

  SLOPE learned:     2.96   (true is 3.0)
  INTERCEPT learned: 53.21  (true is 50)

  The model found these two numbers by looking at the data!
  It didn't know the true formula — it DISCOVERED it.
  
  Once it has these 2 numbers, it can PREDICT any house price.
""")

print("=" * 60)
print("✅ KEY TAKEAWAY")
print("=" * 60)
print("""
  SLOPE     = How fast the output changes when input changes
              ("Each square meter adds $3k to the price")

  INTERCEPT = The starting value when input is zero
              ("Even a tiny house costs $50k for the land")
  
  Together they form the FORMULA:
     price = SLOPE × size + INTERCEPT

  ML just finds these 2 numbers from data!
""")