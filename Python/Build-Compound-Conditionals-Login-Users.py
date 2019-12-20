
username = ''
email = ''
password = ''

if username == '' and password == '':
  print('Access permitted')
else:
  print('You shouldnt be here!')

# Only one required, you will need to use "or"
# My parenthesis will determinated if I need one or the other

if (username == '' or email == '') and password == '':
  print('Access permitted')
else:
  print('Not allowed')

if username == '' or password == '':
  print('Access permitted')
else:
  print('Not allowed')

logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standar dashboard')
