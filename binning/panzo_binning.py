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


def prompt_for_width():
    """Asks users to input either bin for width or frequency"""

    while True:
        inputted_choice = input("Enter the method (width / frequency): ").lower()

        if inputted_choice == "width":
            return True
        elif inputted_choice == "frequency":
            return False
        else:
            print('Type either "width" or "frequency". ', end="")


# TODO: input arrays, bin amount, and method
numbers = sorted(prompt())
bins = bin_prompt()

if prompt_for_width():
    # bin for width
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
else:
    # bin for frequency
    # TODO: take the number of elements
    numbers_length = len(numbers)

    # TODO: calculate the frequency for each bin
    frequency = round(numbers_length / bins)

    # TODO: loop through each elements and identify boundaries
    boundaries = []
    count = frequency - 1
    bin_count = bins - 1
    while count < numbers_length and bin_count > 0:
        boundaries.append((numbers[count] + numbers[count + 1]) / 2)
        count = count + frequency
        bin_count = bin_count - 1

    # TODO: loop through for binning
    prev_boundary = "-∞"
    count = 1

    for boundary in boundaries:
        bin_list = []
        while numbers[0] < boundary:
            bin_list.append(numbers.pop(0))
        print(f"Bin {count} [{prev_boundary}, {boundary}): ", end="")
        for num in bin_list:
            print(f"{num} ", end="")
        print()
        prev_boundary = boundary
        count = count + 1
    print(f"Bin {count} [{prev_boundary}, ∞): ", end="")
    for num in numbers:
        print(f"{num} ", end="")
