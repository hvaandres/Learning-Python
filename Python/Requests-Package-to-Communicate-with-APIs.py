
# You will need to import the libraries that you will need to use!

import requests
import pprint

# Create a variable and request what you need and don't forget to add the .get since you would like to get a URL...

r = requests.get('https://api.dailysmarty.com/posts')

# To pull out all of this information you will need to ask for the json file.

r.json()

# To get a clean data, you will need to use the pprint library to make sure you can see this information as you can see it in a website..

pprint.pprint(r.json()['posts'][0])

# The next line is to see the real URL from the website that contain all this information

pprint.pprint(r.json()['posts'][0]['url_for_post'])