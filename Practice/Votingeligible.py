name = input("What is your name: ").strip()
age = int(input("What is your age: "))

if age < 18:
    print("Hello, ", name,"You are Not eligible for voting")
else:
    print("Hello, ",name, "You are eligible for voting")
