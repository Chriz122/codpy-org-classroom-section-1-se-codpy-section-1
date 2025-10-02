import random

# Constant settings
NUM_POINTS = 1000000
AREA_FACTOR = 4

inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(NUM_POINTS):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1**2:
        inside_circle += 1

# Estimate pi based on the number of points inside the circle
pi = (inside_circle / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {pi}")