
#This should be made on Python 3.7 to make sure we can do the interpolation.




def heading_generator (tittle, heading_type):
  return f'<h{heading_type}>{tittle}</h{heading_type}>'

  print(heading_generator('Greetings!','1'))
  print(heading_generator('I am in  a tittle', '3'))