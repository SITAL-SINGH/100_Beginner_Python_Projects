import random
print(" WELCOME TO THE 'ROCK PAPER  AND SCISSORS' GAME\n".center(70))

randomact=random.randint(1,3)
# 1=rock
# 2=scissors
# 3=paper
# class SomeError(Exception): #custom exception for error haldling
#     pass
try:
    
    enter=input("enter Rock, paper and scissors: ")
    if (enter.lower()=="rock"):
        if(randomact==1):
            print("Computer Entered: Rock")
            print("Tie")

        elif (randomact==2):
            print("Computer Entered: scissor")
            print("You won the game")  
        
        elif (randomact==3):
            print("Computer Entered: paper")
            print("You loose the game")  
             
    elif (enter.lower()=="scissor"):
        if(randomact==1):
            print("Computer Entered: Rock")
            print("You lose the game")

        elif (randomact==2):
            print("Computer Entered: scissors")
            print("Tie")  
        
        elif (randomact==3):
            print("Computer Entered: paper")
            print("You won the game")  
                      
    elif (enter.lower()=="paper"):
        if(randomact==1):
            print("Computer Entered: Rock")
            print("you won the game")

        elif (randomact==2):
            print("Computer Entered: scissor")
            print("You Loose the game")  
        
        elif (randomact==3):
            print("Computer Entered: paper")
            print("Tie")  

    else:  
        print("Oops! Invalid Input Please Try Again")             

# except SomeError:
#     print("Oops! Invalid Input Please Try Again")
except ValueError:
    print("Oops! Invalid Input Please Try Again")
          


    
