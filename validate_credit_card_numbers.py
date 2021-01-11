import csv
import re

class ValidateCreditCardNumbers:

    def check_N_in_range(self, n):
        self.n = int(n)
        #if n is 0?
        if self.n > 0 and self.n < 100:
            print("In range")
            self.validate_credit_numbers(self.credit_numbers)
        else:
            print("Not in range")

    def validate_credit_numbers(self, numbers_array):
        for i in range(1, (self.n)+1):
            if not int(numbers_array[i][:1]) in [4,5,6]:
                print("Credit card number %s does not begin with a 4, 5 or 6" % numbers_array[i])

            result = re.match(r"^(\d{4}-?){3}(\d{4})$", numbers_array[i])
            if not result:
                print("Credit card number %s is not in the correct format" % numbers_array[i])





    def read_csv(self):
        self.credit_numbers = []
        file=open("credit_card_numbers.csv", "r")
        reader = csv.reader(file)
        for line in reader:
            self.credit_numbers.append(line[0])

        self.check_N_in_range(self.credit_numbers[0])

if __name__ == '__main__':
    ValidateCreditCardNumbers().read_csv()
