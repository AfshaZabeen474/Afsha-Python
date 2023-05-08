#Write a Python program to find the sum of all the numbers in a given list.
lis_str = input('Enter the list as a string separated by commas:')
lis_1 = [int(num) for num in lis_str.split(",")]
print('The sum of the numbers in the list is:')
print(sum(lis_1))

#now let us do it by using functions
print('Output based on using functon....')
def addition(lis_1):
    print(sum(lis_1))
print('The sum is:')
addition(lis_1)

#otherwise, we can also write like this
print('The sum of the numbers is:')
add = sum(lis_1)
print(add)
'''Output:
Enter the list as a string separated by commas:1,2,3,4,5
The sum of the numbers in the list is:
15
Output based on using functon....     
The sum is:
15
The sum of the numbers is:
15
'''

#THIS CODE IS WRITTEN BY AFSHA ZABEEN