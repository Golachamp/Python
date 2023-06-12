num_1 = float(input("Please enter the first number:"))
num_2 = float(input("Enter another number:"))
choice = input("Enter the operator (+, -, *, /) :")
if choice == "+":
    sum = num_1 + num_2
    print("The sum is:", sum)
elif choice == "-":
    diff = num_1 - num_2
    print("The difference is :", diff)
elif choice ==  "*":
    mult = num_1 * num_2
    print("The Product is:",mult)
elif choice ==  "/":
    div = num_1 / num_2 
    print("The quotient is",div)  
else:
    print("Invalid choice")