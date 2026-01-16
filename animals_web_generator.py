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
    new_animal = {"name": None, "diet": None, "type": None, "location": None, "color": None,
                  "skin_type": None, "lifespan": None}

    new_animal["name"] = animal.get("name")

    characteristics = animal.get("characteristics", {})
    new_animal["diet"] = characteristics.get("diet")
    new_animal["type"] = characteristics.get("type")
    new_animal["color"] = characteristics.get("color")
    new_animal["skin_type"] = characteristics.get("skin_type")
    new_animal["lifespan"] = characteristics.get("lifespan")

    location = animal.get("locations")
    if len(location) > 0:
        new_animal["location"] = animal.get("locations")[0]

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
    animal_color = new_animal["color"]
    animal_skin_type = new_animal["skin_type"]
    animal_lifespan = new_animal["lifespan"]

    animal_string = ""
    animal_string += '<li class="cards__item">\n'
    #I expect a name for each animal else this needs to be changed a bit
    if animal_name:
        animal_string += f'<div class ="card__title" > {animal_name} </div>\n'
    animal_string += f'<div>'
    animal_string += '<ul class="card__attributes">'
    if animal_diet:
        animal_string += f'<li class="card__attribute"><strong>Diet:</strong> {animal_diet}</li>\n'
    if animal_location:
        animal_string += f'<li class="card__attribute"><strong>Location:</strong> {animal_location}</li>\n'
    if animal_type:
        animal_string += f'<li class="card__attribute"><strong>Type:</strong> {animal_type}</li>\n'
    if animal_color:
        animal_string += f'<li class="card__attribute"><strong>Color:</strong> {animal_color}</li>\n'
    if animal_skin_type:
        animal_string += f'<li class="card__attribute"><strong>Skin type:</strong> {animal_skin_type}</li>\n'
    if animal_lifespan:
        animal_string += f'<li class="card__attribute"><strong>Lifespan:</strong> {animal_lifespan}</li>\n'
    animal_string += '</ul>'
    animal_string += '</div>\n'
    animal_string += "</li>\n"

    return animal_string

def get_animal_string(animals_data):
    """
    This function creates a string of all animals
    """
    animal_list = []
    for animal in animals_data:
        animal_list.append(serialize_animal(animal))

    return "".join(animal_list)


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