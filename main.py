'''
16/05/2024
11am
string validation in one function v3
'''

# FUNCTIONS
# functions to read and write user/pet name
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

# string validation
def input_validation(prompt, write_function, read_function, info_message):
  MIN = 1
  MAX = 20
  Valid = False
  while not Valid:
      user_input = input(prompt)
      if len(user_input) < MIN or len(user_input) > MAX:
          print("\nPlease enter a valid name.")
      else:
          write_function(user_input)
          print(info_message.format(read_function()))
          Valid = True

# feed pet function
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
          weight += 1
          user_history.append("Fed them milk")
          print("\nYou fed {} some milk.".format(
            pet_read())
          )
          return weight
        elif feed_input == 2:
          weight += 2
          user_history.append("Fed them biscuits")
          print("\nYou fed {} some biscuits.".format(
            pet_read())
          )
          return weight
        elif feed_input == 3:
          weight += 3
          user_history.append("Fed them meat")
          print("\nYou fed {} some meat.".format(
            pet_read())
          )
          return weight
    except ValueError:
      print("Please enter a valid number.")

# play with pet function
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
          user_history.append("Played fetch")
          print("\nYou played fetch with {}.".format(
            pet_read())
          )
          return weight
        elif play_input == 2:
          weight -= 2
          user_history.append("Played with a toy")
          print("\nYou played with a toy with {}.".format(
        pet_read())
        )
          return weight
        elif play_input == 3:
          weight -= 1
          user_history.append("Played with a ball")
          print("\nYou played with a ball with {}.".format(
        pet_read())
        )
          return weight
    except ValueError:
      print("Please enter a valid number.")


# edit pet and/or user name
def edit_names():
  Valid = False
  while not Valid:
    try:
      print("\nWhat name would you like to change?: ")
      user_input = int(input("1. Pet name\n"
                             "2. Owner name\n"
                             "3. Both\n\n"
                             "Enter your choice: "))
      if user_input == 1:
        input_validation(
          "\nWhat would you like to name your pet? ",
          pet_write, pet_read,
          "Your pet {} is ready for you!"
        )
        Valid = True
      elif user_input == 2:
        input_validation(
          "\nWhat is your name? ", owner_write, owner_read,
          "Your name is {}!"
        )
        Valid = True
      elif user_input == 3:
        input_validation(
          "\nWhat would you like to name your pet? ",       
          pet_write, pet_read,
          "Your pet {} is ready for you!"
        )
        input_validation(
          "\nWhat is your name? ", owner_write, owner_read,
          "Your name is {}!"
        )
        Valid = True
      else:
        print("\nPlease enter a valid number.")
    except ValueError:
      print("\nPlease enter a valid number.")


# check pet weight
def check_wellbeing(weight):
  MIN = 1
  LQ = 4
  UQ = 7
  MAX = 10
  if weight < MIN or weight > MAX:
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
    print("\n{} has died.".format(pet_read()))
    # informs user of their mistake
    if weight < 1:
      print("You forgot to feed {}.".format(pet_read()))
    else:
      print("You forgot to exercise {}.".format(pet_read()))
    
    # print user's history
    print("\nThese are the things you did with {}:\n".format(pet_read()))
    for event in range(len(user_history)):
      print(user_history[event])
    quit()

  elif weight < LQ:
    print("{} weighs {}kg. They look hungry.".format(pet_read(), weight))
    print('''
／＞　　フ
| 　_　 _ l
／` ミ＿xノ
/　　　 　 |
/　 ヽ　　 ﾉ
│　　| | |
''' )
  elif weight > UQ:
    print("{} weighs {}kg. They look full.".format(pet_read(), weight))
    print('''
／＞　　フ
| 　_　 _ l
／` ミ＿xノ
/　　　 　 |
/　 ヽ　　 ﾉ
│　　| | |
''' )
  elif weight in range(LQ, UQ) or weight == UQ:
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
input_validation(
  "\nWhat would you like to name your pet? ", pet_write, pet_read,
  "Your pet {} is ready for you!"
)
input_validation(
  "\nWhat is your name? ", owner_write, owner_read,
  "Your name is {}!"
)
# initialize global variables
user_history = []
weight = 5

# main loop
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
