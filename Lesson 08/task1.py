name = "Donatas"
password = "123456"

while True:
    enter_name = input("Enter name: ")
    enter_pass = input("Enter password: ")
    if enter_name == name and enter_pass == password:
        print("Welcome!")
        break
    else:
        print("Wrong. Try again.")
