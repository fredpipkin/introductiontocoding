import random

class Dice:
    def __init__(self, sides):
        self.number_of_sides = sides 
    
    def roll(self):
        return random.randint (1, self.number_of_sides)
    
my_d6 = Dice(6)

for _ in range(10):    
    roll_result = my_d6.roll()
    print(roll_result)

d6 = Dice(6)
d20 = Dice(20)

result = d6.roll() + d20.roll()

print(result)

