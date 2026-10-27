#Reflection Questions
#1. The most suprising thing is how they are easily able to combine different data types and add and remove elements quickly or automatically with functions. 
#2. In my previous real estate development internship I manually had to go through rental comparisons to filter out data. Using a Python list I could sort through this data more efficiently. 

# --- Exercise 1 ---
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print("Amount of Inventory: ", len(inventory))

# --- Exercise 2 ---
print("--- Exercise 2 ---")
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])

# --- Exercise 3 ---
print("--- Exercise 3 ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# --- Exercise 4 ---
print("--- Exercise 4 ---")
print(inventory)
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison
print("--- Exercise 5 ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples are immutable and cannot be modified. This is useful for fixed data like coordinates because it protects against accidental changes.")

print(coords)

# --- Exercise 6 ---
print("--- Exercise 6 ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

# --- Exercise 7 ---
print("--- Exercise 7 ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price *.9, 2))
print(prices)
print(discounted)

# --- Exercise 8 ---
print("--- Exercise 8 ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
avg_high_sales = sum(high_sales) / len(high_sales)
print(f"Average: {avg_high_sales:.2f}")