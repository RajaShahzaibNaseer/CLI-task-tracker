import sys
import json


def main():
    tasks = {}
    choice = input("what do you want to do")
    if choice == "add":
        description = input("Please enter the description")
        status = input("Please enter the status of your task")
        created_at = "2025-11-12"
        updated_at = "2025-11-12"
        tasks = {
            "id": 1,
            "description": description,
            "status": status,
            "createdAt": created_at,
            "updatedAt": updated_at
        }
        print(tasks)

main()
