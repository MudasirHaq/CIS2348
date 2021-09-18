#Mudasir Haq
#1834539

import math

paintColorsDict = {'red':35, 'blue':25, 'green':23}

wall_height = int(input('Enter wall height (feet):\n'))
wall_width=int(input('Enter wall width (feet):\n'))
wall_area=wall_height*wall_width
print('Wall area:',wall_area,'square feet')

areaGallon=350
paintNeeded=wall_area/areaGallon
print('Paint needed: {:.2f}'.format(paintNeeded),'gallons')

cans = math.ceil(paintNeeded)
print('Cans needed:',cans,'can(s)\n')

color=input('Choose a color to paint the wall:\n')
print('Cost of purchasing ',color,' paint: $',paintColorsDict[color]*cans,sep='')