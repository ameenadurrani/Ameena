                  #menu
print("___________________menu_____________________________")
print("Enter 1 to add two numbers.")
print("Enter 2 to subtract two numbers.")
print("Enter 3 to multiply two numbers,")
print("Enter 4 to divide two numbers.")
print("Enter 5 to quit.")
print("_____________________________________________________")
choice :int = int(input("Enter Your Choice: "))
num1 : int
num2 : int
while (choice!=5):
        if(choice == 1):
          num1  = int(input("Enter a number: "))
          num2  = int(input("Enter a number: "))
          sum = num1 + num2
          print(f"The sum of two numbers is: {sum}")

        if(choice==2):
          num1 = int(input("Enter a number: "))
          num2  = int(input("Enter a number: "))
          sub = num1 - num2
          print(f"The difference of two numbers is: {sub}")

        if(choice==3):
           num1 = int(input("Enter a number: "))
           num2  = int(input("Enter a number: "))
           mul = num1 * num2
           print(f"The product of two numbers is: {mul}")

        if(choice==4):
          num1 = int(input("Enter a number: "))
          num2  = int(input("Enter a number: "))
          div : float = num1 / num2
          print(f"The divisor of two numbers is: {div}")

        choice = int (input("Enter your Choice: "))  

if(choice == 5):
   print("Thank you for using my calculator!")



