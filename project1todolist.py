def task():
    tasks=[]
    print("welcome to the to-do list ")
    total_task=int(input("enter a how many task you want add"))
    for i in range(1,total_task+1):
        task_name=(input(f"enter you task {i}="))
        tasks.append(task_name)
    print(f"task are\n {tasks}")
    while True:
        operation=int(input("enter 1-Add\n2-update\n3-delete\n4-view\n5-exit/stop"))
        if operation==1:
            add=input("enter a new task=")
            tasks.append(add)
            print(f"you task {add} successfully added")
        elif operation==2:
            update_val=input("enter the task name you want to update=")
            if update_val in tasks:
                up=input("enter a new tasks=")
                ind=tasks.index(update_val)
                tasks[ind]=up
                print(f"your task {ind} updated successfully")
        elif operation==3:
           del_val=input("which want to deleted=")
           if del_val in tasks:
               ind=tasks.index(del_val)
               del tasks[ind]
               print(f"task {del_val} is deleted successfully")
        elif operation==4:
           print(f"total tasks = {tasks}")
        elif operation==5:
           print("closing the program")
           break
        else:
           print("invalid input")
task()
