import random

def roll_dice():
    while True:
        try: 
            valid_input=["y","yes","ye"]
            to_leave=["e","ex","leave"]
            user_input=input("Do you want roll the dice (yes or exit): ")
            if user_input.lower().strip() in valid_input:
                random_no=random.randint(1,6)
                print(f"Dice No: {random_no}")
                print("\n")
            elif(user_input.lower().strip()=="no"):
                continue   
            elif(user_input.lower().strip() in to_leave):
                print("you succesfully leave the game")
                break
            else:
                print("invalid input")

        except ValueError:
            print("Oops! invalid input")    
            
            
roll_dice()