
"""
lstrip = The lstrip() method removes any leading characters (space is the default leading character to remove)

rstrip = The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

"""


url = 'https://google.com'

# print(url.strip())
# print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)
