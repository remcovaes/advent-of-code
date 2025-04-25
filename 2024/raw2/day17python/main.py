from typing import List, Tuple
from math import trunc, pow
from functools import lru_cache
Coor = Tuple[int, int]

def up(s: Coor):
    return (s[0]-1, s[1])
def down(s: Coor):
    return (s[0]+1, s[1])
def left(s: Coor):
    return (s[0], s[1]-1)
def right(s: Coor):
    return (s[0], s[1]+1)



def read_file():
    with open("input") as f:
        return f.read()

class SingleInput:
    operation: int
    literal: int

class MainInput:
    lines: List[SingleInput]
    a: int
    b: int
    c: int
    operation: int
    output: str

def parse_single(a: str, b: str) -> SingleInput:
    single_input = SingleInput()
    single_input.operation= int(a)
    single_input.literal = int(b)
    return single_input


def parse_input(s: str) -> MainInput:
    main = MainInput()
    main.lines = []
    splitted = s.split("\n\n")
    regs = splitted[0].split("\n")
    formatted = []
    for i in regs:
        formatted.append(int(i.split(": ")[1]))
    
    main.a = formatted[0]
    main.b = formatted[1]
    main.c = formatted[2]
    main.output = ""
    main.operation = 0

    ops = splitted[1].split(":")[1].strip(" ").split(",")
    for i in range(0, len(ops), 2):
        main.lines.append(parse_single(ops[i], ops[i+1]))
    return main

input_glob = parse_input(read_file())
def get_next(input: Tuple[int, int, int]):
    a = input[0]
    b = input[1]
    c = input[2]
    
    output = ""
    end = False
    for curop in input_glob.lines:
        single = curop
        operand = single.literal
        if operand == 4:
            operand = a
        elif operand == 5:
            operand = b
        elif operand == 6:
            operand = c

        if single.operation == 0:
            a = trunc(a / pow(2,operand))
        if single.operation == 1:
            result = single.literal ^ b
            b = result
        if single.operation == 2:
            b = operand % 8
        if single.operation == 3:
            if a == 0:
                end = True
        if single.operation == 4:
            b = b ^ c
        if single.operation == 5:
            output = output + str(operand % 8)
        if single.operation == 6:
            b = trunc(a / pow(2,operand))
        if single.operation == 7:
            c = trunc(a / pow(2,operand))

    return end, output, (a,b,c)

def process_single1(main: MainInput) -> int:
    single = main.lines[main.operation]
    operand = single.literal
    if operand == 4:
        operand = main.a
    elif operand == 5:
        operand = main.b
    elif operand == 6:
        operand = main.c

    if single.operation == 0:
        main.a = trunc(main.a / pow(2,operand))
    if single.operation == 1:
        result = single.literal ^ main.b
        main.b = result
    if single.operation == 2:
        main.b = operand % 8
    if single.operation == 3:
        if main.a != 0:
            main.operation = int(single.literal / 2)
            return process_single1(main)
    if single.operation == 4:
        main.b = main.b ^ main.c
    if single.operation == 5:
        main.output = main.output + str(operand % 8)
    if single.operation == 6:
        main.b = trunc(main.a / pow(2,operand))
    if single.operation == 7:
        main.c = trunc(main.a / pow(2,operand))


    total_lines = len(main.lines)
    main.operation = main.operation + 1
    if main.operation == total_lines:
        return 0

    return process_single1(main)


def reverse_engineer(main: MainInput, num1: int, num2: int, num3: int):
    single = main.lines[main.operation]
    operand = single.literal
    if operand == 4:
        operand = main.a
    elif operand == 5:
        operand = main.b
    elif operand == 6:
        operand = main.c

    if single.operation == 0:
        # Done
        # might be some fractional value
        main.a = trunc(main.a * 2 ** operand) + num1
    if single.operation == 1:
        # done
        result = single.literal ^ main.b
        main.b = result
    if single.operation == 2:
        #done
        main.a = main.b + 8 * num2
    if single.operation == 3:
        pass
    if single.operation == 4:
        #done
        main.b = main.b ^ main.c
    if single.operation == 5:
        # Done
        main.output = main.output + str(operand % 8)
    if single.operation == 7:
        # Done
        main.c = trunc(main.a * 8) + num3



