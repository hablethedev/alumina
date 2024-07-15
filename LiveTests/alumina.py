#
#
# Yes, Alumina is one python file.

def init(name, madeWith=True, mapL, mapE):
  global mapLocations
  mapLocations = mapL
  global mapEntities
  mapEntities = mapE
  print(" ")
  if madeWith != False:
    print("Made with Alumina, by hablethedev")
    print(" ")
  print("Welcome to " + name + ".")
  print("Currently in " + mapLocations[mapEntities.value("P")])