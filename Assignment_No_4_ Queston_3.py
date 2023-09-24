## Write a Python program to square the elements of a list using map() function.

'''
Sample List: [4, 5, 2, 9]

Square the elements of the list:

[16, 25, 4, 81]

'''


# sample_list = [4, 5, 2, 9]
# result = list(map(lambda a: a**2, sample_list))
# print("Square of  all the numbers : ", result)



## Taking input from user

size = int(input("Enter number of elements in the list : "))
sample_list = []
for i in range(size):
    a = int(input(f"Enter the {i +1} element : "))
    sample_list.append(a)
print("Sample list : ", sample_list)

result = list(map(lambda a: a**2, sample_list))
print("Square of  all the numbers : ", result)
