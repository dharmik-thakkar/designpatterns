from mvc.model import Person
from mvc import view


def show_all():
    """

    :return:
    """
    people_in_db = Person.get_all()
    return view.show_all_view(people_in_db)


def start():
    """

    :return:
    """
    view.start_view()
    cli_input = input()
    if cli_input == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == "__main__":
    start()
