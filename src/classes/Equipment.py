class MyEquipment:
    def __init__(self):
        self._need = set([])
        self._have = set([])
        self._union = set([])
        self._diff = set([])

    def get_all(self):
        print("DIWATA: Here are the sets")
        print("DIWATA: What you need")
        print(self._need)
        print("DIWATA: And what you have")
        print(self._have)

    def set_need(self):
        user_input = input(
            "DIWATA: Please insert a value to the set of equipment that you need \n USER: ")
        self._need.add(user_input)
        print("DIWATA: Value Added")

    def set_have(self):
        user_input = input(
            "DIWATA: Please insert a value to the set of equipment that you have in possession \n USER: ")
        self._have.add(user_input)
        print("DIWATA: Value Added")

    def del_need(self):
        user_input = input(
            "DIWATA: Please insert a value to the set of equipment that you need to delete \n USER: ")
        self._need.remove(user_input)
        print("DIWATA: Value deleted")

    def del_have(self):
        user_input = input(
            "DIWATA: Please insert a value to the set of equipment \nthat you have in possession the you want to delete \n USER: ")
        self._have.remove(user_input)
        print("DIWATA: Value deleted")

    def look(self):
        print("These are the equipment that you need")
        print(self._need)
        print("These are the equipment that you currently have")
        print(self._have)

    def intersect(self):
        self._union = self._have.intersection(self._need).copy()

    def difference(self):
        self._diff = self._need.difference(self._have).copy()

    def call(self):
        if (len(self._diff) != 0):
            print(
                "DIWATA: these are all the equipment that you should have but you should bring but did not")
            print(self._diff)
            print("DIWATA: These are all the equiment that you have that is in the set of things you have brought correctly")
            print(self._union)
            print("DIWATA ")
        else:
            print("DIWATA: You have brought all the right equipment")
