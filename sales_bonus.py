"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    if sales < 1000
        bonus =  sales * 0.1
    else
        bonus = sales * 0.15
        display your bonus is {bonus:.0f}
        get sales
"""

low_bonus = 0.1
high_bonus = 0.15
sales_limit = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < sales_limit:
        bonus = sales * low_bonus
    else:
        bonus = sales * high_bonus
    print(f"Your bonus is {bonus:.0f}")
    sales = float(input("Enter sales: $"))
