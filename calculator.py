#author__thea_uy
#date__may_4_2024
#this program will ask the user for two inputs and an operation
#this program will also use different exceptions to capture errors during runtime

#create a loop for the whole program 
while True:

#create a list that will contain the numbers that the user will input
    content_integers = []

#create a function that will ask the user for numbers and determine if the the user input float and not string
    def evaluate():
        while True:
            try:
                number = float(input("Enter a number: "))
            except ValueError:
                continue
            return number

#create a for loop that will ask the user for two numbers
    for number in range(2):
        integers = evaluate()
        content_integers.append(integers)

#create an inner while loop and ask the user for their desire mathematical operations that is limited to addition, subtraction, division, and multiplication
    while True:
        try:
            operation = str(input("Enter the operation: +, -. x, /: "))

#this block of code will execute if the user chose addition
            if operation == "+":
                sum = content_integers[0] + content_integers[1]
                integers = round(sum, 2)
                statement  = (f"The sum of {content_integers[0]} and {content_integers[1]} is {integers} \n")
                print(statement)
                break

#this block of code will execute if the user chose subtraction
            elif operation == "-":
                difference = content_integers[0] - content_integers[1]
                integers = round(difference,2)
                statement = (f"The difference of {content_integers[0]} and {content_integers[1]} is {integers} \n")
                print(statement)
                break

#this block of code will execute if the user chose multiplication
            elif operation == "x":
                product = content_integers[0] * content_integers[1]
                integers = round(product,2)
                statement = (f"The product of {content_integers[0]} and {content_integers[1]} is {integers} \n")
                print(statement)
                break

#this block of code will execute if the user chose division
            elif operation == "/":
                quotient = content_integers[0] / content_integers[1]
                integers = round(quotient,2)
                statement = (f"The quotient of {content_integers[0]} and {content_integers[1]} is {integers} \n")
                break

#this block of code will execute if the user chose an operation that is not included in the choices
        except ValueError:
            print("Invalid operation")
            continue

#this block of code will execute if the program will detect a zero division error
        except ZeroDivisionError:
            print("Zero Division Error: Chose another operation")
            continue

#ask the user if they want to create a text file
    while True:
        try:
            answer = str(input("Do you want to create a text file? \n Append lets you add additional data \n Write lets you overwrite the existing data \n No means ou do not want to create a text file \n a/w/n: "))
            answer = answer[:1].lower()

#if the user wants to create a text file, they can choose if they want to append or write a text file
            if answer == "a":
                with open("statement.txt","a") as statement_file:
                    statement_file.write(str(statement))
                    break
            
            elif answer == "w":
                with open ("statement.txt","w") as statement_file:
                    statement_file.write(str(statement))
                    break
#exit the loop if the user do not want to create a text file
            elif answer == "n":
                break

            else:
                continue

        except ValueError:
            continue
#ask the user if they want to try again or exit the program
            

#end of the program 
