def convert(text):
    return text.replace(':)','😊').replace(':(','🙁 ')

def main():
    word = input("Enter Ths string & Emoji :")
    print(convert(word))
main()