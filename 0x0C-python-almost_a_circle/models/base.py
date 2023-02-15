#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a base model class."""

import json
import csv
import turtle


class Base:
    """Base model.
    This Represents the "base" for all other classes in project 0x0C*.
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """

=======
"""Base Module"""
import json
import csv


class Base:
    """Base class
    Attributes:
        __nb_objects (int): class private attribute
        id (int): public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer
        Args:
            id (int): objects id
        """
>>>>>>> 4c31dc54f54bc3cd69f1e4986edcd137ed1edac8
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
<<<<<<< HEAD
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
=======
        """returns JSON format representaion"""
>>>>>>> 4c31dc54f54bc3cd69f1e4986edcd137ed1edac8
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
<<<<<<< HEAD
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
=======
        """writes JSON string representation
        Args:
            list_objs (list): list of instance
        """
        l = []
        if list_objs is not None:
            for d in list_objs:
                l.append(cls.to_dictionary(d))
        with open(str(cls.__name__ + ".json"), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON representation"""
        if json_string is None or json_string == '':
>>>>>>> 4c31dc54f54bc3cd69f1e4986edcd137ed1edac8
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
<<<<<<< HEAD
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
=======
        """Create from dictionnary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load from file"""
        filename = cls.__name__ + ".json"
        ll = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                a_dictionary = cls.from_json_string(f.read())
                for row in a_dictionary:
                    ll.append(cls.create(**row))
                return ll
>>>>>>> 4c31dc54f54bc3cd69f1e4986edcd137ed1edac8
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
<<<<<<< HEAD
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()
=======
        """Serialize a class to csv"""
        filename = cls.__name__ + ".csv"
        attributes = ["id", "x", "y"]
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id","width", "height", "x", "y"]
                else:
                    attributes = ["id","size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=attributes)
                for item in list_objs:
                    writer.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "w") as f:
                reader = csv.DictReader(f)
                ll = []
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    ll.append(row)
                return [cls.create(**item) for item in ll]
        except FileNotFoundError:
            return []


>>>>>>> 4c31dc54f54bc3cd69f1e4986edcd137ed1edac8
