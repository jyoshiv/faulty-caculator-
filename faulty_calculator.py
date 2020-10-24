#design a calculator which gives all result except 45*3 =555, 56+9=77 , 56/6
# We have to fault these three calculations but other calculation will not be affected
# 45 * 3 = 44 , 56 + 9 = 45, 56/6 = 100

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
x = input("Enter your operator {+ , - , * , / , %, ** }: ")

if x == "+":
    if n1 == 56 and n2 == 9:
        print("Your answer is 45.")
    else:
        print("Your answer is ", n1 + n2)
elif x == "-":
    print("Your answer is ", n1 - n2)
elif x == "*":
    if n1 == 45 and n2 == 3:
        print("Your answer is 44.")
    else:
        print("Your answer is ", n1 * n2)
elif x == "/":
    if n1 == 56 and n2 == 6:
        print("Your answer is 100")
    else:
        print("Your answer is ", n1 / n2)
elif x=="%":
    print("your answer is ", n1%n2)


elif x=="**":
    print("your answer is ", n1**n2)

