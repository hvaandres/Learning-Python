"""

tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[2:]
tag_range = tags[0:2]
tag_range = tags[:2]
tag_range = tags[0:-1]

print(tag_range)

"""

tags = [
  'python',
  'development',
  'code',
  'programming',
  'computer science'
]

#tag_range = tags[1:-1:2]
tag_range = tags[::-1] # flipping the order of your list [::-1]
# To get a random order or sort order, you will need to do this: tags.sort(reverse=True) / print(tags)

#To get none or not ssorting items, you will need to create a variable like this: sorted_tags = tags.sort(reverse=True) In other words is embracing immutability

print (tag_range)