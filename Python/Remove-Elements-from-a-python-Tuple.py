post = ('Learning', 'Coding Skillss', 'Programming languages')

# Removing elements from end
post = post[:-1]

# Removing elements from beginning
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)