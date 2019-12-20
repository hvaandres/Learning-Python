# Polymorphic Function: 

class Mexico ():
  def description (self):
    print("Mexico is one of the biggest countries of the world.")
  def language (self):
    print("Mexican people speak Spanish.")

class Guadalajara ():
  def description (self):
    print("Tapatios are from Guadalajara. In other words, Guadalajara is part of Mexico.")
  def language(self):
    print("We don't speak the same as chilangos.")

  def type(self):
    print("Viva Mexico Cabrones.")

def function(object):
  object.description()
  object.language()
  object.type()

object_MX = Mexico()
object_GDL = Guadalajara()

function (object_MX)
function (object_GDL)
