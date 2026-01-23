import time

start_time = time.time()


def main():
    x = 2
    gess = x / 2
    for i in range(4):
        gess = (gess + (x / gess)) / 2
    print(gess)


for i in range(20000):
    main()
print("--- %s seconds ---" % (time.time() - start_time))
