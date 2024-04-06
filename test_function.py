import pytest
from unittest.mock import patch

import json
from function import (
    hide_numbers, hide_invoice_number, hide_cards_number,
    sort_operations_by_date, display_operation, display_last_operations, filter_operation_by_state
)

TEST_OPERATIONS_JSON = """
[
    {
        "date": "2024-04-01T12:00:00",
        "description": "Test operation 1",
        "to": "Card 1234567890123456",
        "operationAmount": {"amount": 100, "currency": {"name": "USD"}},
        "state": "EXECUTED"
    },
    {
        "date": "2024-04-02T12:00:00",
        "description": "Test operation 2",
        "to": "Invoice 12345678",
        "operationAmount": {"amount": 200, "currency": {"name": "EUR"}},
        "state": "PENDING"
    },
    {
        "date": "2024-04-01T11:00:00",
        "description": "Test operation 0",
        "to": "Card 1234567890123456",
        "operationAmount": {"amount": 100, "currency": {"name": "USD"}},
        "state": "EXECUTED"
    },
    {
        "date": "2024-04-02T14:00:00",
        "description": "Test operation 3",
        "to": "Invoice 12345679",
        "operationAmount": {"amount": 300, "currency": {"name": "RUB"}},
        "state": "PENDING"
    },
    {
        "date": "2024-04-01T13:00:00",
        "description": "Test operation 4",
        "to": "Card 1234567890123456",
        "operationAmount": {"amount": 50, "currency": {"name": "RUB"}},
        "state": "EXECUTED"
    }
]
"""


@pytest.fixture
def operations_data():
    return json.loads(TEST_OPERATIONS_JSON)


def test_hide_cards_number():
    assert hide_cards_number("1234567890123456") == "1234 56** **** 3456"
    assert hide_cards_number('9876543210987654') == '9876 54** **** 7654'


def test_hide_invoice_number():
    assert hide_invoice_number('1234567890') == '**7890'
    assert hide_invoice_number('0987654321') == '**4321'


def test_hide_numbers_invoice():
    assert hide_numbers('Card Number: 1234567890123456') == 'Card Number: 1234 56** **** 3456'
    assert hide_numbers('Счет: 1234567890') == 'Счет: **7890'


def test_filter_operation_by_state(operations_data):
    filtered = filter_operation_by_state(operations_data, 'PENDING')
    assert len(filtered) == 2

    filtered = filter_operation_by_state(operations_data, 'EXECUTED')
    assert len(filtered) == 3
    assert filtered[0]['description'] == "Test operation 1"
    assert filtered[1]['description'] == "Test operation 0"
    assert filtered[2]['description'] == "Test operation 4"


def test_sort_operations_by_date(operations_data):
    sorted_ops = sort_operations_by_date(operations_data)
    assert len(sorted_ops) == 5
    assert sorted_ops[0]['description'] == "Test operation 0"
    assert sorted_ops[1]['description'] == "Test operation 1"
    assert sorted_ops[2]['description'] == "Test operation 4"


@patch("builtins.print")
def test_display_operation(mock_print, operations_data):
    display_operation(operations_data[0])
    mock_print.assert_called()


@patch("function.display_operation")
@patch("function.load_operations", return_value=json.loads(TEST_OPERATIONS_JSON))
def test_display_last_operations(mock_load, mock_display, operations_data):
    display_last_operations(operations_data)
    assert mock_display.call_count == 3
