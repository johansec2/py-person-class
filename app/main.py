class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> list:
    result = []
    for person_dict in people:
        name = person_dict.get("name")
        age = person_dict.get("age")
        # Create the Person instance (it will be added to Person.people)
        person = Person(name, age)

        # Check if there's a wife or husband key
        if "wife" in person_dict and person_dict.get("wife") is not None:
            person.wife = Person.people[person_dict.get("wife")]
        elif ("husband" in person_dict 
              and person_dict.get("husband") is not None):
            person.husband = Person.people[person_dict.get("husband")]

        result.append(person)

    return result
