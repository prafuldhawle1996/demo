# num_1 = 10
# num_2 = 40

# sum = num_1 + num_2
# print(sum)

num_1 = float(input("Enter first number:"))
num_2 = float(input("Enter second number:"))
choice = input("Enter the operations + - * /")

if choice == "+":
    sum = num_1 + num_2
    print("The sum is",sum)
elif choice == "-":
    diff = num_1 - num_2
    print("The difference is",diff)
elif choice == "*":
    multiplication = num_1 * num_2
    print("The multiplication is", multiplication)
elif choice == "/":
    division = num_1/num_2
    print("The div is", division)
else:
    print("Invalid choice")