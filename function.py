import json
import datetime


def load_operations():
    with open('operations.json', 'r') as file:
        data = json.load(file)
    return data


def hide_cards_number(raw_card):
    part_1 = raw_card[0:4]
    part_2 = raw_card[4:6] + '**'
    part_3 = '****'
    part_4 = raw_card[12:16]
    return f'{part_1} {part_2} {part_3} {part_4}'


def hide_invoice_number(invoice_number):
    return f'**{invoice_number[-4:]}'


def hide_numbers(value: str):
    ident, number = value.rsplit(' ', 1)
    if "счет" in ident.lower():
        secret_number = hide_invoice_number(number)
    else:
        secret_number = hide_cards_number(number)
    return f"{ident} {secret_number}"


def display_last_operations(operations, limit=5):
    executed_operations = [op for op in operations if op.get('state', '') == 'EXECUTED']
    last_executed_operations = sorted(
        executed_operations,
        key=lambda x: x['date'], reverse=True
    )[:limit]

    for operation in last_executed_operations:
        date = datetime.datetime.fromisoformat(operation['date']).date().strftime('%Y.%m.%d')
        to_operation = hide_numbers(operation['to'])

        print(f"{date} {operation['description']}")
        if 'from' in operation:
            from_operation = hide_numbers(operation['from'])
            print(f"{from_operation} -> {to_operation}")
        else:
            print(f" -> {to_operation}")

        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f"{amount} {currency}")


if __name__ == '__main__':
    display_last_operations(load_operations())
