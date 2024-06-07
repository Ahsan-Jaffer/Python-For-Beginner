
# i=1
# num =int (input("Enter the Number : "))
# while i<=10:
    
#     print(f'{num} * {i} = {num*i}')
#     i = i + 1 

                     #CAR GAME
instruction = ""
while instruction != "quit":
    instruction = input(">").lower()
    if instruction.lower() == "start":
        print("car started ... Ready to go!")
    elif instruction.lower() == "help":
        print('start - to start the car')
        print('stop - to stop the car ')
        print("quit - to exit")
    elif instruction == "quit":
        break

    else:
       print("I don't understand that ...")



    