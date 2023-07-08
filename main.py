import re

from others.Title import say_title_name
from responses import GenericResponses
from responses import HealthTips


def split_messages(message):
    return re.split(r'\s+|[,;?!.-]\s*', message.lower())


def find_value_in_dict(array, dictionary):
    for key in array:
        if key in dictionary:
            function = dictionary[key]
            function()  # Execute the function


hello = True


def farewell():
    print("DIWATA: goodbye, I hope that i have assited you!!")
    global hello
    hello = False


my_dic = {'hello': GenericResponses.say_hi, "who": GenericResponses.introduction,
          "help": GenericResponses.help, "prank": GenericResponses.prank, 'goodbye': farewell, "tips": HealthTips.sayTips}


def main():
    say_title_name()
    while True:
        user_input = input("USER: ")
        find_value_in_dict(split_messages(user_input), my_dic)
        if hello == False:
            break


if __name__ == '__main__':
    main()
