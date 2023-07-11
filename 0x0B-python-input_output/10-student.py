#!/usr/bin/python3

"""A class Student that defines a student"""


class Student:
    """A class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Class intialisation from 9-student.py.

        Args:
            first_name: Student's first name as string.
            last_name: Student's last name as string.
            age: Student's age in integer.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method to retrieves a dictionary representation of
            a Student instance
        """
        if (type(attrs) == list and
                all(type(name) == str for name in attrs)):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
