# Program: Check Leap Year
# Author: M.Pallavi


def is_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 400, OR
    # 2. It is divisible by 4 but not divisible by 100

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    print("================================")
    print("        LEAP YEAR CHECKER")
    print("================================")

    try:
        year = int(input("Enter a year: "))

        if year <= 0:
            print("\nPlease enter a valid positive year.")
            return

        if is_leap_year(year):
            print(f"\n{year} is a Leap Year.")
            print("February has 29 days.")
        else:
            print(f"\n{year} is not a Leap Year.")
            print("February has 28 days.")

    except ValueError:
        print("\nInvalid input!")
        print("Please enter a valid integer year.")


if __name__ == "__main__":
    main()
