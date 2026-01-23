# local modules
from . import distributor as distributor
from . import synonyms as synonyms


# SIMPLE - Function
def smp(function_name, *inputs):
    for x in inputs:
        if not isinstance(x, (int, float)):
            return "ERROR - Wrong format OR inputs"
    if function_name in synonyms.Synonyms:
        filtered_function_name = synonyms.Synonyms[function_name]
    else:
        filtered_function_name = function_name
    # print(f"listed_input: {listed_input}\nfiltered-function: {filtered_function_name}\ninputs: {inputs}\n")
    return distributor.distribute(filtered_function_name, *inputs)
