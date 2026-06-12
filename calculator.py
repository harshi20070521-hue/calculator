while True:
    print("Welcome to the calculator!")
    n1= int(input("Enter the number:"))
    n2= int(input("Enter the number:"))
    print("Select the operation u want to perform:")
    print("1.ADDITION""\n 2.SUBTARCTION""\n 3.MULTIPLICATION""\n 4.DIVISION""\n 5.EXIT")
    choice= int(input("Enter the choice:"))
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        if b==0:
            return "Error: Division by zero is not allowed." 
        return a/b
    if choice==1:
        print("The result of addition is:",add(n1,n2))
    elif choice==2:
        print("The result of subtraction is:",sub(n1,n2))
    elif choice==3:
        print("The result of multiplication is:",mul(n1,n2))
    elif choice==4:
        print("The result of division is:",div(n1,n2))
    elif choice==5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")  
        