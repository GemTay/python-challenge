import unittest
from unittest import mock
from unittest.mock import patch
import io

from credit_card import CreditCard


class CreditCardTest(unittest.TestCase):

    def test_convert_csv_to_array(self):
        numbers = CreditCard().read_csv("test_credit_card_numbers.csv")
        self.assertEqual([
            "3",
            "4123456789123456",
            "5123-4567-8912-3456",
            "51235-4567-8912-3456"
        ], numbers)

    def test_if_N_in_range(self):
        numbers = CreditCard().read_csv("test_credit_card_numbers.csv")

        with mock.patch('sys.stdout') as fake_stdout:
            CreditCard().validate_credit_numbers(numbers)

        fake_stdout.assert_has_calls([
            mock.call.write("N is not in range 0 < N < 100"),
        ])
