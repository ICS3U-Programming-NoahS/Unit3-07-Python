#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct. 29th, 2023
# This program asks the user to enter their age
# and tells the user if they are allowed to date their granddaughter


def main():
    # Get the user's age
    user_age_string = input("Enter your age: ")

    # Making sure the user's age is an integer
    try:
        user_age_int = int(user_age_string)

        # Check if the user can date their grandchild
        if (user_age_int > 25) and (user_age_int < 40):
            print("You can date my grandchild.")
        elif (user_age_int >= 120) or (user_age_int <= 0):
            print("{} is not a valid age!".format(user_age_int))
        elif user_age_int >= 40:
            print("You are too old to date my grandchild.")
        else:
            print("You are too young to date my grandchild.")
    except:
        print("{} is not an integer!".format(user_age_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
