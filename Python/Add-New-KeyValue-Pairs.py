#Add New Key/ Value Pairs 


teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

# Add a new team and new teammates

teams['red sox'] = ['price', 'Betts']




# Using the get function / Configure Fallback Lookup Values

featured_team = teams.get('yankees', 'No featired team')

print(featured_team)
