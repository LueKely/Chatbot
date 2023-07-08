from collections import deque
from datetime import datetime


class MyQueue:
    def __init__(self) -> None:
        self._value = deque([])
        self._now = datetime.now()

    def enqueue(self):
        name = input("DIWATA: What is your name? \nUser: ")
        print("DIWATA: you are now queued to an appointment!!")
        self._value.append("Name: "+name + " date: " +
                           self._now.strftime("%b/%d/%Y - %H:%M:%S"))

    def dequeue(self):
        if not self._value:
            print("But the appointment is empty")
        else:
            print("now dequeueing  " + self._value[0])
            self._value.popleft()

    def look(self):
        print(self._value)

    def peek(self):
        if not self._value:
            print("DIWATA: Looks like no one is inline")
        else:
            print("Diwata: ahead inline is " + self._value[0])
