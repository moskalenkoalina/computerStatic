import numpy as np
#Прший пункт
print("-----частина 1------")
x = np.array([2, 4, 6, 8, 10])

mean = np.mean(x)
print("Середнє:", mean)
variance = np.var(x, ddof=1)
print("Вибіркова дисперсія:", variance)
std = np.std(x, ddof=1)
print("Стандартне відхилення:", std)


#Другий пункт
print("-----частина 2------")

x = np.random.normal(loc=5, scale=2, size=1000)

sample_mean = np.mean(x)
print("Вибіркове середнє:", sample_mean)
sample_std = np.std(x, ddof=1)
print("Вибіркове стандартне відхилення:", sample_std)

print("\nТеоретичне середнє:", 5)
print("Теоретичне стандартне відхилення:", 2)

#Третій пункт
print("-----частина 3------")


np.random.seed(42)

n = 100
p = 0.3

coin = np.random.binomial(1, p, n)

successes = np.sum(coin)
p_estimate = np.mean(coin)

print("Кількість успіхів:", successes)
print("Оцінка p:", p_estimate)
