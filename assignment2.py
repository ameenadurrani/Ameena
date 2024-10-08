
#Simple Message
message : str = "Hello! This is a message!"
print(message)

#Simple Messages
msg : str = "Work Hard!"
print(msg)
msg = "Work Smarter not Harder!"          #reinitialization
print(msg)

#Personal Message
name : str = "Ameena Durrani"
print(f"Hello {name}, would you like to learn some Python today?")

#Name Cases
print(name.title())             #title
print(name.upper())             #uppercase
print(name.lower())             #lowercase

#Famous Quote
print('Maya Angelou once said, “You will face many defeats in life, but never let yourself be defeated.”')

#Famous Quote 2
famous_person : str = "Franklin D. Roosevelt"
quote :str = "The only limit to our realization of tomorrow is our doubts of today."
print(f'{famous_person} once said, “{quote}”')

#Stripping Names
person_name = "\t\n   AMEENA   \t\n"
print("Name with whitespaces:")
print(f"'{person_name}'")
print("After lstrip()")
print(f"'{person_name.lstrip()}'")
print("After rstrip()")
print(f"'{person_name.rstrip()}'")
print("After strip()")
print(f"'{person_name.strip()}'")

#Variable Sum
sum : int 
num1 : int = 5
num2 : int = 10
num3 : int = 15
sum = num1 + num2 + num3
print(f"The sum of {num1}, {num2} and {num3} is {sum}.")

#Variable Swap
a : int = 3
b : int = 5
print("Before Swapping: ")
print(f"a = {a}             b = {b}")
temp :int
temp = a
a = b
b = temp
print("After Swapping: ")
print(f"a = {a}             b = {b}")

#Favorite Color
fav_color : str = "Black"
print(f"My favourite color is: {fav_color}")
color : str = fav_color
print(color)

#Changing Pet Name
pet_name : str = "Buddy"
pet_name = "Max"
print(f"The pet's name is {pet_name}")

#Observing Name Error
#word : str = "Sunshine"
#print(word)
#print(Sunshine)

#Reassigning Score
score : int = 100
print(f"The score is {score}")
score = 89
print(f"The new score is {score}")

#City Name
city : str = "Lahore"
print(city)

#Title Case Text
text : str  = "python programming"
print(f'String "{text}" in title case: {text.title()}')

#Lowercase Conversion
string : str = "HeLLo WOrlD"
print(f'String "{string}" in lower case: {string.lower()}')

#Uppercase Conversion
string1 : str = "HeLLo WOrlD"
print(f'String "{string1}" in upper case: {string1.upper()}')

#Current Temperature
temperature : int = 25
print(f"The current temperature is {temperature} degrees.")

#Printing a Poem
poem = """
The sun sets in the west,
Painting the sky with hues of gold.
The stars appear, one by one,
As the night begins to unfold."""
print(poem)
