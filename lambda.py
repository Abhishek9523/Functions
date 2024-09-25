# Aisa function jiska koi naam naa hoo use lamda function kehte hai.
# syntex:--
    # x=lamda arguments:expressions
    # lamda=keyword
    # arguments=n no. of argument
    # expression= single line pf expression
    # argument:statement of if if condition else statement

n=int(input("enter any number"))
x=lambda n:True  if n%2==0 else False
print(x(n))     