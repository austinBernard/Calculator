import math

class Calculator:
    def input_nums(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
        
    def addition(self):
        total_add = int(num1) + int(num2)
        print(f"{num1} + {num2} = {total_add}")
        
    
    def subtract(self):
        total_sub = int(num1) - int(num2)
        print(f"{num1} - {num2} = {total_sub}")
        
        
    def option(self):
        option_choice = print("\n1. Addition\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")
        option = input("Choose an option: ")
        
        while(option != "5"):
            if option == "1":
                return self.addition()
                break
            elif option == "2":
                return self.subtract()
            print(option_choice) #stopping point!!!!!!_______________________ (Get options to loop after choosing an option.)
        if option == "5":
            print("Thank you!")
            
        
        
# Main

calc = Calculator() # Calling Calculator class



num1 = input("Enter a number: ") # Storing value into num1
num2 = input("Enter a second number: ") # Storing value into num2

calc.input_nums(num1, num2)
calc.option()


