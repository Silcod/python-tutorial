is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water") #if this statement is also indented it will execute if the condition is true
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#=====Down Payment of a House========
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 *price
else:
    down_payment = 0.2 *price
print(f"Down payment: ${down_payment}")
print("Pleasure doing business with you")