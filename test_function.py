from function import hide_cards_number, hide_invoice_number, hide_numbers


def test_hide_cards_number():
    assert hide_cards_number('1234567890123456') == '1234 56** **** 3456'
    assert hide_cards_number('9876543210987654') == '9876 54** **** 7654'


def test_hide_invoice_number():
    assert hide_invoice_number('1234567890') == '**7890'
    assert hide_invoice_number('0987654321') == '**4321'


def test_hide_numbers():
    assert hide_numbers('Card Number: 1234567890123456') == 'Card Number: 1234 56** **** 3456'
    assert hide_numbers('Счет: 1234567890') == 'Счет: **7890'
