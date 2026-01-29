#Financial Python program for businesses who wish to track assets, revenues and expenses

print("This is a simple program using Python to help businesses determine their assets, revenues and expenses")

print("This program will begin by asking you to provide various assets")

asset_source1 = input("Please enter the name of your first asset source:")
asset_source2 = input("Please enter the name of your second asset source:")
asset_source3 = input("Please enter the name of your third asset source:")

asset_amount1 = float(input("Please enter the amount of your first asset:"))
asset_amount2 = float(input("Please enter the amount of your second asset:"))
asset_amount3 = float(input("Please enter the amount of your third asset:"))

print("Next, you will be asked to provide various sources of revenue, coupled with their amounts")

rev_source1 = input("Please enter the name of your first source of revenue:")
rev_source2 = input("Please enter the name of your second source of revenue: ")
rev_source3 = input("Please enter the name of your third source of revenue: ")

rev_amount1 = float(input("Please enter the amount of revenue from your first source:"))
rev_amount2 = float(input("Please enter the amount of revenue from your second source:"))
rev_amount3 = float(input("Please enter the amount of revenue from your third source:"))

print("Finally, you will be asked to provide various expenses")

exp_source1 = input("Please enter the name of your first expense: ")
exp_source2 = input("Please enter the name of your second expense: ")
exp_source3 = input("Please enter the name of your third expense: ")

exp_amount1 = float(input("Please enter the amount of expense from your first source:"))
exp_amount2 = float(input("Please enter the amount of expense from your second source:"))
exp_amount3 = float(input("Please enter the amount of expense from your third source:"))

#Allocation of assets, revenue and expenses (contribution analysis)

print("----- Financial Summary -----")

total_asset_amount = asset_amount1 + asset_amount2 + asset_amount3

alc_ast1 = round((asset_amount1 / total_asset_amount) * 100, 2)
alc_ast2 = round((asset_amount2 / total_asset_amount) * 100, 2)
alc_ast3 = round((asset_amount3 / total_asset_amount) * 100, 2)

print(f'Your total assets amount to ${total_asset_amount}')
print(f'Total assets for {asset_source1}: ${asset_amount1}, Allocation: {alc_ast1}%')
print(f'Total assets for {asset_source2}: ${asset_amount2}, Allocation: {alc_ast2}%')
print(f'Total assets for {asset_source3}: ${asset_amount3}, Allocation: {alc_ast3}%')

total_rev_amount = rev_amount1 + rev_amount2 + rev_amount3

alc_rev1 = round((rev_amount1 / total_rev_amount) * 100, 2)
alc_rev2 = round((rev_amount2 / total_rev_amount) * 100, 2)
alc_rev3 = round((rev_amount3 / total_rev_amount) * 100, 2)

print(f'Your total revenue is ${total_rev_amount}.')
print(f'Total revenue for {rev_source1}: ${rev_amount1}, Allocation: {alc_rev1}%')
print(f'Total revenue for {rev_source2}: ${rev_amount2}, Allocation: {alc_rev2}%')
print(f'Total revenue for {rev_source3}: ${rev_amount3}, Allocation: {alc_rev3}%')

total_exp_amount = exp_amount1 + exp_amount2 + exp_amount3

alc_exp1 = round((exp_amount1 / total_exp_amount) * 100, 2)
alc_exp2 = round((exp_amount2 / total_exp_amount) * 100, 2)
alc_exp3 = round((exp_amount3 / total_exp_amount) * 100, 2)

print(f'Your total expenses are: ${round(total_exp_amount, 2)}')
print(f'Total expense for {exp_source1}: ${exp_amount1}, Allocation: {alc_exp1}%')
print(f'Total expense for {exp_source2}: ${exp_amount2}, Allocation: {alc_exp2}%')
print(f'Total expense for {exp_source3}: ${exp_amount3}, Allocation: {alc_exp3}%')

if total_rev_amount > total_exp_amount:
    net_profit = total_rev_amount - total_exp_amount
    print(f'You have a net profit of: ${round(net_profit, 2)}')

elif total_rev_amount < total_exp_amount:
    net_loss = total_exp_amount - total_rev_amount
    print(f'WARNING: You have a net loss of: -${round (net_loss, 2)}')

elif total_rev_amount == total_exp_amount:
    print("You have broken even")

print("----- End of Financial Summary -----")