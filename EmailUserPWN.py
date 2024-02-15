import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def run_script(script_name, *args):
    try:
        subprocess.run(["python", script_name, *args], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error running {script_name}: {e}")
        exit()

def run_all_scripts(email, username):
    run_script("PWNER.py", "-e", email)
    run_script("UFINDER.py", "-u", username)
    run_script("BreachedCredCheck.py")

def print_menu():
    print(f"{Fore.BLUE}{Style.BRIGHT}=== Menu ===")
    print("1. Run PWNER.py")
    print("2. Run UFINDER.py")
    print("3. Run BreachedCredCheck.py")
    print("4. Run All")
    print("===================")

# Get user input for email
email = input("Enter the email for OSINTPWD2: ")

# Get user input for username (you can replace this with your logic)
username = input("Enter the username for UFINDER.py: ")

# Display the menu and get user choice
while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        run_script("PWNER.py", "-e", email)
    elif choice == '2':
        run_script("UFINDER.py", "-u", username)
    elif choice == '3':
        run_script("BreachedCredCheck.py")
    elif choice == '4':
        run_all_scripts(email, username)
    else:
        print(f"{Fore.YELLOW}Invalid choice. Please enter a number from 1 to 4.")
        continue

    break  # exit the loop after a valid choice
