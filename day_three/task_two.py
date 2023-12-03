

def check_location(sch,i,j):

    try:
        if sch[i][j] == "*": 
            return True

    except Exception as e:
        return False

    return False




def main():

    file_input = open("input.txt","r")

    lines = file_input.readlines()

    schematic = []

    for line in lines:

        line_list = []
        for i in range(0,len(lines)):
            line_list.append(line[i])

        schematic.append(line_list)


    sum_total = 0
    num_string = ""
    is_positive = False
    gear_i = None
    gear_j = None
    gear_dict = {}

    for i in range(0,len(schematic)):

        for j in range(0, len(schematic[i])):

            ch = schematic[i][j]

            if ch.isnumeric():
                
                num_string += ch

                if check_location(schematic,i-1,j-1):
                    gear_i = i-1
                    gear_j = j-1
                    is_positive = True
                if check_location(schematic,i-1,j):
                    gear_i = i-1
                    gear_j = j
                    is_positive = True
                if check_location(schematic,i-1,j+1):
                    gear_i = i-1
                    gear_j = j+1
                    is_positive = True
                if check_location(schematic,i,j-1):
                    gear_i = i
                    gear_j = j-1
                    is_positive = True
                if check_location(schematic,i,j+1):
                    gear_i = i
                    gear_j = j+1
                    is_positive = True
                if check_location(schematic,i+1,j-1):
                    gear_i = i+1
                    gear_j = j-1
                    is_positive = True
                if check_location(schematic,i+1,j):
                    gear_i = i+1
                    gear_j = j
                    is_positive = True
                if check_location(schematic,i+1,j+1):
                    gear_i = i+1
                    gear_j = j+1
                    is_positive = True



            else:
                if is_positive:
                    gear_loc = (gear_i,gear_j)

                    if gear_loc in gear_dict:
                        gear_dict[gear_loc] = (gear_dict[gear_loc],int(num_string))
                    else:
                        gear_dict[gear_loc] = int(num_string)

                num_string = ""
                is_positive = False


 



    total_sum = 0
    for gear in gear_dict:

        gear_val = gear_dict[gear]
        if type(gear_val) is tuple:

            mul = gear_val[0] * gear_val[1]
            total_sum += mul


    print(total_sum)







if __name__ == "__main__":
    main()
