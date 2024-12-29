def view_task(list_task):
    if len(list_task)==0:
        print("there are no tasks currently available")
    
    
    

def add_task():
    list1=["Bring water bottle", "Steal somethings from someone"]
    taskadd1=to_do_list_manager()
    list1.append(taskadd1) 
    



def to_do_list_manager():
    print("WELCOME TO THE 'TO DO LIST MANAGER'\n".center(60))
    print("MENU:")
    print("1   ---------   View Task")
    print("2   ---------   Add Task")
    print("3   ---------   Remove Task")
    print("4   ---------   Mark Task")
    print("5   ---------   Exit ")

    list_task=[1]

    valid_inputs=["1","2","3","4","5","viewtask", "addtask","removetask", "marktask", "exit" ]
    
    while True:

        choice1=input("What Task You Want To Perform or Exit: ")
        choice=choice1.replace(" ","")

        if choice in valid_inputs:
            if (choice=="1" or choice.lower()=="viewtask"):
                task1=view_task(list_task)
                print(task1)

            elif (choice=="2" or choice.lower()=="addtask"):
                taskadd=input("Task description: ")
                return taskadd
                
                   














to_do_list_manager()
