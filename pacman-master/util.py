def convert_maze_to_binary_array(maze):
    binary_array = []
    for row in range(len(maze)):
        binary_row = []
        characters_list = [x for x in maze[row]]
        for character in characters_list:
            if character == "X":
                binary_row.append(1)
            else:
                binary_row.append(0)
        binary_array.append(binary_row)
    return binary_array


def reverse_tuples(tuples_list):
    reversed_tuples_list = []
    for tup in tuples_list:
        reversed_tuple = tup[::-1]
        reversed_tuples_list.append(reversed_tuple)
    return reversed_tuples_list
