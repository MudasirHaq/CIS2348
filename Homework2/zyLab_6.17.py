#Mudasir Haq
#1834539

inputPassword = input()

final_password = ''

for x in inputPassword:

    if(x=='i'):
        final_password+= "!"

    elif(x=='a'):
        final_password += "@"

    elif (x == 'm'):
        final_password += "M"

    elif (x == 'B'):
        final_password += "8"

    elif (x == 'o'):
        final_password += "."

    else:
        final_password += x

final_password += "q*s"

print(final_password)