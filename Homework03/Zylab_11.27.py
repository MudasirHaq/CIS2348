# Mudasir Haq
# 1834539

jersey_dict = {}
for i in range(1,6):
    while True:
        try:    
            jersey_num = int(input("Enter player {}'s jersey number:\n".format(i)))
            if jersey_num < 0 or jersey_num > 99:
                raise ValueError
            break
        except ValueError:
            continue

    while True:
        try:    
            player_rating = int(input("Enter player {}'s rating:\n".format(i)))
            print()
            if player_rating < 1 or player_rating > 9:
                raise ValueError
            break
        except ValueError:
        	continue
        
    jersey_dict[i] = [jersey_num, player_rating]
	

print('ROSTER')

for k, v in sorted(jersey_dict.items(), key=lambda x: x[1][0]):
	jn = str(v[0]) + ','
	rt = str(v[1])
	print('Jersey number:', jn, 'Rating:', rt)
print()
#print('\n')
def menu():
    # print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
menu()
opt = input('Choose an option:\n')
while opt != 'q':
    if opt == 'o':
        print()
        print('ROSTER')
        for k, v in sorted(jersey_dict.items(), key=lambda x: x[1][0]):
            jn = str(v[0]) + ','
            rt = str(v[1])
            print('Jersey number:', jn, 'Rating:', rt)
        pass

    elif opt == 'a':
        addlist = []
        optaddjersey = int(input("Enter a new player's jersey number:"))
        optaddrating = int(input("Enter the player's rating:"))
        addlist.append(optaddjersey)
        addlist.append(optaddrating)
        addkey = len(jersey_dict) + 1
        jersey_dict[addkey] = addlist
        pass

    elif opt == 'd':
        # get jersey number of player to be deleted
        deletejersey = int(input("Enter a jersey number:"))
        # iterate through players in roster dictionary
        for k, v in jersey_dict.items():
            # match player to be deleted by jersey number
            if v[0] == deletejersey:
                # get matched player
                deletedplayer = k
        # delete matched player
        del jersey_dict[deletedplayer]
        pass

    elif opt == 'u':
        updatejersey = int(input("Enter a jersey number:"))
        updateRating = int(input("Enter a new rating for player:"))
        for k, v in jersey_dict.items():
            if v[0] == updatejersey:
                updatedplayer = k
        # dictionary key is accessed to update with new value
        jersey_dict[updatedplayer] = [updatejersey, updateRating]
        pass

    elif opt == 'r':
        ratingaboveList = []
        enterRating = int(input('Enter a rating:'))
        for k, v in jersey_dict.items():
            if v[1] > enterRating:
                ratingaboveList.append(k)
        print('ABOVE', enterRating)
        for player in ratingaboveList:
            jnabove = jersey_dict[player][0]
            rtabove = jersey_dict[player][1]
            print('Jersey number:', jnabove, 'Rating:', rtabove)
        pass

    menu()
    opt = input('Choose an option:\n')
#print('Quit')








#while(1):
    #menu = input('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')
    #opt = input('Choose an option:\n')
    #if opt == 'o':
        #print('ROSTER')
        #for jersey_num, player_rating in sorted(jersey_dict.items()):
            #print('Jersey number:', jn, 'Rating:', rt)
    #if opt == 'a':
        #opt = input('')
# input1 = '99'
# input2 = '5'
# jersey_dict(player_num)
# jersey_dict = {'jersey_number:': []}
#jersey_dict = {'jersey number:': None}

# for i in range(0,100):
    #print(i, end= ' ')
# jersey_dict['jersey number:'] = input1

# print(jersey_dict)

# NOTE left off trying to figure out how to get user to input many variables in req'd format as in the question