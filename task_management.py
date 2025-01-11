from errors import UserInputEmpty
from errors import CommandNotFound

#defined a function for adding a task
def add_task(new_task,list):
    status="Incomplete"
    list.append(new_task + ": " + status)
    return print(f"\n{new_task} added!")

#defined a function for viewing tasks
def view_tasks(list):
    return print ("\nYour To-Do List:",*list,sep="\n")

#defined a function to mark a task as complete if the task is in the list. If not, it returns text.
def complete_task(selected_task,list):
    for task in list:
        if selected_task in task:
            selected_task=task.replace("Incomplete","Complete")
            index=list.index(task)
            list[index]=selected_task
            return print (f"\n{selected_task}! Congratulations!")
    return print(f"\n{selected_task} not on list!")

#defined a function to delete a task if the task is in the list. If not, it returns text.
def delete_task(selected_task,list):
    for task in list:
        if selected_task in task:
            index=list.index(task)
            list.pop(index)
            return print (f"\n{selected_task} removed!")
    return print(f"\n{selected_task} not on list!")

#made the menu a function so that it could be more easily called and printed
def UI():    
    
    #assigned an empty value as the start of the list for the application to alter and printed the initial menu
    to_do_list = []

    menu=("""
        Welcome to the To-Do List App!

            Menu:
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit
        
        """)
    while True:     
    #implemented a try block to handle exceptions throughout the program
        try:
            print(menu)   
            #called for the user to input a command based on what is listed in the menu and converted the response to lower case for easier comparisons
            feature_request=input("Which menu option would you like to perform?\nPlease enter menu option corresponding number:\n")             
            #implented a quit function to exit the loop
            if feature_request == "5":
                break
            #used a comparison statement to add a task, which returns an error which is handled with an exception later if the input is empty and calls the add_task function if the user inputs a task    
            elif feature_request == "1":
                new_task=input("\nWhat task would you like to add:\n")
                if new_task == "":
                        raise UserInputEmpty()
                else:
                    add_task(new_task,to_do_list)
            #used a comparison statement to call the view task function if the condition is met  
            elif feature_request == "2":
                view_tasks(to_do_list)
            #used a comparison statement to mark a task as complete, which returns an error which is handled with an exception later if the input is empty and calls the complete_task function if the user inputs a task  
            elif feature_request == "3":
                task_to_complete=input("\nWhat task did you complete?\nMakes sure to enter name as it appears in list:\n")
                if new_task == "":
                        raise UserInputEmpty()
                else:
                    complete_task(task_to_complete,to_do_list)
            #used a comparison statement to remove a task, which returns an error which is handled with an exception later if the input is empty and calls the delete_task function if the user inputs a task
            elif feature_request == "4":
                task_to_delete=input("\nWhat task would you like to remove?\nMakes sure to enter name as it appears in list:\n")
                if new_task == "":
                        raise UserInputEmpty()
                else:
                    delete_task(task_to_delete,to_do_list)
            #implemented and elif and else statement to raise an error respectively if the user leaves the input blank or the command doesn't match one of the comparisons
            elif feature_request == "":
                raise UserInputEmpty()        
            else:
                raise CommandNotFound()
        #implemented an exception to handle when the user enters nothing
        except UserInputEmpty:
            UserInputEmpty.handle_user_input_empty()
        #implemented an exception to handle when the user enters a command that doesn't match the options
        except CommandNotFound:
            CommandNotFound.handle_command_not_found()
    #printed one final version of the list for the user before exiting the program
    print("\nYour To-Do List:",*to_do_list,sep="\n")