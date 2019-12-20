usernames = {

'aharo',
'hvaandres',
'andresh',
'haandres',
'uva',
}

#continue: If you place it inside of the loop will tell the prgogram to continue with this piece of software...

for username in usernames:
  if username == 'hvaandres':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

#Break will stop when we get the value that you're looking for

for username in usernames:
  if username == 'hvaandres':
    print(f'{username} was found at index {usernames.index(username)}')
    break
    print(username)