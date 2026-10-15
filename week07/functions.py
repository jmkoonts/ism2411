#Self Assessment Questions
#1. In exercise 5 the first bug spotted was the missing colon on the second for loop line which was caught by the python syntax error traceback which shows it checks syntax issues before logic errors
#2. The apply_discount(price, tier) takes a number for the price and a string tier to return the adjusted price after applying the discount that corresponded to the tier level. This is easy for someone to read without explanation because the wording and titiles are self explanatory
#3. AI was used to assit todays lab for helping to find the bugs to repiar the script and confirming the code completed all that was asked. I think it helps me better understand things im confused on but it makes it a bit harder to retain the information compared to learning it slower. 

# --- Exercise 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

#Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")


# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale  # Fixed: added accumulator assignment
print(f"Total: ${total}")

count = 0
for sale in sales:  # Fixed: added missing colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # Fixed: changed <= to < to avoid index out of range
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100 # global x

def double_it():
    x = 999 # local x
    return x *2

print(x)
print(double_it())
print(x)
