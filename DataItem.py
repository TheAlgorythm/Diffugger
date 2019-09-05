from enum import Flag, auto


class DataItem:

    class ValueType(Flag):
        STRING = auto()
        BINARY = auto()
        HEXADECIMAL = auto()
        PASSWORD = auto()

    def __init__(self):
        self.name = str()
        self.type = DataItem.ValueType.STRING
        self.value1 = str()
        self.value2 = str()
