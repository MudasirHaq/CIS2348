#Mudasir Haq
#1834539

xFirst = int(input())
yFirst = int(input())
zFirst = int(input())
xSecond = int(input())
ySecond = int(input())
zSecond = int(input())

solution_valid = False
resX = 0
resY = 0
for x in range(-10,11):
    for y in range(-10, 11):
        if ((xFirst * x+yFirst * y == zFirst) and (xSecond * x+ySecond * y == zSecond)):
            resX = x
            resY = y
            solution_valid = True
            break
    if (solution_valid):
        break
if(solution_valid):
    print(resX, resY)
else:
    print("No solution")