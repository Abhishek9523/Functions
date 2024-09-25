#import functools
#    largest digit
# from functools import reduce
# my_list=[20,35,45,55,65,75]
# def largest_digit (x,y):
#     if x>y:
#         return x
#     else:
#         return y
    
# print(reduce(largest_digit,my_list))    
   
    # smallest digit 
# from functools import reduce
# my_list=[20,40,60,80,100,120]
# def smallest_digit (x,y):
#     if x < y :
#         return x
#     else:
#         return y
# print(reduce(smallest_digit,my_list))    

    # Add
    
# from functools import reduce
# my_list=[20,40,60,80,100,120]
# def sum_of_digit (x,y):
    
#         return x+y
# print(reduce(sum_of_digit,my_list))    

        # Multiply
        
from functools import reduce
my_list=[20,40,60,80,100,120]
def multiply_of_digit (x,y):
    
        return x*y
print(reduce(multiply_of_digit,my_list))    
        