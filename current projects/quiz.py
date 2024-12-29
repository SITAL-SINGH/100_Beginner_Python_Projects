print("[..W E L L C O M E    T O    T H E   Q U I Z    G A M E..]".center(100))
print(".".center(100))
print(".".center(100))
print(".".center(100))
a=input("DO YOU WANT TO ENTER THE GAME ( YES / NO ): ".center(98))
if(a=="no"):
    print(".".center(100))
    print(".".center(100))
    print("THANKS FOR THE RESPONSE".center(100))
elif(a=="yes"):
    print(".".center(100))
    print("THE GAME BEGINS NOW".center(100))
print(".".center(100))
print(" 1). What is the only element that is liquid at room temperature".center(100))
print("and can be found in the human body in trace amounts?".center(104))        
print("A). Mercury                  B). Gallium".center(100))
print( "C). Bromine                  D) Phosphorus".center(101))
b=input("                            ANS: ")
if(b=="a"):
    print("you got the right answer and got one point".capitalize().center(100))
    x=1
elif(b=="mercury"):
    print("you got the correct answer".capitalize().center(100))
    x=1
else:
    print("wrong answer".capitalize().center(100))   
    x=0
print(".".center(100))
print(".".center(100))
print(" 2). Which is the only country in the world to have a flag that is not rectangular or square?".center(100))      
print("A). nepal                  B). Switzerland".center(100))
print( "C). Vatican City                  D) Bhutan".center(101))
b=input("                            ANS: ")
if(b=="a"):
    print("you got the right answer and got one point".capitalize().center(100))
    y=1
elif(b=="nepal"):
    print("you got the correct answer".capitalize().center(100))
    y=1
else:
    print("wrong answer".capitalize().center(100))   
    y=0
print(".".center(100))
print(".".center(100)) 
print(" 3). Who was the first woman to win a Nobel Prize, and in which field did she win it?".center(100))       
print("A). Marie Curie – Physics                  B). Rosalind Franklin – Chemistry".center(100))
print( "C). Dorothy Crowfoot Hodgkin – Chemistry                  D) Marie Curie – Chemistry".center(101))
b=input("                            ANS: ")
if(b=="d"):
    print("you got the right answer and got one point".capitalize().center(100))
    z=1
elif(b=="marie"):
    print("you got the correct answer".capitalize().center(100))
    z=1
elif(b=="marie curie"):
    print("you got the correct answer".capitalize().center(100))
    z=1

else:
    print("wrong answer".capitalize().center(100))   
    z=0

print(" 4). Which famous author wrote under the pseudonym 'Robert Galbraith'y?".center(100))
      
print("A). J.R.R. Tolkien                  B). Agatha Christie".center(100))
print( "C). J.K. Rowling                  D) Ian Fleming".center(101))
b=input("                            ANS: ")
if(b=="c"):
    print("you got the right answer and got one point".capitalize().center(100))
    p=1
elif(b=="jk"):
    print("you got the correct answer".capitalize().center(100))
    p=1
else:
    print("wrong answer".capitalize().center(100))   
    p=0

print(" 5). Which actor holds the record for most appearances in a Marvel Cinematic Universe (MCU) film?".center(100))
       
print("A). Robert Downey Jr.                  B). Samuel L. Jackson".center(100))
print( "C). Chris Hemsworth                  D). Scarlett Johansson ".center(101))
b=input("                            ANS: ")
if(b=="b"):
    print("you got the right answer and got one point".capitalize().center(100))
    q=1
elif(b=="samuel"):
    print("you got the correct answer".capitalize().center(100))
    q=1
else:
    print("wrong answer".capitalize().center(100))   
    q=0         

d=x+y+z+p+q
print("your final score is",a)
