started = False

while True:
    command = input("> ")

    if command.lower() == "help":
        print("start - to start the car \n"
              "stop - to stop the car \n"
              "quit - to exit")

    elif command.lower() == "start":
        if started:
            print("Car has already started!")
        else:
            print("Car started...Ready to go!")
            started = True
    elif command.lower() == "stop":
        if not started:
            print("Car already stopped.")
        else:
            print("Car stopped.")
            started = False
    elif command.lower() == "quit":
        print("Exiting...")
        break
    else:
        print("I don't understand that...")
