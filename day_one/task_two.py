"""
    Example input
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
"""



def convert_string( in_string : str):

    possible_inputs = ["one","two","three","four","five", "six", "seven", "eight", "nine"]

    
    number_locations = {}

    for pi in possible_inputs:

        first_occurence = in_string.find(pi)
        last_occurence = in_string.rfind(pi)

        if( first_occurence < 0 and last_occurence < 0 ) :
            continue

        number_locations[pi] = (first_occurence, last_occurence)

    if len(number_locations) == 0:
        return in_string


    min_key = ""
    max_key = ""
    min_num_loc = None
    max_num_loc = None
    min_num = None
    max_num = None

    for key, values in number_locations.items():
        min_value = min(values)
        max_value = max(values)

        if min_num_loc is None:
            min_num_loc = min_value
            min_key = key
        elif min_value < min_num_loc:
            min_num_loc = min_value
            min_key = key

        if max_num_loc is None:
            max_num_loc = max_value
            max_key = key
        elif max_value > max_num_loc:
            max_num_loc = max_value
            max_key = key

    for i in range(0,len(possible_inputs)):
        if min_key == possible_inputs[i]:
            min_num = i + 1

        if max_key == possible_inputs[i]:
            max_num = i + 1


    if min_num_loc == max_num_loc:
        out_string = in_string[:min_num_loc] + str(min_num) + in_string[min_num_loc+len(min_key):]
    else:
        out_string = in_string[:min_num_loc] + str(min_num) + in_string[min_num_loc+len(min_key):max_num_loc] + str(max_num) + in_string[max_num_loc+len(max_key):]



    return out_string






def main():

    f_input = open("input.txt", "r")
    lines = f_input.readlines()

    final_count = 0

    for line in lines:

        line = convert_string(line)

        first_number = None
        second_number = None
        line_number = 0

        for i in range(0,len(line)):
            j = len(line) - 1 - i
            
            if line[i].isnumeric() and first_number is None:
                first_number = line[i]

            if line[j].isnumeric() and second_number is None:
                second_number = line[j]
        
            if first_number is not None and second_number is not None:
                break

        if first_number is not None and second_number is not None:
            line_number = first_number + second_number
        elif first_number is not None:
            line_number = first_number
        elif second_number is not None:
            line_number = second_number

        final_count += int(line_number)

    print(final_count)

        





if __name__ == "__main__":
    main()
