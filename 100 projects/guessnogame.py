import random
guess_the_no=random.randint(1,100)
count=0
while(count<100):
    enter=int(input("Guesss The Number From (1 to 100): "))
    if(enter> guess_the_no):
        print("You Guessed High")
        count=count+1
        print(f"Number OF Times You Guessed: {count}")
    elif(enter==guess_the_no):
        print("Congratulations You Guessed The Correct") 
        count=count+1   
        print(f"Number OF Times You Guessed: {count}")
        break
    else:
        print("You Guessed Low")
        count=count+1
        print(f"Number Of Times You Guessed: {count}")

print("..You Got Brand New Iphone As A Gift..")        