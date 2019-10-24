names = []
length = 10
while len(names) < length:
    name = input("Enter a name ")
    names.append(name)
while True:
    search = input("enter search name or 'End' to end the game:")
    if search in names:
        print("The name was found")
        break
    elif search == "End":
        print("The Game is Over")
        break
    else:
        print("The name was not found")
   

