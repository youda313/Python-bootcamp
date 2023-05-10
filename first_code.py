def hello(username):
    print("Hello " + username)

def input_username():
    username = input("Enter your username: ")
    return username

def main():
    username = input_username()
    hello(username)

main()

