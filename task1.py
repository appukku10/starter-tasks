import csv
import hashlib

def create_csv_file():
    with open('userdata.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'hashedpw']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:  
            writer.writeheader()

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest() 
    return hashed_password

def register_user(username, password):
    hashed_password = hash_password(password)

    with open('userdata.csv', 'a', newline='') as csvfile:  
        fieldnames = ['username', 'hashedpw']  
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'username': username, 'hashedpw': hashed_password})  
                       
    print(f"User {username} registered successfully :)")

def login_user(username, password):
    hashed_password = hash_password(password)

    with open('userdata.csv', 'r') as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username and row['hashedpw'] == hashed_password:
                print(f"Hello, welcome back >.< {username}! Successfully logged in ")
                return True
    print("Password and username not matching")
    return False

def main():
    create_csv_file()
    
    while True:  
        print("\nEnter your choice:")
        print("Press 1 for registration")
        print("Press 2 for login")
        print("Press 3 to exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_user(username, password)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Press 1, 2, or 3.")

if __name__ == "__main__":
    main()


    
    

