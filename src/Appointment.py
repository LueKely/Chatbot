import classes
import utils

queue = classes.MyQueue()
switch = classes.MySwitch()

my_dic = {"peek": queue.peek, "ahead": queue.look,
          "fall": queue.enqueue, "finished": queue.dequeue, "menu": switch.change_value, "look": queue.look}


def run():
    print("DIWATA: You have initialized the appointment section")

    while True:
        if switch._value == False:
            break
        else:
            userInput = input("USER: ")
            utils.find_value_in_dict(utils.split_messages(userInput), my_dic)
