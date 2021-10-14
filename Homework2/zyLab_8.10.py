#Mudasir Haq
#1834539

line = input()
edited_line = ""
reversed_line = ""

for i in range(len(line)):
    if not line[i].isspace():
        edited_line += line[i].lower()
        reversed_line = line[i].lower() + reversed_line
if edited_line == reversed_line:
    print(line + " is a palindrome")
else:
    print(line + " is not a palindrome")