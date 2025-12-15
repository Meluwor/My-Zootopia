import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animal_info(animal):
    """
    This function gets all info of an animal if possible and returns a "new animal" which just
    have the needed info to display.
    """
    new_animal = {"name": None, "diet": None, "type": None, "location": None}
    if "name" in animal:
        new_animal["name"] = animal["name"]
    if "characteristics" in animal:
        character = animal["characteristics"]
        if "diet" in character:
            new_animal["diet"] = character["diet"]
        if "type" in character:
            new_animal["type"] = character["type"]
    if "locations" in animal:
        if len(animal["locations"]) > 0:
            new_animal["location"] = animal["locations"][0]
    return new_animal


def serialize_animal(animal):
    """
    This function serialize an animal.
    """
    new_animal = get_animal_info(animal)
    animal_name = new_animal["name"]
    animal_diet = new_animal["diet"]
    animal_type = new_animal["type"]
    animal_location = new_animal["location"]

    animal_string = ""
    animal_string += '<li class="cards__item">\n'
    if animal_name:
        animal_string += f'<div class ="card__title" > {animal_name} </div>\n'
    animal_string += f'<p class="card__text">'
    if animal_diet:
        animal_string += f'<strong>Diet:</strong> {animal_diet}<br/>\n'
    if animal_location:
        animal_string += f'<strong>Location:</strong> {animal_location}<br/>\n'
    if animal_type:
        animal_string += f'<strong>Type:</strong> {animal_type}<br/>\n'
    animal_string += '</p>\n'
    animal_string += "</li>\n"

    return animal_string

def get_animal_string(animals_data):
    """
    This function creates a string of all animals
    """
    animal_string =""
    for animal in animals_data:
        animal_string += serialize_animal(animal)
    return animal_string


def get_template_as_string(path):
    """
    This function returns the given template as string
    """
    with open(path, "r") as a:
        data = a.read()
    return data


def save_data(path,data):
    """
    This function creates a new "html" file
    """
    with open(path,"w")as a:
        a.write(data)


def main():
    animals_data = load_data('animals_data.json')
    template_string = get_template_as_string("animals_template.html")
    animal_string = get_animal_string(animals_data)
    new_template_string = template_string.replace("__REPLACE_ANIMALS_INFO__", animal_string)
    save_data("animals.html",new_template_string)

if __name__ == "__main__":
    main()