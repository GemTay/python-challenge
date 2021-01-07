import csv

class ValidateCreditCardNumbers:

    def __init__(self):
        self.csv_as_array = []
        file=open("credit_card_numbers.csv", "r")
        reader = csv.reader(file)
        for line in reader:
            self.csv_as_array.append(line[0])

        print(self.csv_as_array)
        check_N_in_range(self.csv_as_array[0])

    def check_N_in_range(n):
        if n > 0 and n < 100:
            print("In range")
        else:
            print("Not in range")

ValidateCreditCardNumbers()
