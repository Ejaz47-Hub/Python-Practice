def greetings():
    word = input("Greeting:")
    if word.startswith('Hello'):
        print('$0')
    elif word.startswith('H'):
        print('$20')
    elif word.startswith("W"):
        print("$100")
    else :
        print('Error')
greetings()