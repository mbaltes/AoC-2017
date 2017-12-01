# Day 01
# Reverse Captcha

def get_data(fname):
    with open(fname) as f:
        return f.read().rstrip()


def reverse_captcha(seq, part_two=False):
    offset = len(seq) // 2 if part_two else 1
    print(sum(int(value) for i, value in enumerate(seq)
              if seq[i] == seq[(i+offset) % len(seq)]))

data = get_data('day01-input.txt')
reverse_captcha(data, True)
