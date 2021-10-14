#Mudasir Haq
#1834539

def extract_date(date):
    
    correct_date = 0

    
    final_date = ""

    
    if date.find(",") != -1:
        
        month_day, year = date.split(',')

        
        if month_day.find(" ") != -1:
            
            month, day = month_day.split(" ")

            
            correct_date = 1

            
            day = day.strip()
            month = month.strip()
            year = year.strip()

            
            
            if month == "January":
                final_date = "1" + "/"
            elif month == "February":
                final_date = "2" + "/"
            elif month == "March":
                final_date = "3" + "/"
            elif month == "April":
                final_date = "4" + "/"
            elif month == "May":
                final_date = "5" + "/"
            elif month == "June":
                final_date = "6" + "/"
            elif month == "July":
                final_date = "7" + "/"
            elif month == "August":
                final_date = "8" + "/"
            elif month == "September":
                final_date = "9" + "/"
            elif month == "October":
                final_date = "10" + "/"
            elif month == "November":
                final_date = "11" + "/"
            elif month == "December":
                final_date = "12" + "/"
            else:
                correct_date = 0

            
            final_date += day + "/"

            
            final_date += year

    if correct_date == 1:
        return final_date
    else:
        return ""

file = open('inputDates.txt','r')
file_dates = []

file_dates = file.readlines()

file.close()

for i in range(len(file_dates)-1):
    file_dates[i] = file_dates[i][:-1]

file = open('parsedDates.txt', 'w')

for i in file_dates:
    if i == "-1":
        break
    else:
        final_date = extract_date(i)
        if final_date != "":
            file.write(final_date + "\n")

file.close()

file = open('parsedDates.txt', 'r')
file_parsed_dates = []

file_parsed_dates = file.readlines()

file.close()

print("Input file inputDates.txt content:\n")
for i in file_dates:
    print(i)

print("\nOutput file parsedDates.txt content:\n")
for i in file_parsed_dates:
    print(i)