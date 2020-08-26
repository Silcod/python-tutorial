# Just go to your browser and search for python 3 module index, you'll see a lot. As you build more applications yoou will get more familiar with the modules
# Nobody knows all the modules in python standard library. Everybody knows some modules based on the applications they have built
import random             #random is a built in modules

for i in range(5):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
print(dice.roll())

#Another Method which gives same result
for i in range(1):
    first_dice = random.randint(1,6)
    second_dice = random.randint(1, 6)
    print ((first_dice, second_dice))