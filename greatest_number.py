#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program finds the greatest number


def main():
    # This function finds the greatest number out of 3 inputted numbers

    print("Input 3 numbers and I will tell you the greatest number!")

    # Input
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    third_number = int(input("Third number: "))

    # Process
    if first_number > second_number:
        if first_number > third_number:
            print("The greatest number is {}!".format(first_number))
        else:
            print("The greatest number is {}!".format(third_number))
    else:
        if second_number > third_number:
            print("The greatest number is {}!".format(second_number))
        else:
            print("The greatest number is {}!".format(third_number))


if __name__ == "__main__":
    main()
