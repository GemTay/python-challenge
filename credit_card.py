import csv
import re


class CreditCard:

    def check_N_in_range(self, n):
        self.n = int(n)
        if self.n > 0 and self.n < 100:
            return True
        return False

    def validate_credit_numbers(self, numbers_array):

        if self.check_N_in_range(numbers_array[0]):

            for i in range(1, (self.n)+1):
                if (self.check_leading_digit(numbers_array[i]) and
                    self.check_correct_format(numbers_array[i]) and
                        self.check_repeating_digits(numbers_array[i])):

                    print("Credit card number %s is valid" % numbers_array[i])
                else:
                    print("Credit card number %s is NOT valid" %
                          numbers_array[i])

        print("N is not in range 0 < N < 100")

    def check_leading_digit(self, number):
        if not int(number[:1]) in [4, 5, 6]:
            return False
        return True

    def check_correct_format(self, number):
        matched = re.match(r"^(\d{4}-?){3}(\d{4})$", number)
        if not matched:
            return False
        return True

    def check_repeating_digits(self, number):
        l = number.replace('-', '')
        all_slices = [l[i:i+4] for i in range(len(l)-3)]
        for slice in all_slices:
            if (all(element == slice[0] for element in slice)):
                return False
        return True

    def read_csv(self, csv_file):
        credit_numbers = []
        file = open(csv_file, "r")
        reader = csv.reader(file)
        for line in reader:
            credit_numbers.append(line[0])
        return credit_numbers


if __name__ == '__main__':
    numbers = CreditCard().read_csv("credit_card_numbers.csv")
    CreditCard().validate_credit_numbers(numbers)
