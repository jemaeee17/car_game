started = False

while True:
    command = input("> ").lower()

    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)

    elif command == "start":
        if started:
            print("Car has already started!")
        else:
            print("Car started...Ready to go!")
            started = True
    elif command == "stop":
        if not started:
            print("Car already stopped.")
        else:
            print("Car stopped.")
            started = False
    elif command == "quit":
        print("Exiting...")
        break
    else:
        print("I don't understand that...")
