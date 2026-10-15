#1. The accumulator pattern is basically just keeping a running total as you go through a list. 
#   - Step 1: Set up a variable outside the loop to start at 0 (like total = 0). This matters because Python needs the variable to exist before you can add stuff to it.
#   - Step 2: Loop through the list and add each item to your total (like total += sale). This matters so every single number actually gets added in.
#   - Step 3: Print or use the final result after the loop ends. This matters because if you put it inside the loop, it would print every single intermediate step instead of just the final answer.

#2. The while loop took more code than the for loop because I had to set up an index variable (i = 0), check the condition (i < len(sales)), and manually add i += 1 at the end. The for loop does all that automatically. 
#   - For loop: super simple, less code, hard to mess up. 
#   - While loop: gives you more control if you don't know how many items you're looping through, but easy to accidentally cause an infinite loop.
#   In production, I would definitely use the for loop because it's cleaner and way less prone to simple mistakes.

#3.  For a real estate project evaluating single-family home rental comps in Lake Nona, 
#    the dataset would contain dictionaries with details like rent, square footage, bedrooms, etc., 
#    such as [{'rent': 2800, 'sqft': 1800}, {'rent': 3200, 'sqft': 2200}, {'rent': 2950, 'sqft': 1950}]. 
#    I would use a loop to accumulate total rent, total square footage, and count the home comps evaluated. 
#    At the end, I'd calculate and print the total market rent, total square footage, and average rent per square foot to project potential rental yield.

# --- Shared Data ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]


# --- Exercise 1 ---
total = 0       
for sale in sales:
    total += sale   
print(f"Total: ${total}")


# --- Exercise 2 ---
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")


# --- Exercise 3 ---
largest = 0
for sale in sales:
    if sale > largest:
        largest = sale
print(f"Largest sale: ${largest}")


# --- Exercise 4 ---
count_over_100 = 0
total_over_100 = 0

for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")


# --- Exercise 5 ---
for sale in sales:
    if sale <= 100:
        continue
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    print(f"${sale}")


# --- Exercise 6 ---
total_while = 0
i = 0            
while i < len(sales):
    total_while += sales[i]
    i += 1

print(f"Total (while loop): ${total_while}")


# --- Exercise 7 ---
for sale in sales:
    if sale >= 200:
        discount_rate = 0.10
        discount_pct = "10%"
    elif sale >= 100:
        discount_rate = 0.05
        discount_pct = "5%"
    else:
        discount_rate = 0.00
        discount_pct = "0%"
    
    discounted_price = sale * (1 - discount_rate)
    print(f"${sale:<3} -> {discount_pct:>3} discount -> ${discounted_price:.2f}")