# ask user's name and pet name.
# present user with options of pet activities e.g. feed, play, quit
# a function will exectue the activity chosen by the user
# run a function to check pet's wellbeing
# if pet is unwell, pet will die
# if pet is well, pet will live

'''
25/04/2024
10:20pm
established main menu, feed function and play function.
'''
# FUNCTIONS
def main_menu(weight):
  Valid = False
  while not Valid:
    print("\nWelcome {}! What would you like to do?".format(user_name))
    print("1. Feed")
    print("2. Play")
    print("3. Edit Names")
    print("4. Quit")
    try:
      menu_input = int(input("\nEnter your choice: "))
      if menu_input < 1 or menu_input > 4:
        print("Please enter a valid number.")
      elif menu_input == 1:
        weight = feed(weight)
      elif menu_input == 2:
        weight = play(weight)
      elif menu_input == 3:
        edit_names()
      elif menu_input == 4:
        quit()
    except ValueError:
      print("Please enter a valid number.")

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
          weight = weight + 1
          print("You fed your pet some kale. Your pet now weighs", weight, "kg.")
          return weight
        elif feed_input == 2:
          weight = weight + 2
          print("You fed your pet some broccoli. Your pet now weighs", weight, "kg.")
          return weight
        elif feed_input == 3:
          weight = weight + 3
          print("You fed your pet some apples. Your pet now weighs", weight, "kg.")
          return weight
    except ValueError:
      print("Please enter a valid number.")


def play(weight):
  print("What would you like to do with your pet?")
  print("1. Play fetch\n2. Play with a toy\n3. Play with a ball")
  Valid = False
  while not Valid:
    try:
      play_input = int(input("\nEnter your choice: "))
      if play_input < 1 or play_input > 3:
        print("Please enter a valid number.")
      else:
        Valid = True
        if play_input == 1:
          weight -= 3
          print("You played fetch with your pet. Your pet now weighs", weight, "kg.")
          return weight
        elif play_input == 2:
          weight -= 2
          print('You played with a toy with your pet. Your pet now weighs', weight, 'kg.')
          return weight
        elif play_input == 3:
          weight -= 1
          print("You played with a ball with your pet. Your pet now weighs", weight, "kg.")
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
main_menu(weight)


'''
file = open("pet.txt", "w")
file.write(user_name + "\n")
file.write(pet_name)
file.close()
'''
