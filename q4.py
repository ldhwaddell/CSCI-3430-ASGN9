import sys


def validate_input():
    try:
        sqft = input("Input the size of the driveway in square feet: ")
        depth = input("Input the depth of the driveway in inches: ")

        try:
            sqft = int(sqft)
        except ValueError:
            raise ValueError("[-] Error: Input size must be an integer")

        try:
            depth = int(depth)
        except ValueError:
            raise ValueError("[-] Error: Input depth must be an integer")

        if sqft < 1:
            raise ValueError("[-] Error: Input size must be greater than 0")

        if depth < 1:
            raise ValueError("[-] Error: Input depth must be greater than 0")

        return {"sqft": sqft, "depth": depth}

    except ValueError as err:
        raise err


def calculate_price(input):
    cubic_feet = int(input["sqft"] * input["depth"] / 12)
    price = 0

    if cubic_feet <= 199:
        price = 1000
    elif cubic_feet > 199 and cubic_feet <= 399:
        price = 1000 + (10 * (cubic_feet - 199))
    elif cubic_feet >= 400:
        price = 1000 + (10 * (cubic_feet - 199)) + (20 * (cubic_feet - 399))
    return price


if __name__ == "__main__":
    try:
        input = validate_input()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
    else:
        price = calculate_price(input)
        print(price)