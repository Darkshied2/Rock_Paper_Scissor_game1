# This game is user v/s player
# In this game, user gets the first chance to pick the option among Rock, paper
# and scissor. After that computer select from remaining two choices(randomly),
# then winner is decided as per the rules.
# Winning Rules as follows :

# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.


# import random module 
import random 

# Print multiline instruction 
# performstring concatenation of string 
print("Winning Rules of the Rock paper scissor game are as follows: \n" + 
      "Rock vs paper-> paper wins\n" + "Rock vs scissor-> Rock wins\n" + 
      "paper vs scissor-> scissor wins.\n")

while True:
    print("Enter Choices:\n1. Rock\n2. Paper\n3. Scissor\n")
    choice = int (input("Your Turn...")) #Taking Input from user

#Check for valid input
    while choice > 3 or choice < 1:
        choice = int(input("INVALID INPUT ! PLEASE ENTER VALID INPUT ..."))

    # initialize value of choice_name variable 
    # corresponding to the choice value    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'

    #Print user choice  
    print("Your choice is: " + choice_name) 
    print("\nNow its computer turn.......")


    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module 
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value  
    # is equal to the choice value 
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print("Computer choice is: " + comp_choice_name)            

    print(choice_name + " v/s " + comp_choice_name)

    # condition for winning
    if((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice ==1 )):
            print("Paper wins\n ", end = "")
            result = "paper"

    elif((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):
            print("Rock wins\n", end = "") 
            result = "Rock"    
            
    else: 
            print("Scissor wins\n =>", end = "") 
            result = "scissor"    
            
            
    # Printing either user or computer wins 
    if result == choice_name: 
            print("<== You Win ==>") 
    else: 
            print("<==Oops!You Lost ==>") 



    print("Do you want to play again? (Y/N)") 
    ans = input()   
    
    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'N': 
        break

    # after coming out of the while loop 
    # we print thanks for playing 
    print("\nThanks for playing")
                                                                


















