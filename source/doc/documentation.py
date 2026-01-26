import json
import os


def Open_File(Name):
    def find_file_path_os(filename):
        # Get the absolute path of the current script's directory
        script_dir = os.path.abspath(os.path.dirname(__file__))
        # Construct the full path to the target file
        target_file_path = os.path.join(script_dir, filename)
        return target_file_path

    with open(
        find_file_path_os("database\\Documentation_" + Name + ".json"), "r"
    ) as file:
        document = json.load(file)
        return json.dumps(document, indent=4)


# To find a category, we can do if == category, and else: will be to just see if the thing exists in synonyms,
# if yes, get that, and see all files, or if no, then just see all files, if not found : error
