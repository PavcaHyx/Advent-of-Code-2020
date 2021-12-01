from main import file_to_open


def day_1_part_1():
    f = open(file_to_open("day1_input.txt"))
    all_numbers = f.read().split('\n')
    while all_numbers:
        first_number = all_numbers.pop(0)
        for number in all_numbers:
            if (int(first_number) + int(number)) == 2020:
                return (f'Sum of these two numbers: {first_number}, {number} is 2020.'
                        f' \n Required result is {first_number} * {number} = {str(int(first_number)*int(number))}')


def day_1_part_2():
    f = open(file_to_open("day1_input.txt"))
    all_numbers = f.read().split('\n')
    for num_1 in all_numbers:
        for num_2 in all_numbers:
            for num_3 in all_numbers:
                if int(num_1) + int(num_2) + int(num_3) ==2020:
                    return (f'Sum of these two numbers: {num_1}, {num_2}, {num_3} is 2020.'
                            f'\n Required result is {num_1} * {num_2} * {num_3} = {str(int(num_1)*int(num_2)*int(num_3))}')


if __name__ == '__main__':
    print(day_1_part_2())