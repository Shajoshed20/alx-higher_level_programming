#!/usr/bin/python3

"""A class Student that defines a student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Student class initialization.

        Args:
            first_name: Student's first name as string.
            last_name: Student's last name as string.
            age: Student's age in integer.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
