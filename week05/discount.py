#Self Assessment Reflection Anwsers
#1. When an order total is 350, the script first checks if it is greater than or equal to 500, which is false. Then it checks if it is greater than or equal to 200, which is true. It applies the 10% discount and skips the rest of the checks. 
#2. An if/elif chain stops checking as soon as it finds a true condition. Two separate if statements would both run independently, which could overwrite variables or cause conflicting logic.
#3. We run into tiered logic with tax brackets, shipping fees, ect. Knowing Python makes it easier to see that these are just sequential threshold checks running behind the scenes. 

# --- Exercise 1 ---
total = float(input("Enter cart total: $"))

# Add your if/elif/else here

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

# discount = 0  # replace with correct logic
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")

# --- Exercise 2 ---
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
# print(f"Status: {status}")

# --- Exercise 3 ---
region = "South" # S is capitalized

extra_discount = 0  # default value
if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional; 2% off")

final = total * (1 - discount - extra_discount)
print(f"Final total: ${final:.2f}")

# --- Exercise 4 ---
customer_type = "wholesale" 
if region == "South" and total >= 100 and customer_type == "wholesale":
    extra_discount = 0.03

final = total * (1 - discount - extra_discount)
print(f"Final total: ${final:.2f}")

# --- Exercise 5 ---
amount = 0

if amount <= 0:
    print ("SUSPISCIOUS")
elif amount < 10000:
    print ("NORMAL")
else:
    print ("LARGE -- REPORT REQUIRED")

# --- Exercise 6 ---

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False #boolean

vip_upgrade = True
if total_spent_this_year > 2000 and orders_this_year > 10 and not has_outstanding_balance:
    print("VIP")
else:
    vip_upgrade = False
    print("Not VIP")

random = range(10)
print(random)