import json

with open("F:\\Math Engine\\source\\solvers\\database\\lookup.json", "r") as f:
    operations = json.load(f)


def function_recognise(listed_data):
    equation = 0
    op_id = 0
    function = str(listed_data[0])
    if function in operations:
        op_id = operations[function]["id"]
        equation = operations[function]["eq"]
    else:
        print("Operation not found !initial.py")

    no_of_inputs = len(listed_data)
    return equation, op_id
