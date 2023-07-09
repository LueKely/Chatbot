class MyMedicine:
    def __init__(self,) -> None:
        self._list = []

    def get_data(self):
        if len(self._list) == 0:
            print("DIWATA: Looks like the list is empty")
            return
        else:
            print("DIWATA: This is the list that you have written ")
        for item in self._list:
            print(item)

    def set_data(self):
        user_input = input("DIWATA: insert the medicine that you will buy")
        self._list.append(user_input)

    def get_head(self):
        print(f"DIWATA: The first item in the list is: {self._list[0]}")

    def get_tail(self):
        print(f"DIWATA: The last item in the list is: {self._list[-1]} ")

    def remove_tail(self):
        print(f"DIWATA: removed tail {self._list.pop()}")

    def remove(self):
        self.get_data()
        user_input = input("DIWATA: Insert the item you want to remove")
        try:
            print("Removing "+user_input)
            self._list.remove(user_input)
        except ValueError:
            print("DIWATA: Looks like this is not on the list")

    def remove_head(self):
        print("DIWATA: removed " + self._list.pop(0))
