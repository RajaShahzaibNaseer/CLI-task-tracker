import sys
import json
from collections import defaultdict

# todo:
# get insertion working (done)
# have persistent execution (done)
# get multiple insertion working (done)
# make updates (done) 
# fix exit not exiting (done)
# make a display for list of tasks
# convert insertion into a function for sepearation

def add(tasks,id,description,status,created_at,updated_at):
    tasks["id"].append(id)
    tasks["description"].append(description)
    tasks["status"].append(status)
    tasks["createdAt"].append(created_at)
    tasks["updatedAt"].append(updated_at)

def update(tasks,task_id,field_to_update,updated_value):
    tasks[field_to_update][task_id] = updated_value
    

    
def main():
    tasks = defaultdict(list)
    working = True
    task_id = 0
    while working:
        choice = input("what do you want to do")
        if choice == "add":
            description = input("Please enter the description")
            status = input("Please enter the status of your task")
            created_at = "2025-11-12"
            updated_at = "2025-11-12"

            add(tasks,task_id,description,status,created_at,updated_at)

            task_id += 1

            print(tasks)

        if choice == "update":
            update_task = input("what task are you trying to update? ")
            update_field = input("what field are you trying to update? ")
            updated_value = input("enter the new value? ")
            update(tasks,int(update_task),update_field,updated_value)
            
        if choice == "exit":
            working = False
            

main()
