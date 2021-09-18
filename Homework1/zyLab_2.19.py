#Mudasir Haq
#1834539
cups_lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
cups_water = float(input('Enter amount of water (in cups):\n'))
cups_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
print('Lemonade ingredients - yields {:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(cups_lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(cups_water), 'cup(s) water')
print('{:.2f}'.format(cups_agave_nectar), 'cup(s) agave nectar\n')

your_servings = float(input('How many servings would you like to make?\n'))
print()
cups_lemon_juice = cups_lemon_juice/servings * your_servings
cups_water = cups_water/servings * your_servings
cups_agave_nectar = cups_agave_nectar/servings * your_servings
servings = your_servings


print('Lemonade ingredients - yields {:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(cups_lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(cups_water), 'cup(s) water')
print('{:.2f}'.format(cups_agave_nectar), 'cup(s) agave nectar')
print()
gallons  = 16
cups_lemon_juice = cups_lemon_juice/gallons
cups_water = cups_water/gallons
cups_agave_nectar = cups_agave_nectar/gallons

print('Lemonade ingredients - yields {:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(cups_lemon_juice), 'gallon(s) lemon juice')
print('{:.2f}'.format(cups_water), 'gallon(s) water')
print('{:.2f}'.format(cups_agave_nectar), 'gallon(s) agave nectar')