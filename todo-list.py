import time

def main():
    tasks = []
    is_running = True

    def add_task():
        task = input("Add New Task Name: ").capitalize()

        if task == "":
            print("❌ ERROR! Task Should Not Be Empty!")
        else:
            tasks.append(task)
            print("Task In Progress...")
            time.sleep(2)
            print("Task Added Successfuly ✔")

    def view_task():
        print("Checking Tasks...")
        time.sleep(2)git
        
        print()
        if len(tasks) == 0:
            print("❌ ERROR! No Task To Display.")
        else:
            
            print("|----------------------|")
            for x in range(len(tasks)):
                print(f"|- {x + 1}. {tasks[x]}")
            print("|----------------------|")
            print()
            print("Tasks Displayed Successfuly ✔")

    def delete_task():
        try:
            print()
            print("Checking...")
            time.sleep(1)
            if len(tasks) == 0:
                print("❌ ERROR! No Tasks To Delete! ")
            else:
                print()
                print("********************************")
                print()
                print("1. Delete Using Name Of Task")
                print("2. Delete Using Number Of List")
                print("3. Cancel")
                print()
                print("********************************")
                print()

                choices = input("Enter Number Of The Method (1/2/3): ")

                if choices == "1":
                    print()
                    print("Checking...")
                    time.sleep(1)
                    n_task = input("Enter Name Of Task: ").capitalize()
                    if n_task in tasks:
                        print("Deleting Task...")
                        tasks.remove(n_task)
                        time.sleep(2)
                        print("Task Deleted Successfuly ✔")
                    else:
                        print("❌ ERROR! Task Not Exist!")
                elif choices == "2":
                    print("|----------------------|")
                    for x in range(len(tasks)):
                        print(f"|- {x + 1}. {tasks[x]}")
                    print("|----------------------|")
                    print()
                    time.sleep(1)
                    task = int(input(f"Choose Task Between (1 - {len(tasks)}): "))

                    if task <= 0 or task > len(tasks):
                        print("❌ ERROR! Invalid Task!")
                    else:
                        print("Deleting Task...")
                        tasks.remove(tasks[task - 1])
                        time.sleep(2)
                        print("Task Deleted Successfuly ✔")
                elif choices == "3":
                    print("Cancelling...")
                else:
                    print("❌ ERROR! Invalid Choice!")

        except IndexError:
            print("❌ ERROR! Invalid Task!")
        except ValueError:
            print("❌ ERROR! Invalid Task!")

    while is_running:
        print()
        print("******** To-Do List CLI ********")
        print()

        print("1. Add a New Task")
        print("2. Display All Tasks")
        print("3. Delete a Task")
        print("4. Clean The Tasks")
        print("5. Exit")

        print()
        print("********************************")

        choice = input("Enter valid choice (1-5): ")


        if choice == "1":
            add_task()
            time.sleep(3)
        elif choice == "2":
            view_task()
            time.sleep(3)
        elif choice == "3":
            delete_task()
            time.sleep(3)
        elif choice == "4":
            print("Checking...")
            time.sleep(1)
            if len(tasks) == 0:
                print("No Tasks To Clean")
                time.sleep(2)
            else:
                print("Cleaning In Progress...")
                tasks.clear()
                time.sleep(2)
                print("Cleaning The Tasks Successfully! ✔")
                time.sleep(3)
        elif choice == "5":
            print("Thank You For Your Time!")
            time.sleep(1)
            print("You Have a Good Day!")
            time.sleep(1)
            print("GoodBye! 👋")
            is_running = False
            exit()
        else:
            print("Cheking...")
            time.sleep(1)
            print("❌ ERROR! Invalid Choice!")
            time.sleep(2)

    



if __name__ == "__main__":
    main()