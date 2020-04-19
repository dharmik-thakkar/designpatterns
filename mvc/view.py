from mvc.model import Person


def show_all_view(obj_list):
    """

    :param obj_list:
    :return:
    """
    print('In our db we have %i users. Here they are:' % len(list))
    for item in obj_list:
        print(item.name())


def start_view():
    """

    :return:
    """
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def end_view():
    """

    :return:
    """
    print('Goodbye!')