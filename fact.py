def fact(num : int) -> int :
    return num if (num == 1) else num * fact(num - 1)

user_input = int(input("Enter : "))
print(f"The factorial of {user_input} is {fact(user_input)}")