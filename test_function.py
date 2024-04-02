from typing import List, Dict

from function import display_last_operations


def load_operations(data=None):
    load_operations()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(isinstance(op, dict) for op in data)


def test_display_last_operations():
    operations: list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]] = [
        {'date': '2022-01-15', 'description': 'Payment', 'state': 'EXECUTED', 'from': 'Account1', 'to': 'Account2',
         'operationAmount': 100},
        {'date': '2022-01-14', 'description': 'Transfer', 'state': 'EXECUTED', 'from': 'Account3', 'to': 'Account4',
         'operationAmount': 50},
        {'date': '2022-01-13', 'description': 'Payment', 'state': 'PENDING', 'to': 'Account5', 'operationAmount': 75},
        {'date': '2022-01-12', 'description': 'Withdrawal', 'state': 'EXECUTED', 'from': 'Account6',
         'operationAmount': 30}
    ]

#     assert capture_stdout(display_last_operations,
#                           operations) == "2022-01-15 Payment\nAccount1 -> Account2\n100\n2022-01-14 Transfer\nAccount3 -> Account4\n50\n2022-01-12 Withdrawal\nAccount6 -> Account7\n30\n"
#
#
# def capture_stdout(func, *args):
#     from io import StringIO
#     import sys
#     old_stdout = sys.stdout
#     sys.stdout = mystdout = StringIO()
#     func(*args)
#     sys.stdout = old_stdout
#     return mystdout.getvalue()
