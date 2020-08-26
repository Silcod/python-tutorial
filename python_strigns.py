course1 = "Python's Course for Beginners"
another = course1[:]
course2 = 'Python for "Beginners"'
course3 = '''
Hi Ibrahim,

Here is our first email to you. 

Thank you,
The support team
'''
name = 'Jennifer'

print(course1)
print(course2)
print(course3)
print(course1[0]) #Index: start from the beginning of the sentence
print(course1[-1]) #Negative Index: starts from the end of the sentence
print(course1[0:3]) #Python will return the characters starting from index 0 all the way to index 2 but excludes index 3
print(course1[0:]) #Python returns all the characters to the end of the string
print(course1[2:]) #P and Y are removed
print(course1[:5]) #Python interpreter will assume 0 as the first index
print(another) # 0 will be assumed as the Start index and the length of the string will be assumed as the End index
print(name[1:-1])