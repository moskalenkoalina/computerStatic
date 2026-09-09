import numpy as np
from scipy.stats import norm, expon

# ----- частина 1 -----
print("----- Частина 1 -----")
probability = norm.cdf(12, loc=10, scale=3)
print("P(X <= 12):", probability)


# ----- частина 2 -----
# P(X <= x) = 0.95
print("\n----- Частина 2 -----")
x = norm.ppf(0.95)

print("x:", x)


# ----- частина 3 -----
print("\n----- Частина 3 -----")

np.random.seed(42)

# Exp(lambda = 2)
sample = expon.rvs(scale=1/2, size=1000)

sample_mean = np.mean(sample)
theoretical_mean = 0.5

print("Вибіркове середнє:", sample_mean)
print("Теоретичне середнє:", theoretical_mean)