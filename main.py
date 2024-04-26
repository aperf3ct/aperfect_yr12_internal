# ask user's name and pet name.
# present user with options of pet activities e.g. feed, play, quit
# a function will exectue the activity chosen by the user
# run a function to check pet's wellbeing
# if pet is unwell, pet will die
# if pet is well, pet will live

'''
26/04/2024
4:00pm

'''
# FUNCTIONs 
def feed(weight):
  print("\nWhat woud you like to feed", pet_name, "?")
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
            pet_name, pet_name, weight)
          )
          return weight
        elif feed_input == 2:
          weight = weight + 2
          print("\nYou fed {} some biscuits. {} now weighs {}kg.".format(
          pet_name, pet_name, weight)  
          )
          return weight
        elif feed_input == 3:
          weight = weight + 3
          print("\nYou fed {} some Meat. {} now weighs {}kg.".format(
          pet_name, pet_name, weight)
          )
          return weight
    except ValueError:
      print("Please enter a valid number.")


def play(weight):
  print("\nWhat would you like to do with ", pet_name, "?")
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
            pet_name, pet_name, weight)
          )
          return weight
        elif play_input == 2:
          weight -= 2
          print("\nYou played with a toy with {}. {} now weighs {}kg.".format(
            pet_name, pet_name, weight)
          )
          return weight
        elif play_input == 3:
          weight -= 1
          print("\nYou played with a ball with {}. {} now weighs {}kg.".format(
              pet_name, pet_name, weight)
          )
          return weight
    except ValueError:
      print("Please enter a valid number.")


def check_wellbeing(weight):
  if weight < 1:
    print(pet_name, "didn't eat in a while. They died ):")
    quit()
  elif weight > 10:
    print(pet_name, "ate too much. They died ):")
    quit()
  elif weight < 4:
    print(pet_name, "looks hungry.")
  elif weight > 7:
    print(pet_name, "looks full.")
  elif weight in range (4,8):
    print(pet_name, "is doing well :)")
  
# MAIN PROGRAM
print('''
 |\_/|    
 (. .)
  =w= (\  
 / ^ \//  
(|| ||)
,""_""_ .
''')

print('''
               _ |\_      
               \` ..\  
          __,.-" =__Y=
        ."        )
  _    /   ,    \/\_  _ 
 ((____|    )_-\ \_-`(_)
 `-----'`-----` `--`
''')

print('''
　　　　　／＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　| | |
''' )


print("Welcome to the Pet Simulator!")
user_name = input("What is your name? ")
pet_name = input("What would you like to name your pet? ")
print("Hello {}! Your pet {} is ready for you!".format(user_name, pet_name))
#add art here

weight = 5
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

'''
file = open("pet.txt", "w")
file.write(user_name + "\n")
file.write(pet_name)
file.close()
'''
