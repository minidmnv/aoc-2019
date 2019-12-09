with open("day_5.txt", "r") as filestream:
    for line in filestream:
        program_instructions = list(map(int, line.split(",")))

index = 0
instruction = program_instructions[index]

while instruction != 99:
    digits = [int(d) for d in str(instruction)]
    index += 1
    if 2 < digits[-1] < 5:
        parameter = program_instructions[index]
        if instruction == 3:
            inp = int(input("Input: "))
            program_instructions[parameter] = inp
        else:
            output = program_instructions[parameter] if len(digits) < 3 or digits[-3] == 0 else parameter
            print(output)
        index += 1
    else:
        digits = [0] * (4 - len(digits)) + digits
        inst = digits[-1]
        parameters_mode = digits[:-2][::-1]
        parameters_count = 2 if 4 < inst < 7 else 3
        parameters = program_instructions[index:index + parameters_count]
        index += 2

a_value = program_instructions[parameters[0]] if parameters_mode[0] == 0 else parameters[0]
b_value = program_instructions[parameters[1]] if parameters_mode[1] == 0 else parameters[1]

index += 1
if inst == 1:
    program_instructions[parameters[2]] = a_value + b_value
elif inst == 2:
    program_instructions[parameters[2]] = a_value * b_value
elif inst == 5:
    index = b_value if a_value != 0 else index - 1
elif inst == 6:
    index = b_value if a_value == 0 else index - 1
elif inst == 7:
    program_instructions[parameters[2]] = 1 if a_value < b_value else 0
else:
    program_instructions[parameters[2]] = 1 if a_value == b_value else 0

instruction = program_instructions[index]