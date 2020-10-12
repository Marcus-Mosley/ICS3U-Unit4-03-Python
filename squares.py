#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program finds the squares of all natural numbers preceding the
#     number inputted by the user


def main():
    # This function finds the squares of all natural numbers preceding the
    #     number inputted by the user

    # Input
    counter = 0
    square = 0
    natural_string = input("Enter a natural number (To Find Sqaure 0 to N): ")
    print("")

    # Process & Output
    try:
        natural_integer = int(natural_string)
    except Exception:
        print("You have not inputted an integer, please input an integer"
              " (natural number)!")
    else:
        if natural_integer <= 0:
            print("You have not inputted a positive number, please input a"
                  " positive number!")
        else:
            for counter in range(natural_integer+1):
                square = counter**2
                print("The square of {0} is {1}".format(counter, square))


if __name__ == "__main__":
    main()
