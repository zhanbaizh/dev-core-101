import json
import re

FILENAME = 'user_data.json'

def load_users():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_users(user_list):
    with open(FILENAME, 'w') as file:
        json.dump(user_list, file, indent=4)

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def add_user(user_list):
    name = input('Enter the name ')
    
    while True:
        age = input('Enter the age ')
        if age.isdigit():
            age = int(age)
            break
        else:
            print('Age must be an integer. Try again')
    while True:
        email = input('Enter the email ')
        if is_valid_email(email):
            break
        else:
            print('Email is not valid. Try again')
    user_data = {'name':name, 'age':age, 'email':email}
    user_list.append(user_data)
    print(f"User {name} is succesfully added")

def remove_user(user_list):
    name = input('Enter the user who must be eliminated: ')
    for user in user_list:
        if user['name'] == name:
            user_list.remove(user)
            print(f"The user {name} is eliminated")
            break
        print(f"The user {name} is not found")
    
def display_users(user_list):
    if not user_list:
        print("The list is empty.")
    else:
        print("Information about all off the users:")
        for user in user_list:
            print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")

def main():
    users = load_users()

    while True:
        print("\nMenu: ")
        print('1. add user')
        print('2. delete user')
        print('3. show all users')
        print('4. exit')

        choice = input('Please choose menu: ')

        if choice == '1':
            add_user(users)
        elif choice == '2':
            remove_user(users)
        elif choice == '3':
            display_users(users)
        elif choice == '4':
            save_users(users)
            print('The data is saved. Exit')
            break
        else:
            print('You entered wrong number. Try again')

if __name__ == "__main__":
    main()