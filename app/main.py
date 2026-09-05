class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self



def create_person_list(people: dict) -> list:
    result = []
    for person_dict in people:
        name = person_dict['name']
        age = person_dict['age']
        # Create the Person instance (it will be added to Person.people)
        person = Person(name, age)
        
        # Check if there's a wife or husband key
        if 'wife' in person_dict and person_dict['wife'] is not None:
            person.wife = Person.people[person_dict['wife']]
        elif 'husband' in person_dict and person_dict['husband'] is not None:
            person.husband = Person.people[person_dict['husband']]
        
        result.append(person)
    
    return result
