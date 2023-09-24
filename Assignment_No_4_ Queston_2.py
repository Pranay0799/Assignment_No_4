##Write a Python program to triple all numbers of a given list of integers. Use Python map.
'''
sample list: [1, 2, 3, 4, 5, 6, 7]

Triple of list numbers:
[3, 6, 9, 12, 15, 18, 21]
'''

# sample_list = [1,2,3,4,5,6,7]
# result = list(map(lambda a: a*3, sample_list))
# print("Triple all the numbers : ", result)



## Taking input from user

size = int(input("Enter number of elements in the list : "))
sample_list = []
for i in range(size):
    a = int(input(f"Enter the {i +1} element : "))
    sample_list.append(a)
print("Sample list : ", sample_list)

result = list(map(lambda a: a*3, sample_list))
print("Triple all the numbers in list : ", result)


