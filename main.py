
import os
from dataclasses import dataclass, fields
from csv import DictReader


def validate_dataclass_types(instance):
    for field in fields(instance):
        attr = getattr(instance, field.name)
        if not isinstance(attr, field.type):
            raise ValueError(f"{field.name} is type {field.type}, it should be {type(attr)}")


@dataclass
class Animal:
    """
    This class represents an animal.

    Attributes:
        name (str): The name of the animal.
        age (int): The age of the animal.
        breed (str): The breed of the animal.
    """

    name: str
    age: int
    breed: str

    def __post_init__(self):
        validate_dataclass_types(self)


def csv_to_dataclass(cls, filepath):
    types = {field.name: field.type for field in fields(cls)}

    with open(filepath) as f:
        for row in DictReader(f):
            yield cls(**{name: types[name](value) for name, value in row.items()})


def main():
    while True:
        print("We have these animals:")
        for f in os.listdir("data"):
            print(f.rsplit(".", 1)[0])

        response = input("What animal you want?")

        try:
            print(f"Reading {response} from csv...")
            for animal in csv_to_dataclass(Animal, f"data/{response}.csv"):
                print(animal)
            break
        except FileNotFoundError:
            print("File not found. Try again!")


if __name__ == "__main__":
    main()
