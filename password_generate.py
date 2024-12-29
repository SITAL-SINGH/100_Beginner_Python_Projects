import random 
import string
def password_generate(pass_length,list1):
    for i in range(pass_length):
        random_pass=random.choice(list1)
        random_pass1="".join(random_pass)
        # print(random_pass1,end="")
        print(random_pass1,end=" ")




    


while True:
    try:
        pass_length=int(input("\nEnter the length of the password: "))
        list_punctuation=["#","@",",","$","%","&","*","_"]
        list1=list(string.ascii_letters)+list(string.digits)+list(list_punctuation)
        print("The pass is: ")
        password_generate(pass_length,list1)
        print("\n")


    except ValueError:
        print("\nOpps! invalid input\n")
    except Exception as e: 
        pass









    