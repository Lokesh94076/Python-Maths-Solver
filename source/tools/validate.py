import json
import os
from platform import freedesktop_os_release

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
    list(map(str.lower, total_OPS))
    list(map(str.lower, keys_list))
    total_OPS.sort()
    keys_list.sort()
    name_pass_list = []
    name_fail_list = []

    def name_test():
        n = 0
        for i in range(number_of_function):
            if total_OPS[n] == keys_list[n]:
                name_pass_list.append(f"Pass: {total_OPS[n]} = {keys_list[n]}")
                print(f"Pass: {total_OPS[n]} = {keys_list[n]}")

            else:
                name_fail_list.append(f"Fail: {total_OPS[n]} = {keys_list[n]}")
                print(f"Fail: {total_OPS[n]} = {keys_list[n]}")
            n += 1
        if number_of_function == len(name_pass_list):
            return True
        else:
            return False

    def number_test():
        if number_of_function == len(total_OPS):
            print("Pass - Number of functions with total OPS is correct!")
            return True
        elif number_of_function <= len(total_OPS):
            print(
                "Fail - Number of function in documentaion(total) is smaller than total OPS!"
            )
            return False
        elif number_of_function >= len(total_OPS):
            print(
                "Fail - Number of function in documentaion(total) is bigger than total OPS!"
            )
            return False
        else:
            raise ValueError("programme not working! undefined error")

    def print_result():
        if number_test():
            if name_test():
                print("\n\nPass!, all tests completed")
            else:
                print(
                    f"\n\nFail!, all or some tests are not completed  {name_fail_list}"
                )
        else:
            print("\n\nFail!, all or some tests are not completed")

    print_result()
