class Singleton:
    """

    """
    __instance = None

    @staticmethod
    def get_instance():
        """
        static access method
        :return:
        """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __int__(self):
        """
        Virtually private constructor
        :return:
        """
        if Singleton.__instance is not None:
            raise Exception("This class is singleton")
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    s = Singleton()
    print(s)

    s = Singleton.get_instance()
    print(s)

    s = Singleton.get_instance()
    print(s)