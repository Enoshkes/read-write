from model.person import Person
from repository.csv_repository import write_people_to_csv, write_person_to_csv, read_people_from_csv
from repository.json_repository import write_people_to_json, write_person_to_json, read_person_from_json

if __name__ == '__main__':
    p = [
        Person(name="enosh", age=34),
        Person(name="lior", age=30),
        Person(name="avi", age=39),
        Person(name="alef", age=35),
        Person(name="koby", age=25),
    ]

    print(
        read_person_from_json('./person.json')
    )

