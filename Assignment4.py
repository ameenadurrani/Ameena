num1 : int
num2 : int
num3 : int
name : str 
name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
print(f"Hello, {name}! Let's explore your favorite numbers:")
fav_num = [num1,num2,num3]
for i in fav_num:
    if (i%2 == 0):
        print(f"The number {i} is even.")
    elif (i%2 != 0):
        print(f"The number {i} is odd.")    
for i in fav_num:
    print(f"The number {i} and its square: ({i}, {i ** 2})")
totalSum = sum(fav_num)
print(f"Amazing! The sum of your favorite numbers is: {totalSum}")
