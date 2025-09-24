import json
import os
while True:
    def main():
        action = input("Insert the action add/list/delete/update/status/quit: ").lower()
        if action == "add":
            add_task()
        elif action == "list":
            list_task()
        elif action == "delete":
            delete_task()
        elif action == "update":
            update_task()
        elif action == "status":
            status_task()
        elif action == "quit":
            quit()
        else:
            print("Invalid action. choose, add, list, delete, update, status, quit.")
    file = "task.json"

    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)
            
    with open(file, "r") as f:
        task = json.load(f)
        
    def add_task():
        new_task_d = input("New Task: ")
        new_task = {
            "id": len(task) + 1,
            "description": new_task_d,
            "status": "pending"     
        }
        task.append(new_task)
        with open(file, "w") as f:
            json.dump(task, f, indent=4)
        print("Task added successful")

    def list_task():
        with open(file, "r") as f:
            tasks = json.load(f)
        if len(tasks) == 0:
            print("No tasks found")
            return

        for task_item in tasks:
            print(f"ID: {task_item['id']}")
            print(f"Description: {task_item['description']}")
            print(f"Status {task_item['status']}")
            print("-" * 20)
    def delete_task():
        with open(file, "r") as f:
            task = json.load(f)
        
        id_to_delete = int(input("Enter the ID of the task to delete: "))
        
        task_found = False
        for task_item in task:
            if task_item['id'] == id_to_delete:
                task.remove(task_item)
                task_found = True

                with open(file, "w") as f:
                    json.dump(task, f, indent=4)
        if task_found:
            print("Task deleted succesfully")
        else:
            print("Task not found")
    def update_task():
        with open(file, "r") as f:
            task = json.load(f)
        id_to_update = int(input("Enter the ID of the task to update: "))

        new_description = input("Enter new description: ")

        task_found = False
        for task_item in task:
            if task_item['id'] == id_to_update:
                task_item['description'] = new_description
                task_found = True
                
        with open(file, "w") as f:
            json.dump(task, f, indent=4)
        
        if task_found:
            print("Task updated successfully")
        else:
            print("Task not found")
    def status_task():
        with open(file, "r") as f:
            task = json.load(f)
            
        id_to_change = int(input("Enter the ID of the task to change status: "))
        
        new_status = input("Enter new status(pending/in progress/done:)").lower()
        
        if new_status not in ["pending", "in progress", "done"]:
            print("Invalid status choose 'pending', 'in progress', 'done'. ")
            return
        
        task_found = False
        for task_item in task:
            if task_item['id'] == id_to_change:
                task_item['status'] = new_status
                task_found = True
                
        with open(file, "w") as f:
            json.dump(task, f, indent=4)
            
        if task_found:
            print("Task status updated succesfully")
        else:
            print("Task not found")
    main()