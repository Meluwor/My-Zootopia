import json
import requests

def load_data(file_path):
  """
  Loads a JSON file.
  """
  with open(file_path, "r") as handle:
    return json.load(handle)

def get_api_key_from_user():
    """
    This function just takes an api-key from the user.
    """
    api_key = input("Please enter your API-Key. ")
    return api_key

def is_valid_api_key(api_key):
  """
  A simple check if the given key is valid.
  """
  #could ba any other available animal
  animal_name = "fox"

  url = f"https://api.api-ninjas.com/v1/animals?X-Api-Key={api_key}&name={animal_name}"
  res = requests.get(url)
  if res.status_code == 200:
    return True
  print("The given key is not valid. Loading data from json file.")
  return False


def fetch_data(api_key, animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = f"https://api.api-ninjas.com/v1/animals?X-Api-Key={api_key}&name={animal_name}"
  res = requests.get(url)
  return res.json()


