# defining four functions for each tasks
def addition(num1,num2):
    add=num1+num2
    return(add)
    # print(num1+num2)
def subraction(num1,num2):
    return (num1-num2)

def multiplication(num1 , num2):
    return (num1 * num2)

def division(num1 , num2):
    if num2 !=0:
        return (num1/num2)
def modulus(num1,num2):
    return(num1%num2)

def compare(num1,num2): 
    if (num1>num2):
        return(f"{num1} is greater")

    elif((num2>num1)): 
        return(f"{num2} is greater")
    
    else:
        return("both are equal")

# defining the calculator    



def calculator():
    print("WELCOME TO THE MODERN CALCULATOR\n".center(60))   

    print("CHOOSE THE FOLLOWING: ")
    print("1  ---------  ADDITION")
    print("2  ---------  SUBRACTION")
    print("3  ---------  MULTIPLICATION")
    print("4  ---------  DIVISION")
    print("5  ---------  MODULUS")
    print("6  ---------  COMPARISION (greater, lesser or equal.)")
    print("7  ---------  EXIT OR TURN OFF CALCULATOR.\n")
    
    valid_inputs=["1","2","3","4","5","6","7","exit","subraction","addition","multiplication","division", "modulus","comparision"]
            
    while True:
        select=input("enter the task you want to perform or exit the calculator:  ".capitalize().strip())
#strip function is used to remove the unintentional spaces in the given input by user
        
        if select=="7" or select=="exit":
                print("You exited the caculator")
                break               

        else:
                    
                if (select.lower() in valid_inputs ): 
                
                    try:

                        num1=int(input("Enter The First Number: "))
                        num2=int(input("Enter The Second Number: "))

            
                        if select=="1" or select.lower()=="addition":
                            add= addition(num1,num2)  
                            print(add,"\n") 
                           
#remember dont use return function inside the loop
# because it will terminate the program without further processing

                        elif (select=="2" or select.lower()=="subraction"):
                            sub=   subraction(num1,num2)
                            print(sub,"\n")
                        

                        elif(select=="3" or select.lower()=="multiplication"):
                            mul = multiplication(num1,num2)   
                            print(mul,"\n")
                        
                        elif(select=="4"or select.lower()=="division"): 
                            div=division(num1,num2)
                            print(div,"\n")
                        
                        elif(select=="5" or select.lower()=="modulus"):
                            mod=modulus(num1,num2)
                            print(mod,"\n")
                        
                        elif(select=="6"or select.lower()=="comparision"):
                            comp=compare(num1,num2) 
                            print(comp,"\n")

                

                        else:
                            print("invalid input\n")
                        

                    except(ValueError):
                        print("invalid input") 

                    except Exception as e:
                        print(f"invalid input: {e}\n")       
                
                else:
                    print("invalid task\n")

    
        
            

calculator()     