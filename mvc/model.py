import json


class Person(object):
    """
    Class representing a Person
    """
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        """
        Method to get the name of Person's object
        :return:
        """
        return self.first_name, self.last_name

    @classmethod
    def get_all(self):
        """

        :return:
        """
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result
