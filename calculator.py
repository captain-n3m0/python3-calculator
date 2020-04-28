command = ""
while True:
    command = input("> ")
    
    if command == "Addition":
        print("ADDITION")
        first_number =                         int(input("ENTER FIRST NUMBER > "))
        second_number = int(input("ENTER SECOND NUMBER > "))
        result = first_number + second_number
        print(result)
    
    
    elif command == "Subtraction":
        print("SUBTRACTION")
        first_number = int(input("Enter first number "))
        second_number = int(input("Enter the second number "))
        result = first_number - second_number
        print(result)
    
    
    elif command == "Multiplication":
        first_number = int(input("Enter the first number"))
        second_number = int(input("Enter the second number "))
        result = first_number * second_number
        print(result)
    
    elif command == "Division":
        print("DIVISION")
        first_number = int(input("Enter first number "))
        second_number = int(input("Enter the second number "))
        result = first_number/second_number
        print(result)
    elif command == "quit":
        break
        
    else:
        print("""CALCULATOR BY DEBJIT NASKAR
type Addition , Subtraction , Multiplication , Division , type quit to quit""")
    
 
    
    
    

    
    
   
    
    
