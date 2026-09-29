from typing import Any
import random
import statistics


def full_name_import() -> list[Any]:
    with open('names_500000.txt', 'r') as file:
        full_names = file.readlines()

    full_name_list = []

    for full_name_items in full_names:
        capitalization: int = random.randint(1, 100)

        if 10 < capitalization <= 90:
            output_item_capitalization = full_name_items.upper()
        elif capitalization <= 10:
            output_item_capitalization_list = []
            capitalization_split = full_name_items.split(' ')

            for name_objects in capitalization_split:
                output_item_capitalization_list.append(name_objects.capitalize())

            output_item_capitalization = " ".join(output_item_capitalization_list)
        elif capitalization > 90:
            output_item_capitalization = full_name_items.lower()
        else:
            output_item_capitalization = full_name_items.upper()

        remove_periods: int = random.randint(1, 100)

        if remove_periods <= 50:
            output_item_formatted = output_item_capitalization.replace('.', '')
        elif capitalization > 50:
            output_item_formatted = output_item_capitalization
        else:
            output_item_formatted = output_item_capitalization

        full_name_list.append(output_item_formatted.replace('\n', ''))

    return full_name_list


def first_middle_last_split(full_name_inbound):
    full_first_middle_last_out = []
    for full_name in full_name_inbound:
        split_name = full_name.split(' ')
        if len(split_name) == 2:
            full_first_middle_last_out.append([split_name[0], '', split_name[1], full_name])
        if len(split_name) == 3:
            full_first_middle_last_out.append([split_name[0], split_name[1], split_name[2], full_name])

    return full_first_middle_last_out

def add_principal_balance(first_middle_last_full_inbound):

    names_with_balance: list[Any] = []

    for name_rows in first_middle_last_full_inbound:
        dist = statistics.NormalDist(mu=265000.0, sigma=120000.0)
        principal_balance = round(dist.samples(1)[0], 2)
        if principal_balance < 0.0:
            principal_balance = 0.0
        else:
            pass
        if principal_balance == 0.0:
            pif_flag = 'Y'
        else:
            pif_flag = 'N'
        principal_balance_row : list = [name_rows[0],name_rows[1],name_rows[2],name_rows[3],principal_balance,pif_flag]
        names_with_balance.append(principal_balance_row)

    return names_with_balance

def late_balance_fcl(balance_data):
    fcl_added : list[Any] = []

    for loan_balance in balance_data:
        if loan_balance[4] > 30000.0:
            in_fcl: int = random.randint(1, 200)

            if in_fcl == 1:
                dist = statistics.NormalDist(mu=loan_balance[4] / 25, sigma=(loan_balance[4] / 150))
                late_balance = round(dist.samples(1)[0], 2)
                loan_balance.append(round(late_balance,2))

                fcl_complete: int = random.randint(1, 2)
                if fcl_complete == 1:
                    loan_balance.append('A')
                elif fcl_complete == 2:
                    loan_balance.append('C')
            else:
                loan_balance.append(round(0.0,2))
                loan_balance.append('N')
        else:
            loan_balance.append(round(0.0, 2))
            loan_balance.append('N')

        fcl_added.append(loan_balance)

    return fcl_added

def append_address(loans_with_fcl_data):
    with open('addresses_500000.txt', 'r') as file:
        addresses_inbound = file.readlines()
        addresses_split: list[Any] = []

        for address in addresses_inbound:
            addresses_split.append(address.split(','))

    addresses_final: list[Any] = []

    for split_addresses in addresses_split:
        street_split_row = (split_addresses[0].split(' '))

        if len(street_split_row) == 3:
            street_split_row_out = [street_split_row[0],'',street_split_row[1],street_split_row[2]]
        elif len(street_split_row) == 4:
            street_split_row_out = [street_split_row[0],street_split_row[1],street_split_row[2],street_split_row[3]]
        else:
            street_split_row_out = [street_split_row[0],street_split_row[1],street_split_row[2],street_split_row[3]]

        # has no unit number
        if len(split_addresses) == 3:
            street_split_row_out.append('')

        # has unit number
        elif len(split_addresses) == 4:
            street_split_row_out.append(split_addresses[1])
            split_addresses.pop(1)

        else:
            street_split_row_out.append('')

        #append city
        street_split_row_out.append(split_addresses[1].strip())

        # append state
        street_split_row_out.append(split_addresses[2].strip().split(' ')[0])

        # append zip
        street_split_row_out.append(split_addresses[2].strip().split(' ')[1].replace('\n',''))

        capitalization: int = random.randint(1, 100)

        if capitalization < 5:
            street_split_row_out[1] = street_split_row_out[1].lower()
            street_split_row_out[2] = street_split_row_out[2].lower()
            street_split_row_out[3] = street_split_row_out[3].lower()
            street_split_row_out[4] = street_split_row_out[4].lower()
            street_split_row_out[5] = street_split_row_out[5].lower()
        if 5 < capitalization  <= 95:
            street_split_row_out[1] = street_split_row_out[1].upper()
            street_split_row_out[2] = street_split_row_out[2].upper()
            street_split_row_out[3] = street_split_row_out[3].upper()
            street_split_row_out[4] = street_split_row_out[4].upper()
            street_split_row_out[5] = street_split_row_out[5].upper()
        else:
            pass

        addresses_final.append(street_split_row_out)

    for i in range (0, len(loans_with_fcl_data)):
        for j in range (0, len(addresses_final[i])):
            loans_with_fcl_data[i].append(addresses_final[i][j])

    for items in loans_with_fcl_data:
        print(items)


full_name_list_out: list[str] = full_name_import()
first_middle_last_full_list: list[str] = first_middle_last_split(full_name_list_out)
names_with_balance_list : list[Any] = add_principal_balance(first_middle_last_full_list)
with_fcl_list :list[Any] = late_balance_fcl(names_with_balance_list)
append_address(with_fcl_list)

#with_fcl : list[Any] = late_balance_fcl(names_with_balance_list)
