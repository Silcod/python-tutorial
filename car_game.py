game_command = input("Type your command ")


if game_command == "start":
    print("Car started... Ready to go!")
elif game_command == "stop":
    print("Car stopped")
elif game_command == "quit":
    print("program terminated")
else:
    print("I don't understand that...")

#===========Using While Loop===============
#Note: in programming we have what we call DRY (Don't repeat yourself)
#So if you are repeating yourself you're doing something wrong

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")