#Taking user inputs
message=input("What's your name?")
print(f"Hello, {message}\n")

#When there's a prompt that goes more than one line:
prompt="If you tell us who you are, we can personalize the messages you see"
prompt+= "\nWhats your name? "
name=input(prompt)
print(f"Here's what you wanted, {name}")

#Using int() to accept numerical input
"""when we use input() function, pyhton interprets everything that the user has entered as a string..
So when an user enters a number , python will return a string quoted with apostrophes when used with a 
print() statement, thus and therby treating the numerical figure as a string, which produces a TypeError when 
comparison operators are used, as python cannot interpret comparison operators with string..
"""
age = input("\nHow old are you")
age = int(age)
if age>=18:
	print("You are an adult\n")
else:
    print("You are a minor\n")	

#Using a modulo operator along with int() and input() functions to determine if the number is odd or even
number = input('Enter the number :') 
number = int(number)
if number % 2 ==0:
	print(f"{number} is an even number\n")
else : 
    print(f"{number} is an odd number\n")
print(f"Arigato Gojaimasu")  

#excersice: If the number entered is a multiple of ten
number = input("Enter the number : ")
number = int(number)  	
if number % 10 == 0:
	print("It's a multiple of ten\n")
else : 
    print("It's not a multiple of ten\n")	
