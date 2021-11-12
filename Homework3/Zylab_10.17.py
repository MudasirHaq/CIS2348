# Mudasir Haq
# 1834539


class ItemToPurchase:
    item_name = str()
    item_price = float()
    item_quantity = int()

    #__init__ is a constructor because it creates an object with attributes
    def __init__(self, itn='none', ip=0, iq=0):
        self.item_name = itn
        self.item_price = ip
        self.item_quantity = iq

        # method can only be linked back to __init__ constructor when mentioned
        # self.print_item_cost()

    def get_item_cost(self):
        return (self.item_quantity * self.item_price)

    def print_item_cost(self):
        item_cost = self.get_item_cost()
        item_info =  '{} {} @ ${} = ${}'.format(self.item_name,
                                            self.item_quantity,
                                            self.item_price,
                                            item_cost)
        return item_info


if __name__ == "__main__":

    item_list = []
    total_cost = []
    count = 0
    while True:
        count += 1

        print('Item {}'.format(count))
        user_itemn = input('Enter the item name:\n')
        user_iq = input('Enter the item price:\n')
        user_ip = input('Enter the item quantity:\n')
        print()

        item = ItemToPurchase(user_itemn, int(user_iq), int(user_ip))

        item_list.append(item)

        if count == 2:
            break

    print('TOTAL COST')
    for it in item_list:
        print(it.print_item_cost())
        total_cost.append(it.get_item_cost())
    print()
    print('Total: ${}'.format(sum(total_cost)))

