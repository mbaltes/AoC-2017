# Day 02
# Checksum sum



def get_data(fname):
    with open(fname) as f:
        return [list(map(int, line.strip().split())) for line in f]


def divide_even(line):
    for i in range(len(line)):
        for j in range(len(line)):
            if i != j and int(line[i]) % int(line[j]) == 0:
                return int(line[i]) // int(line[j])


def checksum_sum(data):
    print(sum(max(line) - min(line) for line in data))


def division_sum(data):
    print(sum(divide_even(line) for line in data))


data = get_data('day02-input.txt')
checksum_sum(data)
division_sum(data)
