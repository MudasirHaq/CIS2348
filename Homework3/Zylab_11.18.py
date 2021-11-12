# Mudasir Haq
# 1834539

i = input()

elems_input = map(int, i.split())
# num_list = [element for element in elems_input if element >= 0]
num_list = []
for element in elems_input:
    if element >=0:
        num_list.append(element)
num_list.sort()

print(num_list)

