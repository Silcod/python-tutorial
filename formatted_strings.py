first = 'Ibrahim'
last = 'Sanusi'
message = first + ' [' + last + '] is a coder' # It's not easy for us to visualize the output that's why we use formatted strings
msg = f'{first} [{last}] is a coder' #Formatted strings makes it easier to visualize our output
print(message)
print(msg)

# =========================Python String Methods==================//
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.find('P'))
print(course.find('o'))
print(course.find('Beginners')) #You get 11 because the Beginners starts at sequence 11
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print('python' in course) #Note that the function is case sensitive