while True:
  print("BAND NAME GENRETOR")

  city_name = input("name of your city-\n")
  
  pet_name = input("name of your pet-\n")
  
  print("=>The right name for your band is " + city_name + " " + pet_name )
  
  answer = input("if want to continue - press y if not - n\n")
  if answer == "y":
    continue
  elif answer == "n":
    print("goodbye")
  else:
    print("input invalid") 
    break
