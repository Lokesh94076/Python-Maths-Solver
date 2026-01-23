import os
import random as random
import time


def generate_random(a, b):
    return random.randint(a, b)


def generate_random_ninp():
    i_num = 22000
    i_num = i_num + generate_random(-1000, 1000)
    start_time = time.time()

    def main():
        x = 2
        gess = x / 2
        for i in range(4):
            gess = (gess + (x / gess)) / 2

    for i in range(i_num):
        main()
    timee = time.time() - start_time
    string_without_decimal = str((timee / random.random())).replace(".", "")
    string_without_decimal = int(string_without_decimal)
    return string_without_decimal


# doc - done
