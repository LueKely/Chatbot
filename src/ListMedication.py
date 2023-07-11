import classes
import utils

medication = classes.MyMedicine()
switch = classes.MySwitch()

my_dic = {"insert": medication.set_data,
          "look": medication.get_data,
          "head": medication.get_head,
          "end": medication.get_tail,
          "deltail": medication.remove_tail,
          "remove": medication.remove,
          "delhead": medication.remove_head, }


def run():
    print("DIWATA: You have initialized the appointment section")

    while True:
        if switch._value == False:
            break
        else:
            userInput = input("USER: ")
            utils.find_value_in_dict(utils.split_messages(userInput), my_dic)
