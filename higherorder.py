# map()
# my_list=[1,2,3,4,5]
# def square(n):
#     return n**2
# new_list=list(map(square,[1,2,3,4,5]))
# print(new_list)

# add index number
# my_list1=[1,2,3,4,5]
# my_list2=[5,10,15,20,25]
# def add(x,y):
#     return x+y
# new_list=list(map(add,my_list1,my_list2))
# print(new_list)

# multiply index number
# my_list1=[1,2,3,4,5]
# my_list2=[5,10,15,20,25]
# def add(x,y):
#     return x*y
# new_list=list(map(add,my_list1,my_list2))
# print(new_list)

x=lambda a,b:a+b
print(list(map(x,[1,4,6,8,10],[3,5,7,9,11])))