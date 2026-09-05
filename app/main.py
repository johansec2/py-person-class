class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    # Reset class-level registry to avoid leaking state between calls/tests
    Person.people = {}

    # First pass: create all Person instances using a list comprehension
    result: list[Person] = [
        Person(p.get("name"), p.get("age"))
        for p in people
    ]

    # Second pass: assign spouse relationships (lookups will succeed now)
    for person_dict in people:
        name = person_dict.get("name")
        person = Person.people.get(name)

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person.wife = Person.people.get(wife_name)

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return result
