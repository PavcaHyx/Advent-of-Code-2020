from functools import reduce

from main import file_to_open


def get_all_answers():
    f = open(file_to_open("day6_input.txt"))
    all_answers_by_groups = f.read().split('\n\n')
    return all_answers_by_groups

def get_count_of_questions_with_answer_yes():
    all_answers_by_groups = get_all_answers()
    all_answers_by_groups_in_line = [group.replace('\n', '') for group in all_answers_by_groups]
    all_answers_count_in_set = list(set(group) for group in all_answers_by_groups_in_line)
    list_of_groups = []
    count = 0
    for item in all_answers_count_in_set:
        list_of_groups.append(list(item))
        count +=len(list(item))
    return count


def get_count_of_questions_to_which_everyone_answered_yes():
    all_answers_by_groups = get_all_answers()
    all_answers_in_lists = [group.split('\n') for group in all_answers_by_groups]
    count_of_yes = 0
    for my_list in all_answers_in_lists:
        if len(my_list) == 1:
            count_of_yes += len(my_list[0])

        else:
            intersect = list(reduce(set.intersection, [set(x) for x in my_list]))
            count_of_yes += len(intersect)

    return count_of_yes


if __name__ == '__main__':
    print(get_count_of_questions_to_which_everyone_answered_yes())



