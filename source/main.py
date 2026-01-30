# local modules


from . import synonyms as synonyms
from .distributor import adv_distributor as adv_distributor
from .distributor import cmplx_distributor as cmplx_distributor
from .distributor import smp_distributor as smp_distributor
from .doc import documentation, documentation_addition
from .tools import validate as validation


# SIMPLE - Function
# Type - Only deals with simple, one input; one output operations \ fundamental operations.
def smp(function_name, *inputs):
    for x in inputs:
        if not isinstance(x, (int, float)):
            raise ValueError("Call without any inputs.")
    if function_name in synonyms.Synonyms:
        filtered_function_name = synonyms.Synonyms[function_name]
    else:
        filtered_function_name = function_name
    # print(f"listed_input: {listed_input}\nfiltered-function: {filtered_function_name}\ninputs: {inputs}\n")
    return smp_distributor.distribute(filtered_function_name, *inputs)


# WIP
# ADVANCED - Function
# Type - Only deals data\transformation using logic of maths or python. Altho they also return a answer..  ##can change
def adv(function_name, *inputs):
    for x in inputs:
        if not isinstance(x, (int, float)):
            raise ValueError("Call without any inputs.")
    if function_name in synonyms.Synonyms:
        filtered_function_name = synonyms.Synonyms[function_name]
    else:
        filtered_function_name = function_name
    # print(f"listed_input: {listed_input}\nfiltered-function: {filtered_function_name}\ninputs: {inputs}\n")
    return adv_distributor.distribute(filtered_function_name, *inputs)


# COMPLEX - Function
# Type - Only deals with complex maths equations and stuff, usually a combination of adv and smp
def cmplx(function_name, *inputs):
    for x in inputs:
        if not isinstance(x, (int, float)):
            raise ValueError("Call without any inputs.")
    if function_name in synonyms.Synonyms:
        filtered_function_name = synonyms.Synonyms[function_name]
    else:
        filtered_function_name = function_name
    # print(f"listed_input: {listed_input}\nfiltered-function: {filtered_function_name}\ninputs: {inputs}\n")
    return cmplx_distributor.distribute(filtered_function_name, *inputs)


# WIP, SEE AGAGIN FOR RELIABILITY.
def doc(function_name):
    function_name = function_name.strip().lower()
    list_categories = ["smp", "adv", "cmplx", "total"]
    n = 0
    nu = 0
    filtered_function_name = ""
    for i in range(len(list_categories)):
        if function_name == list_categories[n]:
            return documentation.get_documentation(function_name, "file")
        n += 1
    else:
        if function_name in synonyms.Synonyms:
            filtered_function_name = synonyms.Synonyms[function_name]
        else:
            filtered_function_name = function_name
    while nu < len(list_categories):
        if filtered_function_name in documentation.get_documentation(
            list_categories[nu], "file"
        ):
            category = list_categories[nu]
            return documentation.get_documentation(filtered_function_name, category)
        nu += 1
    else:
        raise ValueError("Function not found in documentation. any")


# to add new files\categories, open documentation_addition.py, add new file paths, and new elif commands
def create_documentation(name, category, arg, description):
    name = name.strip().lower()
    return documentation_addition.add(name, category, arg, description)


def validate():
    # create the validation tool, to check if all command in the function exist in documentation.
    validation.start()
