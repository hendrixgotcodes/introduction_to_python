

# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1*price
# else:
#     down_payment = 0.2*price

# print(f"Down payment is GH₵{down_payment}")

# # *********************************************************

# high_income = True

# if high_income and has_good_credit:
#     print("Customer is eligible for loan")

# if high_income or has_good_credit:
#     print("Customer is eligible for loan")

# if not high_income:
#     print("Customer is eligible for loan")
# else:
#     print("Customer is not eligible for loan")

name = input("Please enter your name ")

if len(name) < 3:
    name = input("Name must be atleast 3 characters long. Please try again ")
elif len(name) > 50:
    name = input("Name must be less than 50 characters long ")
else:
    print("name looks good")