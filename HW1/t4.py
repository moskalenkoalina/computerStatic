import numpy as np
import matplotlib.pyplot as plt

# ----- Частина 1 -----
print("----- Частина 1 -----")

x = np.linspace(-5, 5, 100)
y = x ** 2

plt.figure()
plt.plot(x, y)
plt.title("Графік функції y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


# ----- Частина 2 -----
print("\n----- Частина 2 -----")

np.random.seed(42)
data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30)
plt.title("Гістограма N(0, 1)")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.grid()
plt.show()


# ----- Частина 3 -----
print("\n----- Частина 3 -----")

x = [1, 2, 3, 4, 5]
y = [2, 5, 5, 8, 11]

plt.figure()
plt.scatter(x, y)
plt.title("Діаграма розсіювання")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()