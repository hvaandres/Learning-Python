# How To Query for Specific Documents in a MongoDB Collection

"""
db.books.find( {name: "For The Love of Reading"} ).pretty()
"""

# SQL Equivalent

"""
SELECT * from books WHERE name = "For The Love of Reading"

"""

# Mongo DB Projections: This topic will help you to bring only the info that you need from your database.

# 0 = Will not show info
# 1 = Will show the info

"""
Example: 

db.books&libros.find(
  {
    name: "For The Love of Resading"
  },
  {
    _id: 0,
    name: 1,
    authors: 1
  }
).pretty()


"""

# SQL Equivalent 

"""

SELECT name, authors FROM books WHERE name = 'For The Love of Reading'

"""

# Query a portion of a Nested Array Element by using $slice

"""

Example:

db.books&lobros.insert({
  "name": "White",
  "publishedDate": new Date(),
  "authors": [
    { "name": "Andres Haro" },
    { "name": "Francisco Herrera" }
  ]
});


db.books.find(
  {
    name: "Blink"
  },
  {
    publishedDate: 1,
    name: 1,
    authors: { $slice: 1 }
  }
).pretty()

"""

# Slice will help you to bring only one author instead of two. You will only need to choose 1 or 2 instead of pulling or presenting all at once.

# Removing Items Inside of Mongo delattr

"""
db.books.remove({name: " For The Love of Reading "}, 1) // Removes one single item
db.books.remove({name: "For The Love of Reading"}) // Removes all items

"""

# How to Include Nested Fields in a Find Query...

"""
db.books&libros.insert({
  "name": "White",
  "publishedDate": new Date(),
  "authors": [
    {"name": "Alan Vela", "active": "True"},
    {"name": "Lizbeth Vazquez", "active": "True"}
  ]
})

"""

# To delete the status of your authors, you will need to do the following:

"""
db.books&libros.find(
  {
    name: "White"
  },
  {
    name: 1,
    publishedDate: 1,
    "authors.name": 1
  }
).pretty()

"""

# To be more specific about searching for your file. You will need to do the following.

"""

db.books&library({ name: "For The Love of Reading"})

"""

# How To Query for a Portion of a String  in a MongoDB Documento..

"""
# Create a new book

db.books&libreria.insert({
  "name": "Me Gusta Tu Mama Y No Lo Presumo",
  "publishedDate": new Date(),
  "authors": [
    {"name": "Alan Haro"}
  ]
})

"""

# Find large Text or try to Match text

"""

db.books&libros.findOne({ name: /.*Tu Mama.*/i })

# This one will allow you to find regular expressions. In other words, will help you to match the text that you would like to find...

"""

# How to Check if a Field Exists in a MongoDB Document

"""

db.books.insert( 
  {
    "name": "Deep Work: Coco y sus aventuras mas bellas",
    "publishedDate": new Date(),
    "reviews": 992,
    "authors": [
      {"name": "Andres Haro"}
    ]
  }
)

# If you type true, you will find all the items or books that have some reviews

db.books.find({ reviews: { $exists: true } })

# If you type false, you will see all the library that doesn't have this field

db.books.find({ reviews: { $exists: false } })

"""