


def read_file(filename):
    with open(filename) as f:
        while True:
            line = f.readline()

            if not line:
                f.close()
                break

            yield line



gen = read_file("data.txt")
next(gen)

raise ValueError

