# Mudasir Haq
# 1834539

# names_list = ('hey', 'hi', 'Mark', 'mark')
# names = names_list

n = input()
names = n.split()

for value in names:
    frequency = names.count(value)
    print(value, frequency)