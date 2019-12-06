def run_program():
    i = 0
    offset = i * 4
    program_instruction = programline[offset]
    while program_instruction != 99:
        if program_instruction == 1:
            programline[programline[offset + 3]] = programline[programline[offset + 1]] \
                                                   + programline[programline[offset + 2]]
        else:
            programline[programline[offset + 3]] = programline[programline[offset + 1]] \
                                                   * programline[programline[offset + 2]]
        i += 1
        offset = i * 4
        program_instruction = programline[offset]


with open("day_2.txt", "r") as filestream:
    for line in filestream:
        programline = list(map(int, line.split(",")))
        reference_program_line = programline[:]

for i in range(0, 99):
    for j in range(0, 99):
        programline[1] = i
        programline[2] = j
        run_program()
        if programline[0] == 19690720:
            print("i = ", i, ", j = ", j)
            break

        programline = reference_program_line[:]