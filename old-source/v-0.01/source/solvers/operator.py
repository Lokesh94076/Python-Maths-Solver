from . import distributor as distributor
from . import initial as initial


# categories
def simple(*data):
    listed_data = list(data)
    inputs = data[1:]
    type, id = initial.function_recognise(listed_data)
    answer = distributor.distrubute(type, id, inputs)
    print(answer)


def complex(*data):
    inputs = no_inputs(*data)
    initial.data_cleapup(inputs, *data)
