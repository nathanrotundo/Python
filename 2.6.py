# asking user total budget 
budget = float(input("enter total budget: $"))

# asking user amount for each individual catagory
housing = float(input("Enter amount spent on housing $"))
utilities = float(input("Enter amount spent on utilities $"))
groceries = float(input("Enter amount spent on groceries $"))
transportation = float(input("Enter amount spent on transportation $"))
health_care = float(input("Enter amount spent on healthcare $"))
personal_care = float(input("Enter amount spent on personal care $"))
clothing = float(input("Enter amount spent on clothing $"))
debt = float(input("Enter amount spent on debt $"))

# calculating percatage of budget each catagry takes up
housing_percentage = (housing / budget) * 100
utilities_percentage = (utilities / budget) * 100
groceries_percentage = (groceries / budget) * 100
transportation_percentage = (transportation / budget) * 100
health_care_percentage = (health_care / budget) * 100
personal_care_percentage = (personal_care / budget) * 100
clothing_percentage = (clothing / budget) * 100
debt_percentage = (debt / budget) * 100

# displying results to user 
print(f"Housing: ${housing:.2f} ({housing_percentage:.2f}%) of the total budget")
print(f"Utilities: ${utilities:.2f} ({utilities_percentage:.2f}%) of the total budget")
print(f"Groceries: ${groceries:.2f} ({groceries_percentage:.2f}%) of the total budget")
print(f"Transportation: ${transportation:.2f} ({transportation_percentage:.2f}%) of the total budget")
print(f"Health Care: ${health_care:.2f} ({health_care_percentage:.2f}%) of the total budget")
print(f"Personal Care: ${personal_care:.2f} ({personal_care_percentage:.2f}%) of the total budget")
print(f"Clothing: ${clothing:.2f} ({clothing_percentage:.2f}%) of the total budget")
print(f"Debt: ${debt:.2f} ({debt_percentage:.2f}%) of the total budget")