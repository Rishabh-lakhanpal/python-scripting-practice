import csv
import os
import time

FOLDER = 'users'
FILENAME = os.path.join(FOLDER, 'users.csv')

os.makedirs(FOLDER, exist_ok=True)

def user_exists(username, email):
    if not os.path.exists(FILENAME):
        return False
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username or row['email'] == email:
                return True
    return False

def register_user(username, email, password):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['username', 'email', 'password', 'timestamp'])
        writer.writerow([username, email, password, timestamp])
    print(f" User '{username}' registered successfully at {timestamp}")

username = input("Enter username: ")
email = input("Enter email: ")
password = input("Enter password: ")

if user_exists(username, email):
    print(" Username or email already exists. Try again.")
else:
    register_user(username, email, password)
