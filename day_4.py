from main import file_to_open


def get_all_passports():
    f = open(file_to_open("day4_input.txt"))
    all_passports = f.read().split('\n\n')
    passports_info_in_line = [passport_info.replace('\n', ' ') for passport_info in all_passports]
    passports_info_separeted_to_items = [passport.split() for passport in passports_info_in_line]
    passports_info_in_dict = [convert_to_dictionary(passport) for passport in passports_info_separeted_to_items]
    return passports_info_in_dict


def convert_to_dictionary(password_list):
    dictionary = {}

    for item in password_list:
        item_parts = item.split(":")
        key = item_parts[0]
        value = item_parts[1]
        dictionary[key] = value

    return dictionary


def is_valid_passport(passport):
    has_birth_year = "byr" in passport
    has_issue_year = "iyr" in passport
    has_expiration_year = "eyr" in passport
    has_height = "hgt" in passport
    has_hair_color = "hcl" in passport
    has_eye_color = "ecl" in passport
    has_passport_id = "pid" in passport
    has_country_id = "cid" in passport

    return (
        has_birth_year and
        has_issue_year and
        has_expiration_year and
        has_height and
        has_hair_color and
        has_eye_color and
        has_passport_id
    )


def has_valid_year(passport):
    return 1920 <= int(passport["byr"]) <= 2002


def has_valid_expiration_year(passport):
    return 2020 <= int(passport["eyr"]) <= 2030


def has_valid_issue_year(passport):
    return 2010 <= int(passport["iyr"]) <= 2020


def has_valid_height(passport):
    has_valid_height = False
    height_units = passport["hgt"][-2:]
    if height_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_height = 150 <= height <= 193
    elif height_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_height = 59 <= height <= 76
    return has_valid_height


def has_valid_eye_color(passport):
    return passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_hex_string(string):
    string.lower()
    is_valid = True

    for character in string:
        if character not in "0123456789abcdef":
            is_valid = False
            break

    return is_valid


def has_valid_hair_color(passport):
    hair_color = passport["hcl"]
    has_valid_hair_color = False
    if len(hair_color) == 7:
        digits = hair_color[1:]
        has_valid_hair_color = is_valid_hex_string(digits)
    return has_valid_hair_color


def has_valid_passport_id(passport):
    is_valid = False
    pid = passport["pid"]

    if len(pid) == 9:
        is_valid = True

        for character in pid:
            if character not in "0123456789":
                is_valid = False
                break

    return is_valid


def has_valid_values(passport):
    valid_birth_year = has_valid_year(passport)
    valid_issue_year = has_valid_issue_year(passport)
    valid_expiration_year = has_valid_expiration_year(passport)
    valid_height = has_valid_height(passport)
    valid_hair_color = has_valid_hair_color(passport)
    valid_eye_color = has_valid_eye_color(passport)
    valid_passport_id = has_valid_passport_id(passport)

    return (
            valid_birth_year and
            valid_issue_year and
            valid_expiration_year and
            valid_height and
            valid_hair_color and
            valid_eye_color and
            valid_passport_id
    )


def day_4_part_1():
    all_passports = get_all_passports()
    valid_passwords = []
    for passport in all_passports:
        if is_valid_passport(passport):
            valid_passwords.append(passport)
    return valid_passwords, len(valid_passwords)


def day_4_part_2():
    valid_passports = day_4_part_1()[0]
    truly_valid_passports = []
    for passport in valid_passports:
        if has_valid_values(passport):
            truly_valid_passports.append(passport)
    return truly_valid_passports, len(truly_valid_passports)


if __name__ == '__main__':
    print(day_4_part_2())