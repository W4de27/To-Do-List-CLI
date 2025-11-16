"""
To-Do List CLI Program v2.0
Author: W4de27
Description:
A modern, animated, persistent To-Do List manager using JSON storage.
UI fully upgraded with clean structure, icons, animations, and error handling.
"""

import json
import time
import os
import sys


# =================================================================
#                       JSON FILE DETECTION
# =================================================================
base_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_path, "todo.json")


# =================================================================
#                           UTILITIES
# =================================================================

def pause():
    print()
    input("Press Enter to continue...")
    time.sleep(1)

def error(msg):
    print()
    print(f"❌ {msg}")
    time.sleep(2)
    pause()

def animate(word, repeats=3, delay=0.5):
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)
        print(f"\r{word}{dots}  ", end='', flush=True)
        time.sleep(delay)
    print()

def slow_print(text, delay=0.009):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def separator():
    print("\n" + "-" * 40 + "\n")




# =================================================================
#                         ONE-TIME HEADER
# =================================================================
def show_logo_once():
    separator()
    slow_print("████████╗  ██████╗  ██████╗   ██████╗ ")
    slow_print("╚══██╔══╝ ██╔═══██╗ ██╔═══██ ██╔═══██╗")
    slow_print("   ██║    ██║   ██║ ██║   ██╗██║   ██║")
    slow_print("   ██║    ██║   ██║ ██║   ██║██║   ██║")
    slow_print("   ██║    ╚██████╔╝ ██████╔╝ ╚██████╔╝")
    slow_print("   ╚═╝     ╚═════╝  ╚═════╝   ╚═════╝ ")
    print()
    slow_print("    ⭐ TO-DO LIST MANAGER v2.0 ⭐", 0.02)
    separator()
    time.sleep(2)


# =================================================================
#                      JSON: LOAD & SAVE
# =================================================================

def load_tasks():
    """Load tasks from JSON (auto-create if missing)."""
    if not os.path.exists(json_path):
        return []

    try:
        with open(json_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON."""
    with open(json_path, "w") as file:
        json.dump(tasks, file, indent=4)


# =================================================================
#                       MAIN FEATURE SET
# =================================================================
def add_task(tasks):
    task = input("+ Enter new task: ").strip().capitalize()
    print()

    if not task:
        error("Task should not be empty!")
        return

    animate("Adding task", repeats=3, delay=0.5)
    time.sleep(1)

    tasks.append(task)
    save_tasks(tasks)

    print("✔ Task added successfully!")
    pause()


def view_tasks(tasks):
    animate("Loading tasks", repeats=3, delay=0.5)
    time.sleep(1)
    

    if not tasks:
        error("No tasks to display.")
        return
    print()
    print("=" * 40)
    print(f"{'📌 YOUR TO-DO TASKS':^40}")
    print("=" * 40)
    time.sleep(1)

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
        time.sleep(0.5)

    time.sleep(1)
    separator()
    print("✔ Tasks displayed successfully!")
    time.sleep(1)
    pause()


def delete_task(tasks):
    animate("Loading", repeats=3, delay=0.5)
    if not tasks:
        error("No tasks to delete!")
        return

    separator()
    print("🗑 Delete Task Options: \n")
    print("1. Delete by task name")
    print("2. Delete by number")
    print("3. Cancel")
    separator()

    choice = input("Choose (1/2/3): ").strip()

    # ---------------- Delete by Name ----------------
    if choice == "1":
        name = input("Enter task name: ").strip().capitalize()

        if name in tasks:
            print()
            animate("Deleting task", repeats=3, delay=0.5)
            time.sleep(1)
            tasks.remove(name)
            save_tasks(tasks)
            print("✔ Task deleted successfully!")
            pause()
        else:
            error("Task not found!")
        return

    # ---------------- Delete by Number ----------------
    elif choice == "2":
        view_tasks(tasks)
        try:
            num = int(input(f"Choose number (1 - {len(tasks)}): "))
            

            if not (1 <= num <= len(tasks)):
                error("Invalid task number!")
                return
            print()
            animate("Deleting task", repeats=3, delay=0.5)
            time.sleep(1)
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("✔ Task deleted successfully!")

        except ValueError:
            error("Please enter a valid number!")
            return

        pause()
        return

    # ---------------- Cancel ----------------
    elif choice == "3":
        animate("Cancelling", repeats=3, delay=0.5)
        pause()
        return

    else:
        error("Invalid selection!")


def clean_tasks(tasks):
    if not tasks:
        error("No tasks to clean!")
        return
    
    print()
    animate("Cleaning tasks", repeats=3, delay=0.5)
    time.sleep(1)

    tasks.clear()
    save_tasks(tasks)

    print("✔ All tasks cleaned successfully!")
    pause()


# =================================================================
#                             MAIN LOOP
# =================================================================
def main():
    tasks = load_tasks()

    show_logo_once()  # Show once only at startup

    is_running = True
    while is_running:
        print("=" * 40)
        print(f"{'📌 MAIN MENU':^40}")
        print("=" * 40)
        print("1. ➕ Add a New Task")
        print("2. 📋 Display All Tasks")
        print("3. ❌ Delete a Task")
        print("4. 🧹 Clean All Tasks")
        print("5. 🚪 Exit")
        separator()

        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                add_task(tasks)

            elif choice == "2":
                view_tasks(tasks)

            elif choice == "3":
                delete_task(tasks)

            elif choice == "4":
                clean_tasks(tasks)

            elif choice == "5":
                for i in range(3):
                    print("Exiting" + "." * (i + 1))
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                print("\n Saving and exiting...")
                time.sleep(1)
                print("✔ Goodbye! Have a wonderful day! 👋 \n")
                time.sleep(1)
                is_running = False
            else:
                error("Invalid menu choice!")
        except KeyboardInterrupt:
            print("\n \n Saving and exiting...")
            time.sleep(1)
            print("✔ Goodbye! Have a wonderful day! 👋 \n")
            sys.exit()



# =================================================================
#                        PROGRAM ENTRY
# =================================================================
if __name__ == "__main__":
    main()
