# Mudasir Haq
# 1834539

import csv
from datetime import datetime

## LOAD DATA

# list that will hold specific CSV file's lines
manuf = []
serve = []
price = []

all_csv = ['ManufacturerList.csv', 'ServiceDatesList.csv', 'PriceList.csv']
# accesses one element at a time in all_csv list
for csvdoc in all_csv:
    # opens CSV file
    f = open(csvdoc)
    # reader function within CSV module interprets file as CSV
    reader = csv.reader(f)
    # accesses single row in reader function
    for row in reader:
        # conditional statement to select a specific CSV file
        if csvdoc == 'ManufacturerList.csv':
            # adds (appends) a new row to the end of the specific list NOTE(append only works with lists)
            manuf.append(row)
        if csvdoc == 'ServiceDatesList.csv':
            serve.append(row)
        if csvdoc == 'PriceList.csv':
            price.append(row)

## a.) Inventory report -> FullInventory

# variable holds one line in CSV file
# for loop reads one element at a time
allInv = []
for line in manuf:
    firstd = {}
    firstd['itemid'] = line[0]
    firstd['manufname'] = line[1]
    firstd['type'] = line[2]
    firstd['condition'] = line[3]
    allInv.append(firstd)
# allInv
for item in allInv:
    for elem_s in serve:
        if elem_s[0] == item['itemid']:
            # new item added to dictionary
            item['servicedate'] = elem_s[1]
    for elem_s in price:
        if elem_s[0] == item['itemid']:
            item['price'] = elem_s[1]

# sort by manufacturer alphabetically
allInv = sorted(allInv, key=lambda d: d['manufname'])

# opening the csv file in 'w' mode
file = open('FullInventory.csv', 'w', newline='')

with file:
    # identifying header
    header = ['itemid', 'manufname', 'type',
              'price', 'servicedate', 'condition']
    writer = csv.DictWriter(file, fieldnames=header)

    # writing data row-wise into the csv file
    for item_d in allInv:
        writer.writerow(item_d)

## b.) Inventory report -> Item type inventory list

type_dict = {}
for entry in allInv:
    entry_c = entry.copy()
    item_type = entry_c['type']
    ## remove type data from entry
    del entry_c['type']
    if item_type in type_dict:
        type_dict[item_type].append(entry_c)
    elif item_type not in type_dict:
        type_dict[item_type] = [entry_c]
    # sort by itemid
    type_dict[item_type] = sorted(
        type_dict[item_type], key=lambda d: d['itemid'])

for k, v in type_dict.items():
    csvname = k + 'Inventory.csv'
    # opening the csv file in 'w' mode
    file = open(csvname, 'w', newline='')

    with file:
        # identifying header
        header = ['itemid', 'manufname',
                  'price', 'servicedate', 'condition']
        writer = csv.DictWriter(file, fieldnames=header)

        # writing data row-wise into the csv file
        for item_t in v:
            writer.writerow(item_t)

## c.) Inventory report -> PastServiceDateInventory

# get current date
datetime_obj = datetime.now()
# extract the time from datetime_obj
curr_date = datetime_obj.date()

serv_needed = []
for entry in allInv:
    # get service date
    serv_date = entry['servicedate']
    # convert date to datetime object
    serv_date = datetime.strptime(serv_date, '%m/%d/%Y')
    # convert datetime type to date type
    serv_date = datetime.date(serv_date)

    # compare dates
    if serv_date < curr_date:
        serv_needed.append(entry)

# sort by service dates, oldest to most recent ## NOTE unclear if works
serv_needed = sorted(serv_needed, key=lambda d: d['servicedate'])

# opening the csv file in 'w' mode
file = open('PastServiceDateInventory.csv', 'w', newline='')

with file:
    # identifying header
    header = ['itemid', 'manufname', 'type',
              'price', 'servicedate', 'condition']
    writer = csv.DictWriter(file, fieldnames=header)

    # writing data row-wise into the csv file
    for item_s in serv_needed:
        writer.writerow(item_s)

## d.) Inventory report -> DamagedInventory

damaged = []
for entry in allInv:
    entry_c = entry.copy()
    condition = entry_c['condition']
    del entry_c['condition']
    if condition == 'damaged':
        damaged.append(entry_c)

# sort by price, descending
damaged = sorted(damaged, key=lambda d: d['price'], reverse=True)

# opening the csv file in 'w' mode
file = open('DamagedInventory.csv', 'w', newline='')

with file:
    # identifying header
    header = ['itemid', 'manufname', 'type',
              'price', 'servicedate']
    writer = csv.DictWriter(file, fieldnames=header)

    # writing data row-wise into the csv file
    for item_d in damaged:
        writer.writerow(item_d)