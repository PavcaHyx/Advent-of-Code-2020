from main import file_to_open


def day_3():
    f = open(file_to_open("day3_input.txt"))
    all_lines = f.read().split('\n')
    all_lines_in_play = all_lines[1:]
    count_of_trees = 0
    start_position = 3
    step = 3
    lenght_of_line = len(all_lines[0])
    for i, line in enumerate(all_lines_in_play):
        new_position = start_position + i*step
        position = new_position % lenght_of_line
        if line[position] == '#':
            count_of_trees += 1
    return count_of_trees


def day_3_part_2():
    f = open(file_to_open("day3_input.txt"))
    all_lines = f.read().split('\n')
    lenght_of_line = len(all_lines[0])
    list_of_coordinates = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    results = []
    result = 1
    for run_number, coordinate in enumerate(list_of_coordinates, 1):
        count_of_trees = 0
        step_column = coordinate[0]
        step_line = coordinate[1]
        position_line = 0

        for i in range(len(all_lines)-step_line):
            new_position_column = step_column + i * step_column
            position_column = new_position_column % lenght_of_line
            position_line += step_line
            try:
                if all_lines[position_line][position_column] == '#':
                    count_of_trees += 1
            except:
                pass

        results.append([run_number, count_of_trees])
        result *= count_of_trees
    return results, result


if __name__ == '__main__':
    print(day_3_part_2())