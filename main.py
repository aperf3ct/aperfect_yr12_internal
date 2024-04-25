# ask user's name and pet name.
# present user with options of pet activities e.g. feed, play, quit
# a function will exectue the activity chosen by the user
# run a function to check pet's wellbeing
# if pet is unwell, pet will die
# if pet is well, pet will live

'''
25/04/2024
10pm
setting up feed function
'''
# FUNCTIONS
def main_menu():
  print("\nWhat would you like to do?")
  print("1. Feed")
  print("2. Play")
  print("3. Edit Names")
  print("4. Quit")
  Valid = False
  while not Valid:
    try:
      menu_input = int(input("\nEnter your choice: "))
      if menu_input < 1 or menu_input > 4:
        print("Please enter a valid number.")
      else:
        return menu_input
    except ValueError:
      print("Please enter a valid number.")


def user_selection(selection, weight):
  if selection == 1:
    weight = feed(weight)
    return weight
  elif selection == 2:
    weight = play()
    return weight
  elif selection == 3:
    edit_names()
  elif selection == 4:
    quit()

def feed(weight):
  print("What woud you like to feed your pet?")
  print("1. Kale\n2. Broccoli\n3. Apples")
  Valid = False
  while not Valid:
    try:
      feed_input = int(input("\nEnter your choice: "))
      if feed_input < 1 or feed_input > 3:
        print("Please enter a valid number.")
      else:
        Valid = True
        if feed_input == 1:
          weight = weight + 0.1
          print("You fed your pet some kale. Your pet now weighs", weight, "kg.")
          return weight
        elif feed_input == 2:
          weight = weight + 0.2
          print("You fed your pet some broccoli. Your pet now weighs", weight, "kg.")
          return weight
        elif feed_input == 3:
          weight = weight + 0.4
          print("You fed your pet some apples. Your pet now weighs", weight, "kg.")
          return weight
    except ValueError:
      print("Please enter a valid number.")


# MAIN PROGRAM
print("Welcome to the Pet Simulator!")
user_name = input("What is your name? ")
pet_name = input("What would you like to name your pet? ")
print("Hello {}! Your pet {} is ready for you!".format(user_name, pet_name))
#add art here

weight = 2
selection = main_menu()
weight = user_selection(selection, weight)


'''
file = open("pet.txt", "w")
file.write(user_name + "\n")
file.write(pet_name)
file.close()
'''
