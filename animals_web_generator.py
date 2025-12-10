import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animal_info(animal):
    """
    This function gets all info of an animal if possible
    """
    animal_name = None
    animal_diet = None
    animal_type = None
    animal_location = None
    if "name" in animal:
        animal_name = animal["name"]
    if "characteristics" in animal:
        character = animal["characteristics"]
        if "diet" in character:
            animal_diet = character["diet"]
        if "type" in character:
            animal_type = character["type"]
    if "locations" in animal:
        if len(animal["locations"]) > 0:
            animal_location = animal["locations"][0]
    return animal_name, animal_diet, animal_type, animal_location


def print_animal_info(animals_data):
    """
    This function prints all data of an animal.
    """
    for animal in animals_data:
        animal_name, animal_diet, animal_type, animal_location = get_animal_info(animal)
        if animal_name:
            print("Name: ", animal_name)
        if animal_diet:
            print("Diet: ", animal_diet)
        if animal_location:
            print("Location: ", animal_location)
        if animal_type:
            print("Type: ", animal_type)
        print()
        print()


def main():
    animals_data = load_data('animals_data.json')
    print_animal_info(animals_data)


if __name__ == "__main__":
    main()