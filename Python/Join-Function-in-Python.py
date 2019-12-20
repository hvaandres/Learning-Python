# https://www.google.com/search?client=firefox-b-1-d&q=python+course+bottega

uri = 'https://www.google.com/search?q='
tags = ['python', 'course', 'bottega']
fromatted_tags = '+' .join(tags)
query_uri = f'{uri}{fromatted_tags}'

print(query_uri)