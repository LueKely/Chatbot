import utils
from others.Title import say_title_name
from responses import GenericResponses
from responses import HealthTips
import classes
import Appointment
import CompareEquipment
import CheckSymptomes
import stack
switch = classes.MySwitch()


def farewell():
    print("DIWATA: goodbye, I hope that i have assited you!!")
    switch.change_value()


# the list of commands, the key words will correspond to the function that
# will excute

my_dic = {'hello': GenericResponses.say_hi,
          "hi": GenericResponses.say_hi,
          "who": GenericResponses.introduction,
          "help": GenericResponses.help,
          "prank": GenericResponses.prank,
          'goodbye': farewell,
          "tips": HealthTips.sayTips,
          "appointment": Appointment.run,
          "equipment": CompareEquipment.run,
          "sick": CheckSymptomes.run,
          "kamusta": GenericResponses.tagalog,
          "patientlist": stack.run}


def main():
    say_title_name()
    while True:
        if switch._value == False:
            break
        else:
            user_input = input("USER: ")
            utils.find_value_in_dict(utils.split_messages(user_input), my_dic)


# runs the program
if __name__ == '__main__':
    main()
