import classes
import utils

switch = classes.MySwitch()
Equipment = classes.MyEquipment()


def compare():
    Equipment.difference()
    Equipment.intersect()
    Equipment.call()


my_dic = {"add have": Equipment.set_have, "add need": Equipment.set_need, "remove have": Equipment.del_have,
          "remove need": Equipment.del_need, "see": Equipment.get_all, "compare": compare, }


def run():
    print("DIWATA: You have initialized the equipment check section")

    while True:
        if switch._value == False:
            break
        else:
            userInput = input("USER: ")
            utils.find_value_in_dict(utils.split_messages(userInput), my_dic)
