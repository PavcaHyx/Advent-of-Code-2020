from main import file_to_open


def day_2():
    f = open(file_to_open("day2_input.txt"))
    all_lines = f.read().split('\n')
    count_of_valid_passwords_first_condition = 0
    count_of_valid_passwords_second_condition = 0
    for line in all_lines:
        particular_items = line.split()
        character = particular_items[1].replace(":", "")
        password = particular_items[2]
        my_range = particular_items[0].split("-")
        for i in range(int(my_range[0]), int(my_range[1])+1):
            if i == password.count(character):
                count_of_valid_passwords_first_condition += 1

        if int(my_range[1]) <= len(password):
            if (password[int(my_range[0]) - 1] == character or password[int(my_range[1]) - 1] == character) \
                    and not (password[int(my_range[0]) - 1] == character and password[int(my_range[1]) - 1] == character):
                count_of_valid_passwords_second_condition += 1

    return count_of_valid_passwords_first_condition, count_of_valid_passwords_second_condition


if __name__ == '__main__':
    print(day_2())