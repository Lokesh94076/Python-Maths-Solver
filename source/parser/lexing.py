def whitespace(char):
    return char.isspace()


def number(input):
    return input.isdigit()


def operator(input):
    tokens = ["+", "*"]
    return input in tokens


def dot(input):
    if input != ".":
        return False
    else:
        return True


def lex(input_list):
    # print(f"before start - {input_list}")
    tokens = []
    i = 0
    while i < len(input_list):
        char = input_list[i]
        # print(f"char - {char}")
        if whitespace(char):
            i += 1
            continue
        if number(input_list[i]) or dot(input_list[i]):
            number_string = ""
            while i < len(input_list) and (number(input_list[i]) or dot(input_list[i])):
                number_string = number_string + (input_list[i])
                i += 1
            number_string = float(number_string)
            tokens.append(number_string)
            continue
        if operator(char):
            # print(f"op: {char}")
            i += 1
            tokens.append(str(char))
            continue
        else:
            raise ValueError()
    return tokens
