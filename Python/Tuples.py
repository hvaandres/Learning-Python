# Rules: List [], Dictionary {} & Tuple()
# Strong Rule: If you set up a Tuple, you will need to make sure that this information is not going to change since tuples are immutable & lists are mutable

# Tuple: immutable 
# List: mutable

post = ('UVU', 'Web & App Development Services', 'We are the department that can help you with web design')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)