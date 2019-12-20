teams = {
  "Colombia": ["Medillin","Cartagena","Carichimba"],
  "Canada": ["Alberta","Blah","Blah Blah"],
  "Mexico": ["Guadalajara","Mexico City","Monterrey"],
  "USA": ["Utah","Seattle"],
}


# If we do the following, we will delete the USA Info
del teams["USA"]

# If we type the wrong team or if we try to delete an item that will not exist inside of the dictionary, we will need to do the following:

print(teams.get('mets', 'No team found by that name'))

#The information above is only to look for the name before we decide to delete the item or the info.

#Delete or remove item from the dictionary. In order to do that we need to use the function called .pop

teams.pop('Mexico', 'No item found by this name')

# Also you can see the delete items with the pop function by doing the following:

removed.team = teams.pop 'Mexico', 'No item found by this name')

print (teams)