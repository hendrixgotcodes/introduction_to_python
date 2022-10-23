appIsRunning = True
carRunning = False

while appIsRunning:
    userInput = input("> ").lower()
    if userInput == "start":
        if carRunning:
            print("Car has already started")
        else:
            print("Car started")
            carRunning = True
    elif userInput == "stop":
        if not carRunning:
            print("car is not running")
        else:
            print("Car stopped")
            carRunning = False
    elif userInput == "quit":
            print("quitting. bye")
            break;
    elif userInput == "help":
        print('''
            stop - stop car
            start - start car
        ''')
    else:
        print("invalid command")