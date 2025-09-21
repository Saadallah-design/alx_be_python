
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task but not time-bound. You can schedule it for later.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is medium priority and should be addressed soon.")
        else:
            print(f"Reminder: {task} is medium priority.")
    case "low":
        if time_bound == "no":
            print(f"Note: {task} is a low priority task. You can schedule it for later.")
        else:
            print(f"Reminder: {task} is not time-bound. This is a low priority task.")
    case _:
        print("Invalid priority level. Please choose high, medium, or low.")    