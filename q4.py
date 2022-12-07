import sys


def validate_input():
    """
    Function to validate the user input and either return
    validated input or raise a value error
    """
    try:
        width = input("Input the width of the driveway in feet: ")
        length = input("Input the length of the driveway in feet: ")
        depth = input("Input the depth of the driveway in inches: ")

        try:
            width = int(width)
        except ValueError:
            raise ValueError(
                "[-] Error: Input width must be an integer. Program Exiting"
            )

        try:
            length = int(length)
        except ValueError:
            raise ValueError(
                "[-] Error: Input length must be an integer. Program Exiting"
            )

        try:
            depth = int(depth)
        except ValueError:
            raise ValueError(
                "[-] Error: Input depth must be an integer. Program Exiting"
            )

        if width < 1:
            raise ValueError(
                "[-] Error: Input width must be greater than 0. Program Exiting"
            )

        if length < 1:
            raise ValueError(
                "[-] Error: Input length must be greater than 0. Program Exiting"
            )

        if depth < 1:
            raise ValueError(
                "[-] Error: Input depth must be greater than 0. Program Exiting"
            )

        return (width, length, depth)

    except ValueError as err:
        raise err


def calculate_price(width, length, depth):
    """Function to calculate the price based on constraints in q4"""
    cubic_feet = int(width * length * (depth / 12))
    price = 0

    if cubic_feet <= 199:
        print("Breakdown: 1000")
        price = 1000

    elif cubic_feet > 199 and cubic_feet <= 399:
        print(f"Breakdown: 1000 + {10 * (cubic_feet - 199)}")
        price = 1000 + (10 * (cubic_feet - 199))

    elif cubic_feet >= 400:
        print(f"Breakdown: 1000 + 2000 + {20 * (cubic_feet - 399)}")
        price = 3000 + (20 * (cubic_feet - 399))

    return price


if __name__ == "__main__":
    try:
        width, length, depth = validate_input()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
    else:
        price = calculate_price(width, length, depth)
        print(f"${price}")
