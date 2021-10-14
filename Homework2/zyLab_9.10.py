#Mudasir Haq
#1834539
import csv

file_name = input()

frequency = {}
with open('input1.csv', newline='') as csvfile:
  data = csv.reader(csvfile)
  for words in data:
    for word in words:
      if word in frequency.keys():
        frequency[word] += 1
      else:
        frequency[word] = 1

for word in frequency.keys():
  print(f"{word} {frequency[word]}")