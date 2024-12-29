import string
import random

string_letters=list(string.ascii_letters)

def secretcoder(input_as_list,input_length):
    if input_length>=3:
        removed_item=input_as_list.pop(0)
        input_as_list.append(removed_item)
        for i in range(1,4):
            random_letters_start=random.choice(string_letters)
            random_letters_end=random.choice(string_letters)
            input_as_list.insert(0,random_letters_start)
            input_as_list.insert(len(input_as_list),random_letters_end)
        # for i in range(1,4):
        #     random_letters_end=random.choice(string_letters)
        #     input_as_list.insert(len(input_as_list),random_letters_end)
        return input_as_list  
    else:
        input_as_list.reverse()
        return input_as_list

    



def decoder(input_as_list,input_length):
    if input_length<3:  # we does not have to pass input_length as argumeant to access inside fuction because input_lengt is declared globally
        input_as_list.reverse()
        return input_as_list
    
    else:
        for i in range(1,4):
            input_as_list.pop(0)
            input_as_list.pop(len(input_as_list)-1)
        removed_item=input_as_list.pop(len(input_as_list)-1)
        input_as_list.insert(0,removed_item)
        return input_as_list
        

    

    

    
def mainapp():
    print("...welcome to secret language converter...\n".center(65))
    print("CHOICE: ")
    print("Encode ----------> e")
    print("Decode ----------> d")
    print("\n")
    while True:
        choice=input("Do you want to encode or decode (e/d): ")
        valid_input=["e","E","d","D"]
        if choice in valid_input:
            user_input=input("enter the letter: ")    # Take input from user
            input_as_list=list(user_input)            # conver user_input into list
            input_length=len(user_input)      # caculate the length of the user input
            
            if choice.strip().lower()=="e":

                if input_length>=3:
                    updated_list=secretcoder(input_as_list,input_length)
                    encoded_input=''.join(updated_list)    # to convert list back into its string format
                    print(encoded_input)
                    print("\n")

                elif input_length<3:
                    updated_list=secretcoder(input_as_list,input_length)
                    encoded_input=''.join(updated_list)
                    print(encoded_input)
                    print("\n")
            
            else: 
                if input_length<3:
                    decoded_list=decoder(input_as_list,input_length)
                    decoded_msg=''.join(decoded_list)
                    print(decoded_msg)
                    print("\n")
                else:
                    decoded_list=decoder(input_as_list,input_length)
                    decoded_msg=''.join(decoded_list)
                    print(decoded_msg)
                    print("\n")

        else: 
            print("invalid input")


mainapp()
        



    

