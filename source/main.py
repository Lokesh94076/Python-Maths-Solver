# local modules
from . import synonyms as synonyms
from .distributor import adv_distributor as adv_distributor
from .distributor import cmplx_distributor as cmplx_distributor
from .distributor import smp_distributor as smp_distributor


# documentation access
def documentation(name):
    if name in synonyms.Docu:
        docu = synonyms.Docu[name]
    else:
        raise ValueError(
            "Not Found in Documentation database - check the function name(priority)"
        )
    return docu


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


# DOCUMENTATION return
def doc(function_name):
    if function_name == None:
        raise ValueError("Call without any inputs.")
    if function_name in synonyms.Synonyms:
        filtered_function_name = synonyms.Synonyms[function_name]
    else:
        filtered_function_name = function_name
    return documentation(filtered_function_name)
