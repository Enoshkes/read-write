import json
from model.person import Person
from typing import List

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.__dict__
        return super().default(obj)

def write_people_to_json(people: List[Person], filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(people, jsonfile, cls=PersonEncoder, indent=4)

def read_people_from_json(filename: str) -> List[Person]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Person(person['name'], person['age']) for person in data]


def write_person_to_json(person: Person, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(person.__dict__, jsonfile, indent=4)

def read_person_from_json(filename: str) -> Person:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Person(data['name'], data['age'])