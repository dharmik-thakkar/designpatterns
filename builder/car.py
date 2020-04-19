# Car Parts
class Wheel:
    """

    """
    size = None


class Engine:
    """

    """
    horsepower = None


class Body:
    """

    """
    shape = None


# Car
class Car:
    """

    """
    def __int__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        """

        :param body:
        :return:
        """
        self.__body = body

    def attach_wheel(self, wheel):
        """

        :param wheel:
        :return:
        """
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        """

        :param engine:
        :return:
        """
        self.__engine = engine

    def specifications(self):
        """

        :return:
        """
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)


class Builder:
    """

    """
    def get_wheel(self):
        """

        :return:
        """
        pass

    def get_engine(self):
        """

        :return:
        """
        pass

    def get_body(self):
        """

        :return:
        """
        pass


class JeepBuilder(Builder):
    """

    """
    def get_wheel(self):
        """

        :return:
        """
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        """

        :return:
        """
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        """

        :return:
        """
        body = Body()
        body.shape = "SUV"
        return body


class Director:
    """

    """
    __builder = None

    def set_builder(self, builder):
        """

        :param builder:
        :return:
        """
        self.__builder = builder

    def get_car(self):
        """

        :return:
        """
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
        i += 1

        return car


def main():
    jeep_builder = JeepBuilder()  # initializing the class
    director = Director()
    # Build Jeep
    print("Jeep")
    director.set_builder(jeep_builder)
    jeep = director.get_car()
    jeep.specification()
    print("")


if __name__ == "__main__":
    main()
