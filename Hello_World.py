# Hello World by Sean Layton

# Developer practice in session

number_choice = int(input("Please pick a number between [1-10] "))
Hello = range(1,10)

if number_choice in Hello:
    print("Hello World")
else:
    print("Goodbye World")
    raise SystemExit(1)
