names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0:2])


#Write a program to find the largest number in a list
numbers = [23, 15, 36, 89]
max = numbers[0]
for item in numbers:
    if item > max:
        max = item
print(max)