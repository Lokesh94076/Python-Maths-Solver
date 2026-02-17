import json
import os


def find_file_path_os(filename):
    # Get the absolute path of the current script's directory
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the full path to the target file
    target_file_path = os.path.join(script_dir, filename)
    return target_file_path


def add_function_to_json(file_path, key, category, args, description):
    # 1. Check if file exists, if not, create an empty dict
    if os.path.exists(find_file_path_os(file_path)):
        with open(find_file_path_os(file_path), "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    # 2. Reliability Check: No Overwrite
    if key in data:
        raise ValueError("Documentation already exists. - error")
        return

    # 3. Add new data
    data[key] = {"category": category, "args": args, "description": description}

    # 4. Save back to file with nice formatting
    with open(find_file_path_os(file_path), "w") as f:
        json.dump(data, f, indent=2)

    return f"Successfully added: {key} to {file_path}"


# Documentation Files
file_total = "database\\Documentation_total.json"
file_smp = "database\\Documentation_smp.json"
file_adv = "database\\Documentation_adv.json"
file_cmplx = "database\\Documentation_cmplx.json"
file_const = "database\\Documentation_const.json"


# This should work
def add(name, category, arg, description):
    # adds to _total.json
    total = add_function_to_json(
        file_total,
        name,
        category,
        arg,
        description,
    )

    # add to particular category
    category = category.strip().lower()  # normalize for if statements
    all_category = ["smp", "adv", "cmplx", "const"]
    n = 0  # for loop counter
    category_found = ""
    # search algorithm
    for i in range(len(all_category)):
        if category == all_category[n]:
            category_found = all_category[n]
        n += 1

    # shitty slop
    if category_found == all_category[0]:
        categ = add_function_to_json(
            file_smp,
            name,
            category,
            arg,
            description,
        )
    elif category_found == all_category[1]:
        categ = add_function_to_json(
            file_adv,
            name,
            category,
            arg,
            description,
        )
    elif category_found == all_category[2]:
        categ = add_function_to_json(
            file_cmplx,
            name,
            category,
            arg,
            description,
        )
    elif category_found == all_category[3]:
        categ = add_function_to_json(
            file_const,
            name,
            category,
            arg,
            description,
        )
    # not quite sure
    else:
        raise ValueError("Category does not exist.")
    return True
