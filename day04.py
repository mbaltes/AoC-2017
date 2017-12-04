# Day 04
# Passphrase checking quick and dirty

def get_data(fname):
    with open(fname) as f:
        return [line.strip().split() for line in f]


def passphrase_count_part1(data):
    sum = 0
    for line in data:
        seen = set()
        for elem in line:
            seen.add(elem)
        if len(seen) == len(line):
            sum += 1
    print(sum)


def passphrase_count_part2(data):
    sum = 0
    for line in data:
        seen = set()
        for elem in line:
            seen.add(''.join(sorted(elem)))  # No anagrams allowed.
        if len(seen) == len(line):
            sum += 1
    print(sum)


data = get_data('day04-input.txt')
passphrase_count_part1(data)
passphrase_count_part2(data)
