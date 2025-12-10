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

def get_animal_string(animals_data):
    """
    This function creates a string of all animals
    """
    animal_string =""
    for animal in animals_data:
        animal_name, animal_diet, animal_type, animal_location = get_animal_info(animal)
        if animal_name:
            animal_string += f'Name: {animal_name}\n'
        if animal_diet:
            animal_string += f'Diet: {animal_diet}\n'
        if animal_location:
            animal_string += f'Location: {animal_location}\n'
        if animal_type:
            animal_string += f'Type: {animal_type}\n'
        animal_string +="\n"
    return animal_string


def get_template_as_string(path):
    with open(path, "r") as a:
        data = a.read()
    return data


def save_data(path,data):
    with open(path,"w")as a:
        a.write(data)


def main():
    animals_data = load_data('animals_data.json')
    template_string = get_template_as_string("animals_template.html")
    animal_string = get_animal_string(animals_data)
    new_template_string = template_string.replace("__REPLACE_ANIMALS_INFO__", animal_string)
    save_data("animals.html",new_template_string)
    print(new_template_string)

if __name__ == "__main__":
    main()