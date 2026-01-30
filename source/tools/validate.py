import json
import os
from multiprocessing import Value

from ..distributor import adv_distributor, cmplx_distributor, smp_distributor


def find_file_path_os(filename):
    # Get the absolute path of the current script's directory
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the full path to the target file
    target_file_path = os.path.join(script_dir, filename)
    return target_file_path


# get functions from the distributor
smp_list = list(smp_distributor.OPS)
adv_list = list(adv_distributor.OPS)
cmplx_list = list(cmplx_distributor.OPS)
total_OPS = smp_list + adv_list + cmplx_list

# get function from documentation
with open(
    find_file_path_os("\\Math Engine\\source\\doc\\database\\Documentation_total.json"),
    "r",
) as file:
    total = json.load(file)
keys_list = list(total.keys())
number_of_function = len(keys_list)


def start():
    if number_of_function == len(total_OPS):
        print("Pass - Number of functions with total OPS is correct!")
    elif number_of_function <= len(total_OPS):
        print(
            "Fail - Number of function in documentaion(total) is smaller than total OPS!"
        )
    elif number_of_function >= len(total_OPS):
        print(
            "Fail - Number of function in documentaion(total) is bigger than total OPS!"
        )
    else:
        raise ValueError("programme not working! undefined error")
