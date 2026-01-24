import json
import os


# Open JSON for Synonyms
def find_file_path_os(filename):
    # Get the absolute path of the current script's directory
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the full path to the target file
    target_file_path = os.path.join(script_dir, filename)
    return target_file_path


with open(find_file_path_os("synonyms.json"), "r") as file:
    Synonyms = json.load(file)


# Open Json - END


# Open Documentaiton - START


def find_file_path_os(filename):
    # Get the absolute path of the current script's directory
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the full path to the target file
    target_file_path = os.path.join(script_dir, filename)
    return target_file_path


with open(find_file_path_os("Documentation.json"), "r") as file:
    Docu = json.load(file)

# Open Documentaiton - END
