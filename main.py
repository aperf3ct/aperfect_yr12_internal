'''
10/05/2024
2pm
string validation in a function v2
'''

# FUNCTIONS
def pet_write(str):
  text = open("names.txt", "w")
  text.write(str)
  text.close()


def pet_read():
  text = open("names.txt", "r")
  pet_name = text.read()
  text.close()
  return pet_name

def owner_write(str):
  text = open("owner.txt", "w")
  text.write(str)
  text.close()


def owner_read():
  text = open("owner.txt", "r")
  owner_name = text.read()
  text.close()
  return owner_name

def pet_validation():
  valid = False
  while not valid:
    pet_name = input("\nWhat would you like to name your pet? ")
    if len(pet_name) < 1 or len(pet_name) > 20:
      print("\nPlease enter a valid name. ")
    else:
      pet_write(pet_name)
      print("Your pet {} is ready for you!".format(pet_read()))
      valid = True

def owner_validation():
  valid = False
  while not valid:
    owner_name = input("\nWhat is your name? ")
    if len(owner_name) < 1 or len(owner_name) > 20:
      print("\nPlease enter a valid name. ")
    else:
      owner_write(owner_name)
      print("Your name is {}!".format(owner_read()))
      valid = True

def feed(weight):
  print("\nWhat would you like to feed {}?".format(pet_read()))
  print("1. Milk\n2. Biscuits\n3. Meat")
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
          print("\nYou fed {} some milk.".format(
            pet_read())
          )
          return weight
        elif feed_input == 2:
          weight = weight + 2
          print("\nYou fed {} some biscuits.".format(
            pet_read())
          )
          return weight
        elif feed_input == 3:
          weight = weight + 3
          print("\nYou fed {} some Meat.".format(
            pet_read())
          )
          return weight
    except ValueError:
      print("Please enter a valid number.")


def play(weight):
  print("\nWhat would you like to do with {}?".format(pet_read()))
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
          print("\nYou played fetch with {}.".format(
            pet_read())
          )
          return weight
        elif play_input == 2:
          weight -= 2
          print("\nYou played with a toy with {}.".format(
        pet_read())
        )
          return weight
        elif play_input == 3:
          weight -= 1
          print("\nYou played with a ball with {}.".format(
        pet_read())
        )
          return weight
    except ValueError:
      print("Please enter a valid number.")


def edit_names():
  valid = False
  while not valid:
    try:
      print("\nWhat name would you like to change?: ")
      user_input = int(input("1. Pet name\n"
                             "2. Owner name\n"
                             "3. Both\n\n"
                             "Enter your choice: "))
      if user_input == 1:
        pet_validation()
        valid = True
      elif user_input == 2:
        owner_validation()
        valid = True
      elif user_input == 3:
        pet_validation()
        owner_validation()
        valid = True
      else:
        print("\nPlease enter a valid number.")
    except ValueError:
      print("\nPlease enter a valid number.")


def check_wellbeing(weight):
  if weight < 1 or weight > 10:
    print("\n{} has died.".format(pet_read()))
    print(
    '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣟⣛⣛⡓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣟⣵⠟⠋⠉⠁⠈⠉⢳⡈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠻⣄⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣭⡙⢦⣄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢰⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡙⣆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠠⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⢹⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢰⣧⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠸⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠨⣿⡇⠀⢀⣠⣤⣤⣀⣀⠀⢠⣤⠤⣤⡄⣠⣀⣀⣀⣀⡀⠀⢸⢰⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⢾⢹⠋⠉⠛⣯⢻⡤⢹⡧⡟⠀⣿⣾⠛⠛⢿⣽⣄⣼⢸⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⢸⣼⡄⠀⢀⡾⣸⠇⢸⠀⡇⠀⣿⣿⠀⠀⢸⣿⠏⡏⣼⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡯⡇⠀⢸⣼⣷⣾⡿⠛⠉⠀⢸ ⡇⠀⣿⣿⣶⣾⠿⠏⠀⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⡇⠀⢸⣿⡟⠻⣿⢦⡀⠀⢠⡧⡇⢀⣿⣿⠀⠀⠀⠀⢠⡏⡏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⡇⢀⣼⣿⣷⡄⠸⠿⠿⠦⢨⣷⣧⠈⣿⣾⣥⠀⠀⠀⢸⠇⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢹⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢸⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣸⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣴⠃⣿⢷⣄⣀⣀⣀⣀⣄⣄⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣤⡿⣹⠙⣆⠀⠀⠀⠀
    ⠀⠀⢀⡾⠃⠀⠛⠒⠒⠒⠛⠛⠻⠿⠷⠶⠶⠶⠶⠦⠶⠶⠖⠒⠒⠛⠛⠛⠀⠘⣦⠀⠀⠀
    ⠀⠀⣸⠧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠶⠾⣷⠀⠀
    ⠀⠀⠹⣦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣄⣀⣀⣀⣀⣀⣤⣤⣤⡿⠀⠀

''')
    quit()

  elif weight < 4:
    print("{} weighs {}kg. They look hungry.".format(pet_read(), weight))
    print('''
／＞　　フ
| 　_　 _ l
／` ミ＿xノ
/　　　 　 |
/　 ヽ　　 ﾉ
│　　| | |
''' )
  elif weight > 7:
    print("{} weighs {}kg. They look full.".format(pet_read(), weight))
    print('''
／＞　　フ
| 　_　 _ l
／` ミ＿xノ
/　　　 　 |
/　 ヽ　　 ﾉ
│　　| | |
''' )
  elif weight in range (4,8):
    print("{} weighs {}kg. They are doing doing well :)".format(pet_read(), weight))
    print('''
     |\_/|    
     (. .)
      =w= (\  
     / ^ \//  
    (|| ||)
    ,""_""_ .
''')

# MAIN PROGRAM
print("Welcome to the Pet Simulator!")
pet_validation()
owner_validation()

weight = 5
Valid = False
while not Valid:
  print("\nWelcome {}! What would you like to do?".format(owner_read()))
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
      check_wellbeing(weight)
    elif menu_input == 2:
      weight = play(weight)
      check_wellbeing(weight)
    elif menu_input == 3:
      edit_names()
    elif menu_input == 4:
      quit()
  except ValueError:
    print("Please enter a valid number.")
