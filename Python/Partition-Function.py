heading = "Python: An Introduction, and Python: Advanced"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)

# Split Function

tags = 'python,coding,programming, development'

list_of_tags = tags.split(',')

list_of_tags = tags.split()

print(list_of_tags)
print(list_of_tags)


heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)