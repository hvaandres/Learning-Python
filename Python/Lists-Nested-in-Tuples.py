post = ('Learning', 'Coding Skills', 'Online')

tags =['HTML', 'CSS', 'Python']

columns = {}

post += (tags,)

print(post[-1][2])

# Will print all list because it parse and check all the items that you have inside of the post...
print(post[:3]) 


#Will print all post & all tags
print(post[0::1])

#Will print one post & all tags
print(post[1::2])
