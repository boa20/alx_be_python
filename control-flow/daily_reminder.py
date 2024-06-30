Task = input("Enter your task: ")
Priority = input("Priority (high/ medium/ low): ")
Time_bound = input("Is it time-bound? (yes/ no): ")

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a high priority task that needs to be completed in a timely manner")

    case "medium":
        print(f"'{Task}' is a medium priority task that needs to be completed in a timely manner.")

    case "low":
        print(f"'{Task}' is a low priority task. Consider completing it when you have free time.")