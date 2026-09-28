from decimal import Decimal
from typing import Any


def first_name_and_percent_import() -> list[Any]:
    with open('1000_first_names.txt', 'r') as file:
        first_names = file.readlines()

    first_names.pop(0)

    first_name_and_percent = []

    for items in first_names:
        output_item: list[str] = items.split('\t')
        output_item_formatted = [output_item[0].capitalize(),Decimal(output_item[3].replace(',', ''))/100000]
        first_name_and_percent.append(output_item_formatted)

    return first_name_and_percent

def last_name_and_percent_import()  -> list[Any]:
    with open('1000_last_names.txt', 'r') as file:
        last_names = file.readlines()

    last_name_and_percent = []

    starting_stat = Decimal(.0076)

    zipf = 1

    for items in last_names:
        output_item: list[Any] = [items.replace('\n','').capitalize(), starting_stat / zipf]
        last_name_and_percent.append(output_item)
        zipf += 1
    return last_name_and_percent

first_name_stats: list[Any] = first_name_and_percent_import()

last_name_stats: list[Any] = last_name_and_percent_import()

for items in first_name_stats:
    print(items)

for items in last_name_stats:
    print(items)