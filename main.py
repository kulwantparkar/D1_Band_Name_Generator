while True:
  #1. Create a greeting for your program.
  print("BAND NAME GENRETOR")

  #2. Ask the user for the city that they grew up in.
  city_name = input("name of your city-\n")
  #3. Ask the user for the name of a pet.
  pet_name = input("name of your pet-\n")
  #4. Combine the name of their city and pet and show them their band name.
  print("=>The right name for your band is " + city_name + " " + pet_name )
  #5. Make sure the input cursor shows on a new line, see the example at:
  #   https://replit.com/@appbrewery/band-name-generator-end
  answer = input("if want to continue - press y if not - n\n")
  if answer == "y":
    continue
  elif answer == "n":
    print("goodbye")
  else:
    print("input invalid") 
    break