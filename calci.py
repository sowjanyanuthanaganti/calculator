'''import random
import array
max_len=12
digits=['0','1','2','3','4','5','6','7','8','9']
lowercase_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['@','#','$','&','%','=','*','/','+','-','.',':','?','|','~','<','.','(',')']
combined_list=digits+lowercase_characters+uppercase_characters+symbols
rand_digit=random.choice(digits)
rand_lower=random.choice(lowercase_characters)
rand_upper=random.choice(uppercase_characters)
rand_symbol=random.choice(symbols)
temp_pass=rand_digit+rand_lower+rand_upper+rand_symbol
for x in range(max_len-4):
    temp_pass=temp_pass+random.choice(combined_list)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
password=""
for x in temp_pass_list:
    password=password+x'''

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
