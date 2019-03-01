import numpy as np
import matplotlib.pyplot as plt

# Topics Covered:
# 1. Comparison Operators as uFuncs
# 2. Working with Boolean Arrays: counting entries, boolean operators, 
# boolean arrays as masks

# 1. Comparison Operators as uFuncs
x = np.arange(1,8)

print("Greater than 3", x>3)
print("Less than 3", x<3)
print(">= 3", x>=3)
print("<=3", x<=3)
print("!=", x!=3)
print("=", x==3)

# Compound statements:
print("Compount test:", (2*x) == (x**2) )

# Comparison on array
M = np.arange(16).reshape((4,4))

print("div by 2:")
print(M%2==0)

# Working with Boolean Arrays 
rng = np.random.RandomState(0)
M2 = rng.randint(10, size=(4,5))

# Greater than or equal to 8
print("<=8 matrix:", M2>=8)

# Counting entries
# First, nonzero:
num_less6_fn1 = np.count_nonzero(M2<6)
# Find entries less than 5
num_less6 = np.sum(M2<5)

# How many values less than 5 in each row and column
row_less5 = np.sum(M2<5, axis=1)
col_less5 = np.sum(M2<5,axis=0)

all_less5 = np.all(M2<5)
any_less3_row = np.any(M2<3, axis=1)
all_less3_row = np.all(M2<3, axis=1)


# Boolean Arrays as Masks
M2[M2>8] # subarray with all values greater than 9
M2[(M2>4) & (M2<8)] # subarray with all values between 4 and 7 inclusive