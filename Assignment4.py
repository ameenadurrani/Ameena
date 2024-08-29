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
tuples_list : list = []
for i in fav_num:
    if (i%2 == 0):
        print(f"The number {i} is even.")
        tuple = (i,'even') 
    elif (i%2 != 0):
        print(f"The number {i} is odd.")    
        tuple =(i,'odd')
    tuples_list.append(tuple)
       
print(tuples_list)
for i in fav_num:
    print(f"The number {i} and its square: ({i}, {i ** 2})")
totalSum = sum(fav_num)
print(f"Amazing! The sum of your favorite numbers is: {totalSum}")
is_prime = True
if totalSum > 1:
    for j in range(2, int(totalSum**0.5) + 1):
        if totalSum % j == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"Wow, {totalSum} is a prime number!")
else:
    print(f"Wow, {totalSum} is not a prime number!")  

print("\nSummary of your favorite numbers:")
for item in tuples_list:
    print(item)