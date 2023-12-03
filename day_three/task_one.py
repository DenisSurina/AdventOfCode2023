

def check_location(sch,i,j):

    try:
        if sch[i][j] != "." and not sch[i][j].isnumeric():
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

    for i in range(0,len(schematic)):

        for j in range(0, len(schematic[i])):

            ch = schematic[i][j]

            if ch.isnumeric():
                print(ch)
                print(is_positive)
                
                num_string += ch

                if check_location(schematic,i-1,j-1):
                    is_positive = True
                if check_location(schematic,i-1,j):
                    is_positive = True
                if check_location(schematic,i-1,j+1):
                    is_positive = True
                if check_location(schematic,i,j-1):
                    is_positive = True
                if check_location(schematic,i,j+1):
                    is_positive = True
                if check_location(schematic,i+1,j-1):
                    is_positive = True
                if check_location(schematic,i+1,j):
                    is_positive = True
                if check_location(schematic,i+1,j+1):
                    is_positive = True



            else:
                if is_positive:
                    sum_total += int(num_string)

                num_string = ""
                is_positive = False


 


    print(sum_total)







if __name__ == "__main__":
    main()
