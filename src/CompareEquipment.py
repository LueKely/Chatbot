import classes
import utils

switch = classes.MySwitch()
Equipment = classes.MyEquipment()


def compare():
    Equipment.difference()
    Equipment.intersect()
    Equipment.call()


my_dic = {"ahave": Equipment.set_have, "aneed": Equipment.set_need, "rhave": Equipment.del_have,
          "rneed": Equipment.del_need, "see": Equipment.get_all, "compare": compare, "menu": switch.change_value}


def run():
    print("DIWATA: You have initialized the equipment check section")

    while True:
        if switch._value == False:
            break
        else:
            userInput = input("USER: ")
            utils.find_value_in_dict(utils.split_messages(userInput), my_dic)
