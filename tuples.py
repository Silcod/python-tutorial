numbers = (1, 2, 3) #Tuples are immutable, you cannot change them. We use brackets to define lists and parenthesis to define tuple
print(numbers[0])

#Unpacking: with unpacking we can achieve the same result with far less code
coordinates = (1, 2, 3 )
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates #What we have on line 10 is identical to what we have on line 6 to 7
print(x)