# print("Hello World")
name = input("Enter The Name :")
print('The Name is',name)


def ejaz():
    a = input("Enter The Name :")
    a.strip().title()
    print(f"Nigga {a}")
ejaz()

def calc():
    x = int(input("Enter The Number For Square"))
    print(f"The Square is {square(x)}")

def square(n):
    return n*n
calc()