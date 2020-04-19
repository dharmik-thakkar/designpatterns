class Button(object):
    """

    """
    html = ""

    def get_html(self):
        """

        :return:
        """
        return self.html


class Image(Button):
    """

    """
    html = "<img></img>"


class Input(Button):
    """

    """
    html = "<input></input>"


class Flash(Button):
    """

    """
    html = "<obj></obj>"


class ButtonFactory(object):
    """

    """
    def create_button(self, type):
        """
        
        :param type:
        :return:
        """
        target_class = type.capitalize()
        return globals()[target_class]()


if __name__ == "__main__":
    button_obj = ButtonFactory()
    button = ['image', 'input', 'flash']
    for b in button:
        print(button_obj.create_button(b).get_html())
