import json
import os


def find_file_path_os(filename):
    # Get the absolute path of the current script's directory
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the full path to the target file
    target_file_path = os.path.join(script_dir, filename)
    return target_file_path


def get_documentation(Name, type):
    if type == "file":
        #   Entire file/category or all
        with open(
            find_file_path_os("database\\Documentation_" + Name + ".json"), "r"
        ) as file:
            document = json.load(file)
            return json.dumps(document, indent=4)

    elif type == "smp":
        #   function in smp category
        with open(find_file_path_os("database\\Documentation_smp.json"), "r") as file:
            document = json.load(file)

        if Name in document:
            docu = document[Name]
            doc = json.dumps(docu, indent=4)
        else:
            raise ValueError(
                "Not Found in Documentation database - check the function name(priority)"
            )
        return doc

    elif type == "adv":
        with open(find_file_path_os("database\\Documentation_adv.json"), "r") as file:
            document = json.load(file)

        if Name in document:
            docu = document[Name]
            doc = json.dumps(docu, indent=4)
        else:
            raise ValueError(
                "Not Found in Documentation database - check the function name(priority)"
            )
        return doc

    elif type == "cmplx":
        with open(find_file_path_os("database\\Documentation_cmplx.json"), "r") as file:
            document = json.load(file)

        if Name in document:
            docu = document[Name]
            doc = json.dumps(docu, indent=4)
        else:
            raise ValueError(
                "Not Found in Documentation database - check the function name(priority)"
            )
        return doc

    else:
        raise ValueError("wrong internal input - documentation API")


# To find a category, we can do if == category, and else: will be to just see if the thing exists in synonyms,
# if yes, get that, and see all files, or if no, then just see all files, if not found : error
