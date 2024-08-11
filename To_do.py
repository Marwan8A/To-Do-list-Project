import time
dict_of_tasks = {}

def add_task():
    name_to_add = input("Name of task: ").capitalize()
    if name_to_add not in dict_of_tasks:
        dict_of_tasks[name_to_add] = 'In Progress'                #Creates a new dictionary entry
        print("Task '" + name_to_add + "' added to To-Do list")
    else:
        print("Task already exists ")
    
def change_task_status():
    name_to_change = input("Name of task: ").capitalize()
    if name_to_change in dict_of_tasks:
        dict_of_tasks[name_to_change] = 'Completed'  
    
    else:
        print("Task not found")
          

def delete_task():
    name_to_delete = input("Name of task: ").capitalize()
    if name_to_delete in dict_of_tasks:
        del dict_of_tasks[name_to_delete]
        print("Task '"+name_to_delete+"' deleted from To-Do list")
    else:
        print("Task not found")

def reset_list():
    dict_of_tasks.clear()
    print("To-Do list has been reset")

def view_tasks():
    
    if len(dict_of_tasks)>0:
        print("\nNumber of tasks: "+ str(len(dict_of_tasks))+"\n")
        for key in dict_of_tasks:
            print('- ' + key + '\t\t' + dict_of_tasks[key])
            
    else:
        print("You have an empty To-Do list")

print("\n~ Welcome to To-Do-List ~")
print("_________________________")
while True:
    time.sleep(2)
    print("\n 'A' Add task")
    print(" 'C' Change task status")
    print(" 'D' Delete task ")
    print(" 'R' Reset tasks ")
    print(" '.' View all tasks ")
    print(" 'e' Exit To-Do list")
    user_input = input("Enter a command: ").upper()

    if user_input == 'A':
        add_task()
    elif user_input == 'C':
        change_task_status()
    elif user_input == 'D':
        delete_task()
    elif user_input == 'R':
        reset_list()
    elif user_input == '.':
        view_tasks()
    elif user_input == 'E':
        print("\nThank you for using my To-Do list!!\n")
        break
    else:
        print("\nInvalid Command\nPlease enter a valid command ")

