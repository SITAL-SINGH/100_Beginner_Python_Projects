import random
print("...WELCOME TO THE GUESS THE NUMBER GAME...".center(70))
random_no=random.randint(1,100)
max_attempts=100
print("\n")
print(f"Notice!!! Your Max Attempts Will Be  {max_attempts}")
print("\n")
count=0
while(count<=max_attempts):
    try:
        enter=input("Guess The Number Or Type 'Quit' To leave the game=")
        if(enter.lower()=="quit"):
           
            remaining_count=100-count 
            print(f"Your Attempts: {count}")
            print(f"Remaining Attempts: {remaining_count}") 
            print("\n")                         
            print("..Thanks For Playing The Game..") 
            break
        print("\n")
        count=count+1
        remaining_count=100-count

        print(f"Your Attempts: {count}")
        print(f"Remaining Attempts: {remaining_count}")

        if(int(enter)<random_no):
            print("You Guessed Too Low")
            print("\n")  
            
        elif(int(enter)>random_no):
            print("You Guessed Too High")
            print("\n")
            
        else:
            print("Your Guess Is Correct") 
            print("\n") 
            print("Congratulations! You Won The Game")
            print("\n") 
            print("You Got Brand New Iphone As A Winning Gift")
            print("\n")              

            break       

    except ValueError:
        print("Oops! You Entered Invalid Value") 
        print("\n")


if(count==max_attempts):
    print(" You Have Used Your 100 Attempts...Better Luck Next Time ")
    print("\n") 

else:
    print("")
                 

    

