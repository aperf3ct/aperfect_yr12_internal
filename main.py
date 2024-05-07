'''
08/05/2024
11am
edit names function reads from two txt files
'''

# FUNCTIONS
def file_write(str):
  text = open("names.txt", "w")
  text.write(str)
  text.close()


def file_read():
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

def feed(weight):
  print("\nWhat would you like to feed {}?".format(file_read()))
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
          print("\nYou fed {} some milk. {} now weighs {}kg.".format(
            file_read(), file_read(), weight)
          )
          return weight
        elif feed_input == 2:
          weight = weight + 2
          print("\nYou fed {} some biscuits. {} now weighs {}kg.".format(
            file_read(), file_read(), weight)
          )
          return weight
        elif feed_input == 3:
          weight = weight + 3
          print("\nYou fed {} some Meat. {} now weighs {}kg.".format(
            file_read(), file_read(), weight)
          )
          return weight
    except ValueError:
      print("Please enter a valid number.")


def play(weight):
  print("\nWhat would you like to do with {}?".format(file_read()))
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
          print("\nYou played fetch with {}. {} now weighs {}kg.".format(
            file_read(), file_read(), weight)
          )
          return weight
        elif play_input == 2:
          weight -= 2
          print("\nYou played with a toy with {}. {} now weighs {}kg.".format(
        file_read(), file_read(), weight)
        )
          return weight
        elif play_input == 3:
          weight -= 1
          print("\nYou played with a ball with {}. {} now weighs {}kg.".format(
        file_read(), file_read(), weight)
        )
          return weight
    except ValueError:
      print("Please enter a valid number.")


def edit_names(user_name):
  print("\nWhat name would you like to change?: ")
  valid = False
  while not valid:
    try:
      user_input = int(input("1. Pet name\n"
                             "2. Owner name\n"
                             "3. Both\n\n"
                             "Enter your choice: "))
      if user_input == 1:
        pet_name = input("Enter new name: ")
        file_write(pet_name)
        print("\nName changed to", pet_name)
        valid = True
      elif user_input == 2:
        user_name = input("Enter new name: ")
        owner_write(user_name)
        print("Owner name changed to", user_name)
        valid = True
      elif user_input == 3:
        pet_name = input("Enter new pet name: ")
        file_write(pet_name)
        print("\nName changed to", pet_name)
        user_name = input("Enter new owner name: ")
        owner_write(user_name)
        print("\nName changed to", user_name)
        valid = True
    except ValueError:
      print("Please enter a valid number.")
  

def check_wellbeing(weight):
  if weight < 1 or weight > 10:
    print("\n{} has died.".format(file_read()))
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
    print("{} looks hungry.".format(file_read()))
    print('''
　　　　　／＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　| | |
''' )
  elif weight > 7:
    print("{} looks full.".format(file_read()))
    print('''
　　　　　／＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　| | |
''' )
  elif weight in range (4,8):
    print("{} is doing well :)".format(file_read()))
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
user_name = input("What is your name? ")
owner_write(user_name)
pet_name = input("What would you like to name your pet? ")
file_write(pet_name)
print("Hello {}! Your pet {} is ready for you!".format(owner_read(), file_read()))

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
      edit_names(user_name)
    elif menu_input == 4:
      quit()
  except ValueError:
    print("Please enter a valid number.")
