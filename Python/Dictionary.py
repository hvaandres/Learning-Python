
#Dictionaries

players = {
  "ss": "Puyol",
  "2b": "Chicharito",
  "3b": "Beckam",
  "DH": "Neimar",
  "OF": "DosSantos",
}

second_base = players['2b']
designated_hitter = players['DH']

print(designated_hitter)
print(second_base)

#Nested  Collections in Dictionaries (You can add list of team and teamplayer)

teams = {
  "Barcelona": ["Chicharito", "Puyol", "Beckam"],
  "Manchester": ["Trout", "Pujols"],
  "Real Madrid": ["Judge", "Stanton"],
}

start = teams['start']
print(start)
print(teams['Barcelona'])
print(teams['Real Madrid'])


