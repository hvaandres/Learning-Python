tags =['python', 'development', 'tutorials', 'code']

# Big No No
"""
tags[-1] = 'programming'
print(tags)

This will overridde the last element..

tags.extend('Programming')
print(tags)

Will insert the word but will be divided letter by letter...

"""

# Yes We Can Do That (In Place)

tags.extend(['Programming'])

# New List
new_tags = tags + (["Programming2"])

print(tags)
print(new_tags)

