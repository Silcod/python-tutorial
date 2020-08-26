for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
#Explanation: In the first iteration of the outer loop x is 0, in the first iteration of the outer x is still 0 but y is
#incremented to 1, so this will continue untill the inner loop(y) completes. After the inner loop completes then the control
#will move to line 2 or the inner loop and the range function is going to generate the numbers 0 to 3 one more time

#Exercise
numbers = [1, 1, 1, 1, 5]
for item in numbers:
    output = ''
    for count in range(item):
        output += 'x'
    print(output)