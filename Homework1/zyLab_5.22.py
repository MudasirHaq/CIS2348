#Mudasir Haq
#1834539
costDict = {'-': 'No service', 'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print('')
print('Select first service:')
first_service = input()
print('Select second service:')
second_service = input()

print('')
print("Davy's auto shop invoice")
print('')

if first_service!='-' and second_service!='-':
    print('Service 1: '+first_service+', $'+ str(costDict[first_service]))
    print('Service 2: '+second_service+', $'+ str(costDict[second_service]))
    Total=costDict[first_service]+costDict[second_service]
elif first_service=='-':
    print('Service 1: '+'No service')
    print('Service 2: '+second_service+', $'+ str(costDict[second_service]))
    Total=costDict[second_service]
else:
    print('Service 1: '+first_service+', $'+ str(costDict[first_service]))
    print('Service 2: '+'No service')
    Total=costDict[first_service]

print('\nTotal: $'+str(Total))
