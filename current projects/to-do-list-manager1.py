

# for widget

def view_task(task_list):
    if len(task_list)==0:
        print("\n...No available task at this moment...\n")
        print("\n")

    else:           # here we can use enumerate() function to assign numbers to each element i
                    # in the list

        print("\n...Tasks currently available:\n ")
        for index, item in enumerate(task_list,start=1):
            print(f"{index} : {item}")  
            print("\n")

def add_task(task_list,taskinput):
   task_list.append(taskinput)
   print("\n...task is added successfully...\n")
   print("\n")

def remove_task(task_list,taskremove):
    number_to_remove=taskremove-1
    task_list.pop(number_to_remove)
    print("\ntask is succesfully removed\n ")
    print("\n")

# def mark_task(task_list,taskid):
#     if taskid<=len(task_list) and taskid>0:
#         completed_task=task_list(taskid-1) + "(completed)"
#         print(f"{completed_task} is marked as complete")
    
#     else:
#         print("invalid task number")


    
def to_do_list_manager():
    task_list=[]  # empty list for to store the tasks
    while True:
        print("WELCOME TO THE 'TO DO LIST MANAGER'\n".center(60))
        print("MENU:")
        print("1   ---------   View Task")
        print("2   ---------   Add Task")
        print("3   ---------   Remove Task")
        # print("4   ---------   Mark Task")
        print("4   ---------   Exit \n")

        valid_inputs=["1","2","3","4","5","viewtask","addtask","removetask","marktask","exit"]
        try:
            choice1=input("\nWhat task do you want to perform or exit: ")

            choice=choice1.replace(" ","")
            if choice=="exit" or choice==4:
                break
            else:
            
                if choice in valid_inputs: 
                    if choice=="1" or choice.lower()=="viewtask":
                        view_task(task_list)
        
                    elif choice=="2" or choice.lower()=="addtask":

                        taskinput=input("Task Description: ")
                        add_task(task_list,taskinput)

                    elif choice=="3" or choice.lower()=="removetask":
                        taskremove=int(input("\nEnter the number of the task you want to remove: "))
                        remove_task(task_list,taskremove)

                # elif choice=="4" or choice.lower()=="marktask":
                #     taskid=int(input("Enter the task id you want to mark as completed: "))

                #     mark_task(task_list,taskid)

                else:
                    print( "\ninvalid input\n")    

        except ValueError:
            print("invalid input")    

        except Exception as e:
            print(f"{e} is an invalid input")   
            



    
    
    
    
    


to_do_list_manager()  

