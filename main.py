
from dataclasses import dataclass
from csv import DictReader


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

    def __postinit__(self):
        if not isinstance(self.age, int):
            try:
                self.age = int(self.age)
            except ValueError:
                raise ValueError('Age must be an integer')

    # TODO maybe read from static methods


def read_animals_from_csv(csv_path):
    with open(csv_path) as f:
        reader = DictReader(f)
        for row in reader:
            yield Animal(**row)


def main():
    print("Reading dogs from csv...")
    for dog in read_animals_from_csv("data/dogs.csv"):
        print(dog)

    print("\nReading cats from csv...")
    for cat in read_animals_from_csv("data/cats.csv"):
        print(cat)


if __name__ == '__main__':
    main()
