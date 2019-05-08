class Name:
    def __init__(self):
        self.name = "abc"
        self._name = "xyz"
        self.__name = "ABC"


if __name__ == "__main__":
    item = Name()
    print(item.name)
    print(item._name)
    # print(item.__name)
    print(item._Name__name)
