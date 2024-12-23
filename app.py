while True:
    try:
        number = int(input("Enter a number to check whether even: "))
        if number % 2 == 0:
            print(f"{number} is even")

        else:
            print(f"{number} is odd")

    except:
        print("Please enter a number only.")