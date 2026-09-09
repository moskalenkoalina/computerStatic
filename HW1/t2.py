import pandas as pd

# 1. Завантаження data.csv
df = pd.read_csv("data.csv")

print("----- Частина 1 -----")
print("Перші 5 рядків:")
print(df.head())

print("\nКількість рядків:", df.shape[0])
print("Кількість колонок:", df.shape[1])


# 2. Середні значення total та special_proposition
print("\n----- Частина 2 -----")

mean_total = df["total"].mean()
mean_special = df["special_proposition"].mean()

print("Середнє total:", mean_total)
print("Середнє special_proposition:", mean_special)


# 3. Створення змінної other
print("\n----- Частина 3 -----")

df["other"] = df["total"] - df["special_proposition"]

print("Стовпець other:")
print(df["other"])

mean_other = df["other"].mean()
print("\nСереднє other:", mean_other)