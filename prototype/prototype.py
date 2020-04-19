import copy


class Prototype(object):
    """

    """
    _type = None
    _value = None

    def clone(self):
        """

        :return:
        """
        pass

    def get_type(self):
        """

        :return:
        """
        return self._type

    def get_value(self):
        """

        :return:
        """
        return self._value


class Type1(Prototype):
    """

    """
    def __int__(self, number):
        self._type = "Type 1"
        self._value = number

    def clone(self):
        return copy.copy(self)


class Type2(Prototype):
    """

    """
    def __int__(self, number):
        self._type = "Type 2"
        self._value = number

    def clone(self):
        return copy.copy(self)


class ObjectFactory:
    """
    Manages prototypes.
    Static factory, that encapsulates prototype
    initialization and then allows instatiation
    of the classes from these prototypes.
    """
    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        """

        :return:
        """
        ObjectFactory.__type1Value1 = Type1(1)
        ObjectFactory.__type1Value2 = Type1(2)
        ObjectFactory.__type2Value1 = Type2(1)
        ObjectFactory.__type2Value2 = Type2(2)

    @staticmethod
    def get_type1_value1():
        """

        :return:
        """
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def get_type1_value1():
        """

        :return:
        """
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def get_type1_value1():
        """

        :return:
        """
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def get_type1_value1():
        """

        :return:
        """
        return ObjectFactory.__type2Value2.clone()


def main():
    ObjectFactory.initialize()

    instance = ObjectFactory.get_type1_value1()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.get_type1_value2()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.get_type2_value1()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.get_type2_value2()
    print("%s: %s" % (instance.getType(), instance.getValue()))


if __name__ == "__main__":
    main()
