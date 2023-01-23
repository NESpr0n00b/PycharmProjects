import math


def prompt():
    """Tells the user to input integers seperated by comma to generate a list"""

    while True:
        isnumeric = True
        inputted_nums = input("Input integers, seperated by commas (ex. 1,2,3): ")
        numbers_list = inputted_nums.split(",")

        for num in numbers_list:
            num = num.strip()
            if not num.isnumeric():
                isnumeric = False
                break
            num = int(num)

        if isnumeric:
            return [eval(num) for num in numbers_list]
        else:
            print("Invalid input. ", end="")


def bin_prompt():
    """Asks users to input number of bins"""

    while True:
        inputted_num = input("Enter the number of bins generated (each will be exported on the same folder): ")

        if inputted_num.isnumeric():
            return int(inputted_num)
        else:
            print("Invalid input. ", end="")


# TODO: input arrays and bin
numbers = sorted(prompt())
bins = bin_prompt()

# TODO: take the start, end, and range
start = numbers[0]
end = numbers[-1]
number_range = end - start

# TODO: calculate each interval
interval = math.ceil(number_range / bins)

# TODO: loop through each bin
upper_boundary = start
lower_boundary = start
count = 1

while upper_boundary < end:
    upper_boundary = lower_boundary + interval
    if count == bins:
        print(f"Bin {count} [{lower_boundary}, ∞): ", end="")
        for num in numbers:
            print(f"{num} ", end="")
    else:
        bin_list = []
        while numbers[0] < upper_boundary:
            bin_list.append(numbers.pop(0))
        print(f"Bin {count} [{lower_boundary}, {upper_boundary}): ", end="")
        for num in bin_list:
            print(f"{num} ", end="")
    print()
    lower_boundary = upper_boundary
    count = count + 1