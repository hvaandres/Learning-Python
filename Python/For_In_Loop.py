#Adding New Items to a List with a Loop
#Current customers
golden_customers = ['Andres','Adrian']
#Add new customers
new_customers = ['Cristina','Liliana']

# Nested List
combine_gn = [golden_customers, new_customers]

print(combine_gn)

# iterating the pre-existing list
# Combine all the information to get the new clients inside of the current employees
 
for golden_customer in golden_customers:
  new_customers.append(golden_customer)

  print(new_customers)