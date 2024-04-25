# ask user's name and pet name.
# present user with options of pet activities e.g. feed, play, quit
# a function will exectue the activity chosen by the user
# run a function to check pet's wellbeing
# if pet is unwell, pet will die
# if pet is well, pet will live

'''
25/04/2024
3:00pm
Setup of main menu function and user/pet names
'''

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


print("Welcome to the Pet Simulator!")
user_name = input("What is your name? ")
pet_name = input("What would you like to name your pet? ")
print("Hello {}! Your pet {} is ready for you!".format(user_name, pet_name))
#add art here

selection = main_menu()


'''
file = open("pet.txt", "w")
file.write(user_name + "\n")
file.write(pet_name)
file.close()
'''