#Mudasir Haq
#1834539

def exact_change(user_total):
    dollars_count = user_total // 100
    user_total %= 100
    quarters_count = user_total // 25
    user_total %= 25
    dimes_count = user_total // 10
    user_total %= 10
    nickels_count = user_total // 5
    user_total %= 5
    pennies_count = user_total
    return dollars_count, quarters_count, dimes_count, nickels_count, pennies_count


if __name__ == '__main__':
    input_val = int(input())
    dollars_count, quarters_count, dimes_count, num_nickels, pennies_count = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    else:
        if dollars_count > 1:
            print(dollars_count, 'dollars')
        elif dollars_count == 1:
            print(dollars_count, 'dollar')

        if quarters_count > 1:
            print(quarters_count, 'quarters')
        elif quarters_count == 1:
            print(quarters_count, 'quarter')

        if dimes_count > 1:
            print(dimes_count, 'dimes')
        elif dimes_count == 1:
            print(dimes_count, 'dime')

        if num_nickels > 1:
            print(num_nickels, 'nickels')
        elif num_nickels == 1:
            print(num_nickels, 'nickel')

        if pennies_count > 1:
            print(pennies_count, 'pennies')
        elif pennies_count == 1:
            print(pennies_count, 'penny')