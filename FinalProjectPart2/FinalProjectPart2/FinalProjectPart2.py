# Mudasir Haq
# 1834539

import csv  # loads module to work with CSV files
from datetime import datetime  # loads module to import current date

## NOTE: LOAD DATA
def load_data():
    # list that will hold specific CSV file's lines
    manuf = []
    serve = []
    price = []
    # csv files to read
    all_csv = ['ManufacturerList.csv', 'ServiceDatesList.csv', 'PriceList.csv']
    # accesses one csv file element at a time in all_csv list
    for csvdoc in all_csv:
        # opens CSV file
        f = open(csvdoc)
        # reader function within CSV module interprets file as CSV
        reader = csv.reader(f)
        # accesses single row in reader function
        for row in reader:
            # conditional statement to select a specific CSV file
            if csvdoc == 'ManufacturerList.csv':
                # (appends) a new row to end of specific list NOTE(append only works with lists)
                manuf.append(row)
            if csvdoc == 'ServiceDatesList.csv':
                serve.append(row)
            if csvdoc == 'PriceList.csv':
                price.append(row)
        f.close()

    # variable holds one line in CSV file
    # for loop reads one element at a time
    allInv = []  # NOTE: will hold list of all item info dicts
    # add item ID, manufacturer, type and condition info
    for line in manuf:
        firstd = {}
        firstd['itemid'] = line[0].strip() # strip() removes extra spaces
        firstd['manufname'] = line[1].strip()
        firstd['type'] = line[2].strip()
        firstd['condition'] = line[3].strip()
        allInv.append(firstd)
    # add matching price and service date info to each item
    for item in allInv:
        for elem_s in serve:
            if elem_s[0] == item['itemid']:
                # new item added to dictionary
                item['servicedate'] = elem_s[1]
        for elem_s in price:
            if elem_s[0] == item['itemid']:
                item['price'] = float(elem_s[1])

    # list storing all item-info dicts is called in the sort function to
    # sort the inventory items by descending price (high to low)
    allInv = sorted(allInv, key=lambda d: d['price'], reverse=True)

    ## NOTE: return list of inventory item info dicts, sorted high to low price
    return allInv

# NOTE: make a list of all damaged inventory item IDs
def damaged_check(allInv):
    # define list of damaged inventory to include possibility of future appending
    damaged = []
    # iteration to find the condition of all items and verify whether those items in main CSV file are damaged
    for entry in allInv:
        condition = entry['condition']
        # checks if the item is damaged
        if condition == 'damaged':
            # NOTE: add damaged item ID to list "damaged"
            damaged.append(entry['itemid'])

    # NOTE: damaged list now holds ALL damaged item IDs
    return damaged

# NOTE: make a list of all out-of-service inventory item IDs
def service_check(allInv):
    # get current date
    datetime_obj = datetime.now()
    # get current time from previous defined datetime object
    curr_date = datetime_obj.date()

    # define list that will get appended out-of-service item IDs
    serv_needed = []
    # iterates through each product to output date of service
    for entry in allInv:
        # get service date
        serv_date = entry['servicedate']
        # convert date to datetime object in order to manipulate time and dates simultaneously for later sorting by most recent date
        serv_date = datetime.strptime(serv_date, '%m/%d/%Y')
        # convert datetime type to date type to keep date without hour, minute, second manipulation
        serv_date = datetime.date(serv_date)
        # iterates whether item has surpassed service date to confirm that item is in need of service
        if serv_date < curr_date:
            # NOTE: add out of service item ID to list "serv_needed"
            serv_needed.append(entry['itemid'])

    # NOTE: serv_needed list now holds ALL out of service item IDs
    return serv_needed

## NOTE: make lists of all manufacturers + item-types in inventory
def inventory_item_manuf():
    allInv = load_data()  # get list of all inventory info dicts

    test_manuf = []  # list that will hold all manufacturers in inventory
    test_type = []  # list that will hold all item-types in inventory
    # itterate inventory dicts and add type/manufacturer to each's list
    for item in allInv:
        # list of all manufacturers
        test_manuf.append(item['manufname'])
        # list of all item types
        test_type.append(item['type'])

    ## NOTE: return lists of all manufacturers + item-types in inventory
    return test_manuf, test_type

# NOTE: check if user inputted only one valid item and manufacturer, each
def check_item_manuf(users_input):

    ## NOTE: 1) return lists of all manufacturers + item-types in inventory
    test_manuf, test_type = inventory_item_manuf()

    ## NOTE: 2) check if user inputted ONE valid manufacturer and item-type
    # counts number of valid manufacturers the user inputted; initially zero
    manuf_count = 0
    # counts number of valid item-types the user inputted; initially zero
    type_count = 0

    ## itterate through all inputted words and check if valid
    for word in users_input:
        ## NOTE: manufacturer check section
        # checks if query manufacturer is in list of all inventory manufacturers
        if word in test_manuf:
            # if passes check, stores the query manufacturer
            user_manuf = word
            # if passes check, add 1 to the manufacturer counter
            manuf_count += 1

        ## NOTE: item-type check section
        # checks if query item-type is in list of all inventory item-types
        if word in test_type:
            # if passes check, stores the query item-type
            user_type = word
            # if passes check, add 1 to the item-types counter
            type_count += 1

    # if input exactly one valid type and manufacturer -> return valid inputs
    if manuf_count == 1 and type_count == 1:
        return user_manuf, user_type

    # if input no valid type/manufacturer or too many -> return two None's
    else:
        return None, None