def process_single2(single: SingleInput) -> int:
    total = 0
    return total

def solve_total_1():
    file = read_file()
    target = "2412754113550330"
    return solver_part1(file, target)

def solve_total_2():
    file = read_file()

    return solver_part2(file)
def solver_part1(s: str, target: str):
    total = 500000000000
    step =  100000000000
    prev_match = 0
    while True:
        main = parse_input(s)
        main.a = total
        process_single1(main)
        print(total)
        matches = 0
        j = 0
        for k in range(len(target)):
            if j >= len(main.output):
                break
            tar = target[-k -1]
            res = main.output[-j -1]
            if tar == res:
                matches+=1
            else:
                break
            j+=1
        # if prev_match > matches:
        #     inc = (step // 10 ** matches)
        #     total = (total - (step // 10 ** prev_match)) + inc
        #     if inc == 0:
        #         prev_match = 0
        #     continue
        prev_match = matches
        print(len(main.output), matches, main.output)
        inc = step // 10 ** matches
        if target == main.output:
            print("win")
            print(total)
            break
        total = total + (inc if inc != 0 else 1)
        if len(main.output) > 25:
            break

    # i = 0
    # prev = 0
    # unique = {}
    # total = 0
    # step =  1
    # diffs = []
    # for i in range(1024):
    #     main = parse_input(s)
    #     main.a = total
    #     process_single1(main)
    #     m = unique.get(main.output)
    #     if m == None:
    #         m = set()
    #         unique[main.output] = m
    #     m.add(total)
    #
    #     diffs.append((int(main.output) - int(prev), i))
    #     prev = main.output
    #     total+=step
    #
    # diffs2 = []
    # for i in range(1024):
    #     main = parse_input(s)
    #     main.a = total
    #     process_single1(main)
    #     m = unique.get(main.output)
    #     if m == None:
    #         m = set()
    #         unique[main.output] = m
    #     m.add(total)
    #
    #     diffs2.append((int(main.output) - int(prev), i))
    #     prev = main.output
    #     total+=step
    #
    # ops = []
    # for i in range(len(diffs)):
    #     if diffs[i][0] != diffs2[i][0]:
    #         ops.append(i)
    #     else:
    #         ops.append(False)
    #
    #
    # current_result: int = 0
    # main = parse_input(s)
    # main.a = 0
    # process_single1(main)
    # current_result = int(main.output)
    #
    # for i in range(1,100000000):
    #     curropp = i % 1024
    #     print(i, curropp)
    #     if ops[curropp] != False:
    #         op = ops[curropp]
    #         current_result = current_result + op
    #         main = parse_input(s)
    #         main.a = i
    #         process_single1(main)
    #         check = int(main.output)
    #         if check != current_result:
    #             print(check, current_result, op)
    #             break
    #         continue
    #     main = parse_input(s)
    #     main.a = i
    #     process_single1(main)
    #     current_result = int(main.output)
    #
    #

    

    # main = parse_input(s)
    # main.operation = len(main.lines) - 1
    # while main.operation > 0:
    #     reverse_engineer(main, 0)
    #     main.operation = main.operation - 1
    # print(main.a)
    # main.operation = main.operation - 1
    # if main.operation != 0:
    #     return reverse_engineer(main, 0)
    # else:
    #     return 0   

        # i = 297770083000000
    #
    # m = 1
    # decs = []
    # j = i
    # prev = False
    # while True:
    #     j += m
    #     end, output, nums = get_next((j, input.b, input.c))
    #     result = output
    #     while not end:
    #         end, output, nums = get_next(nums)
    #         result = result + output
    #     if int(result) == int(target):
    #         print(j)
    #     if int(result) < int(target):
    #         print(j)
    #     if int(result) >= int(target) and prev:
    #         print(j)
    #     prev = result[-10:] == target[-10:]
    #     previ = j
    #     if prev:
    #         print(j)
    #     if int(result) > int(target):
    #         print(j)
    #
    #     if m == 0:
    #         break
        # if int(result) > int(target):
        #     decs.append(i - m)
        #     i = i - m
        #     m = m // 10
        #     continue
        #
        # i+=m

