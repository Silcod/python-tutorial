for every in ['Ibrahim', 'Mubarak', 'Halima', 'Wahab']:
    print(every)
for item in [1, 2, 3, 4]:
    print(item)
# If you want to 'Iterate' over a large list of number, you use the range function
for item in range(10):
    print(item)
for item in range(5, 10, 2):
    print(item)

#Write a program to calculate all the items in a shopping cart. For ==condition== execute this
prices = [50, 95, 36]

total = 0
for price in prices:
    total += price
print (f"Total: {total}")