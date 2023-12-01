"""
    Example input
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
"""







def main():

    f_input = open("task_one_input.txt", "r")
    lines = f_input.readlines()

    final_count = 0

    for line in lines:

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
