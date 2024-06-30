task = input("Enter your task: ")
priority = input("Priority (high/ medium/ low): ")
time_bound = input("Is it time-bound? (yes/ no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that needs to be completed in a timely manner")

    case "medium":
        print(f"'{task}' is a medium priority task that needs to be completed in a timely manner.")

    case "low":
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")