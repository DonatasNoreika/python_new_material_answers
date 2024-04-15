privileged_users = ['Tomas', "Domas", "Vytautas"]

name = input("Enter your name: ")

if name in privileged_users:
    print(f"Hello, {name}. You're VIP user.")
else:
    print("Hello")
