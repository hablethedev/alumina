import alumina.py as maphandle

gameName = input("Input a game name: ")
mapentities = ["","","","",""
      "","","P","","",
      "","","","",""]
      
maplocations = ["","","","",""
      "","","Grassy Grasslands","","",
      "","","","",""]

maphandle.init(gameName, maplocations, mapentities)