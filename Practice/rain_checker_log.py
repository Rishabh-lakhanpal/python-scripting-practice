import time 

log_file = "logs/rain_decision_log.txt"

def log(message):
    timestamp = time.strftime("%y-%m-%d %H:%M:%S")
    with open(log_file,"a") as file:
        file.write(f"[{timestamp}] {message}\n")

print("Welcome to the Rain Decision Assistant! \n")

name = input("What is your name? ").strip().title()
log(f"User name: {name}")

while True:
    is_raining_input = input(f"\nHello, {name}! Is it raining outside? (Y/N): ").strip().lower()
    log(f"Is it raining? → {is_raining_input}")

    if is_raining_input == 'y':
        has_umbrella_input = input("Do you have an umbrella? (Y/N): ").strip().lower()
        log(f"Do you have an umbrella? → {has_umbrella_input}")

        if has_umbrella_input == 'y':
            print("\n You can go outside with your umbrella. Stay dry!")
            log("Decision: Go outside with umbrella.")
            break
        elif has_umbrella_input == 'n':
            print("\n Please wait a while. It may stop raining soon...")
            log("Decision: User told to wait.")
            time.sleep(3)
        else:
            print(" Please enter only 'Y' or 'N' for the umbrella question.")
            log("Invalid input for umbrella.")
    elif is_raining_input == 'n':
        print("\n It's not raining. You can go outside freely!")
        log("Decision: Go outside. No rain.")
        break
    else:
        print(" Please enter only 'Y' or 'N' for the rain question.")
        log("Invalid input for rain.")