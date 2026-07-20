print("My first Calculator".center(50))  #Basic Calculator for performing general mathematical operations
# while True:                      #Using While Loops
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('5',):
        print("Exiting the calculator")
        break            #Break is used to stop the programme right away
    elif choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero")
            else:
                print(f"Result: {num1 / num2}")
            else:
                print(f"Rsult: {num1 / num2}")    

    else:
        print("Invalid choice. Please try again.")
     
