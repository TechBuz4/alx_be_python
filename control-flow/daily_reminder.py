"""
This script will ask the user for a single task, its priority level, and if it is time-sensitive. 
The program will then provide a customized reminder for that task, demonstrating control flow 
and loops without relying on data structures to store multiple tasks."""

#prompting user for inputs
task = input("Enter the task:")
priority = input("Priority (high/medium/low):")
time_sensitive = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if time_sensitive == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it asap")
    case "medium":
        if time_sensitive == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it soon")
    case "low":
        if time_sensitive == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it when you have free time.")
