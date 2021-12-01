from math import floor

from main import file_to_open


def get_all_codes():
    f = open(file_to_open("day5_input.txt"))
    all_codes = f.read().split('\n')
    return all_codes


def day_5():
    codes = get_all_codes()
    all_seats = [int((code.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')), 2) for code in codes]
    your_seat = [s for s in range(min(all_seats), max(all_seats)) if s not in all_seats][0]

    return print(f"Part 1: Highest seat is {max(all_seats)}"), print(f"Part 2: Your seat is {your_seat}")


if __name__ == '__main__':
    print(day_5())