import json


def load_operations():
    with open('operations.json' 'r') as file:
        data = json.load(file)
    return data


def display_last_operations(operations):
    executed_operations = [op for op in operations if op['state'] == 'EXECUTED']
    last_executed_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    for operation in last_executed_operations:
        print(f"{operation['date']} {operation['description']}")
        if 'from' in operation:
            print(f"{operation['from']} -> {operation['to']}")
        else:
            print(f"Карта -> {operation['to']}")
        print(f"{operation['operationAmount']}")
