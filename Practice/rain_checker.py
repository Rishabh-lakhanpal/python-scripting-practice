import time

name = input("What is your name: ")

while True:
    is_raining = input(f"Hello, {name}, is it raining (Y/N)? ").lower()
    
    if is_raining == "y":
        has_umbrella = input("Do you have an umbrella (Y/N)? ").lower()
        
        if has_umbrella == "y":
            print("You can go outside with your umbrella.")
            break
        else:
            print("Wait a while.")
            time.sleep(5)
            print("Done waiting")
    elif is_raining == "n":
        print("You can go outside.")
        break
    else:
        print("Please enter Y or N.")