# NOTE: get item info if not out-of-service or damaged
def get_match_item_info(user_manuf, user_type):

    ## NOTE: 1) make list of all items that match user input
    ## get list of all inventory info dicts, sorted high to low price
    allInv = load_data()
    matching_items = [] # list of all items info dicts matching user input
    # itterate through all items in inventory
    for item in allInv:
        inventory_manuf = item['manufname']
        inventory_type = item['type']
        # check if user input matches itterating item's manufacturer and type
        if user_manuf==inventory_manuf and user_type==inventory_type:
            # if matches, add item info to list of all matches
            matching_items.append(item)

    ## NOTE: 2) check if matching items are damaged/out-of-service
    valid_matches = [] # list of undamaged + in-service matching item info dicts
    damaged = damaged_check(allInv)  # list of all damaged item IDs
    expired = service_check(allInv)  # list of all out-of-service item IDs
    # itterate through all matching items
    for match in matching_items:
        match_ID = match['itemid']  # ID of match
        ## check if match is not damaged AND not out-of-service
        if match_ID not in damaged and match_ID not in expired:
            # if passes check, add to list of undamaged + in-service matches
            valid_matches.append(match)

    expensive_match = valid_matches[0]  # most expensive matched + valid item
    # NOTE: return item info dict of most expensive valid match
    return expensive_match

# NOTE: get recommended item info if not out-of-service or damaged
def recommended(user_item_info):

    ## NOTE: 1) make list of all items that match user input
    ## get list of all inventory info dicts, sorted high to low price
    allInv = load_data()

    user_type = user_item_info['type']  # get types of items to recommend
    user_manuf = user_item_info['manufname']  # manufacturers to NOT recommend

    ## list of all items with same item-type as user + from other manufacturers
    matching_items = []
    # itterate through all items in inventory
    for item in allInv:
        inventory_type = item['type']
        inventory_manuf = item['manufname']
        # check if itterating item matches user's item-type and NOT user's manuf
        if inventory_type == user_type and inventory_manuf != user_manuf:
            # if matches, add item info to list of all matches
            matching_items.append(item)

    ## NOTE: 2) check if matching items are damaged/out-of-service
    valid_matches = [] # list of undamaged + in-service matching item info dicts
    damaged = damaged_check(allInv)  # list of all damaged item IDs
    expired = service_check(allInv)  # list of all out-of-service item IDs
    # itterate through all matching items
    for match in matching_items:
        match_ID = match['itemid']  # ID of match
        ## check if match is not damaged AND not out-of-service
        if match_ID not in damaged and match_ID not in expired:
            # if passes check, add to list of undamaged + in-service matches
            valid_matches.append(match)

    expensive_recommended = valid_matches[0]  # most expensive + valid match
    # NOTE: return item info dict of most expensive valid match
    return expensive_recommended


## NOTE: query user and tie together other functions
def query_user():
    users_input = []
    # while loop queries the user whenever anything but q is inputted, and quits the loop when q is inputted
    while users_input != 'q':
        ## NOTE: 1) get user input
        users_input = input(
            "Please enter an item type and item manufacturer, or enter 'q' to quit:\n")
        ## NOTE: 2) quit statement
        if users_input == 'q' or users_input == 'Q':
            # loop will query the user again
            break
        # splits user input line into strings
        users_input = users_input.split()

        ## NOTE: 3) process user input into manufacturer + item-type
        user_manuf, user_type = check_item_manuf(users_input)

        ## NOTE: 4) check if invalid input manufacturer + item-type
        if user_manuf == None and user_type == None:
            print('No such item in inventory')

        ## NOTE: 5) print inputted item info, or most expensive if multiple
        else:
            user_item_info = get_match_item_info(user_manuf, user_type)
            id = str(user_item_info['itemid']) + ','
            mn = str(user_item_info['manufname']) + ','
            it = str(user_item_info['type']) + ','
            ip = str(user_item_info['price'])
            print('Your item is: ' 'Item ID:', id, 'Manufacturer name:', mn, 'Item type:', it, 'Item price:', ip)

        ## NOTE: 6) print item info of recommended other manuf valid item
            reccommend_info = recommended(user_item_info)
            id = str(reccommend_info['itemid']) + ','
            mn = str(reccommend_info['manufname']) + ','
            it = str(reccommend_info['type']) + ','
            ip = str(reccommend_info['price'])
            print('You may also consider: ' 'Item ID:', id, 'Manufacturer name:', mn, 'Item type:', it, 'Item price:', ip)
    return

## execute script by calling main function
query_user()



######################################

