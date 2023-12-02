import re



possible_colors = ["red", "green", "blue"]



def return_numbers_from(string):

    numbers_list = [int(s) for s in re.findall(r'\b\d+\b', string)
]
    return numbers_list

def return_color_from(string):
    
    for cl in possible_colors:

        rc = string.find(cl)

        if rc > 0:
            return cl



def possible(line):

    first_split = line.split(":")

    game = first_split[0]
    game_id = return_numbers_from(game)[0]

    sets = first_split[1].split(";")

    game_is_possible = True
    cubes_dict = {}

    for st in sets:
        values = st.split(",")

        for value in values:

            cube_value = int( return_numbers_from(value)[0] )
            cube_key = return_color_from(value)

            if cube_key not in cubes_dict:
                cubes_dict[cube_key] = cube_value
            elif cube_value > cubes_dict[cube_key]:
                cubes_dict[cube_key] = cube_value

    
    cubes_power = None
    for key in cubes_dict.keys():

        if cubes_power is None:
            cubes_power = cubes_dict[key]
        else:
            cubes_power *= cubes_dict[key]

    return cubes_power





def main():

    input_file = open("input.txt","r")


    lines = input_file.readlines()

    sum_of_id = 0

    for line in lines:

        game_id = possible(line)

        if game_id > 0:
            sum_of_id += game_id


    print(sum_of_id)


if __name__ == "__main__":
    main()
