numbers = [5, 2, 1, 7, 4]
numbers2 = [2, 6, 4, 3, 9]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(7)
#numbers.clear(): to remove all items in the list
numbers.pop() #To remove the last item in a list
print(numbers)
print(numbers.index(5))
print (5 in numbers)
numbers2.sort() #To sort items of a list in ascending order
numbers2.reverse() #To sort items of a list in descending order
print(numbers2)

#Copy : numbers2 and numbers3 are two independent lists
numbers3 = numbers2.copy()
numbers2.append(10)
print(numbers2)
print(numbers3)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)