# def solver_part1(s: str, target: str):
#     input = parse_input(s)
#     result = ""
#     i = 10
#     m = 10
#     # target = "2412754113550330"
#     correct = []
#     multi = 10
#     while True:
#         end, output, nums = get_next((i, input.b, input.c))
#         result = output
#         while not end:
#             end, output, nums = get_next(nums)
#             result = result + output
#         print(i)
#         if len(correct) > 0 and result[len(result) - len(correct) :] != target[len(target) - len(correct) :]:
#             while len(correct) > 0 and result[len(result) - len(correct) :] != target[len(target) - len(correct) :]:
#                 wrong = correct.pop()
#                 m = wrong[1]
#                 i = wrong[0] * wrong[1] + wrong[1]
#                 continue
#             continue
#         if result == target:
#             print("wint")
#         if len(correct) == len(result):
#             i+=1
#             continue
#
#         length_to_check = -len(correct) - 1
#         if length_to_check + len(result) < 0 or length_to_check + len(target) < 0:
#             print("oops")
#         else:
#             resulPart = result[length_to_check]
#             targetPArt = target[length_to_check]
#             if resulPart == targetPArt:
#                 correct.append((i//m, m))
#                 if m != 1:
#                     m = m // 10 
#                 continue
#
#
#
#         i+=m
#         if len(correct) > 0:
#             temp = correct[-1][1]
#             if i >= (correct[-1][0] * temp + temp):
#                 correct.pop()
#                 m = m * 10
#
#         if len(correct) > 0:
#             continue
#         if i >= m * 10:
#             m = m * 10

# def solver_part1(s: str):
#     input = parse_input(s)
#     result = ""
#     i = 581582213878
#     multiplier = 1000000000
#     target = "2412754113550330"
#     map = {}
#     while True:
#         end, output, nums = get_next((i, input.b, input.c))
#         result = output
#         while not end:
#             end, output, nums = get_next(nums)
#             result = result + output
#         l = len(result)
#         curr = -len(map) -1
#         if len(map)!= 0:
#             correctPartREsult = result[len(result)  - len(map):]
#             correctTarger = target[len(target) -  len(map):]
#             if  (correctPartREsult != correctTarger and len(map) != 0):
#                 last_correct = map[len(map) -1 ]
#                 print (i, result)
#                 if multiplier == 1:
#                     multiplier = 10
#                     i = last_correct + 1
#                     continue
#                 multiplier = multiplier * 10
#                 i = last_correct * (multiplier) + multiplier
#                 del map[len(map) - 1]
#                 continue
#             if correctTarger == correctPartREsult and multiplier == 1:
#                 map[len(map) -1 ] = i
#             if l + curr < 0:
#                 print("panmioc")
#             if len(map) >= 2:
#                 prev= map[len(map) -1]
#                 prevprev = map[len(map) -2]
#                 if prev > (prevprev * 10 + 10):
#                     last_correct = prevprev
#                     multiplier = multiplier * 10 * 10
#                     i = last_correct * (multiplier) + multiplier
#                     del map[len(map) - 1]
#                     continue
#
#         if result[curr] == target[curr]:
#             prev = map.get(len(map) -1)
#             if prev != i:
#                 map[len(map)] = i//multiplier
#                 multiplier = int(multiplier / 10)
#             if multiplier == 0:
#                 multiplier =1
#             if result == target:
#                 print (i, result)
#                 return result
#
#         i += multiplier
#         if len(map) == 0:
#             if i // multiplier == 10:
#                 multiplier = multiplier * 10
#

def solver_part2(s: str):
    input = parse_input(s)
    input.a = 2412754113550330
    input.operation = len(input.lines) - 1
    # reverse_engineer(input)

if __name__ == "__main__":
    solve_total_1()
