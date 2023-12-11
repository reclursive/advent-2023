
# file = open("input/tester.txt")
# test = file.read()
# import re
# input_2 = test.lower()
# container = input_2.split("\n")


# def circle_scan(line, char_idx):
#     pass
#     # if line = 0:
#     # elif line = len(input-1):
#     # else:

#     # line_up = line - 1
#     # line_down = line + 1
#     # right = char_idx+1
#     # left = char_idx-1

# def gondola(input):
#     # regex_1 = [^\d.]
#     engine_map = {}
#     # print(input)
#     tally = 0
    
#     for index, line in enumerate(input):
#         # pass
#         # line_2 = line.replace([^a-zA-Z\d\s\.], "bar")
#         auto_bings = re.sub("[^0-9a-zA-Z\.]", "BING", line)
#         line_3 = re.split(r"[^0-9a-zA-Z$]", auto_bings)

#         print(len(line_3), "LINEs")

#         for idx, char in enumerate(line_3):
#             print(char, idx)
#             if char == '':
#                 continue
#             elif char.isalnum():
#                 if len(char) == 1:
#                     if line[index-1][idx] == "BING" or line[index+1][idx] == "BING":
#                         tally += char
#                     else:
#                         continue
#                 elif len(char)>2 and idx> 0 and index>1:
#                     diag_FF = idx +len(char)
#                     diag_RW = idx -1 
#                     if line[index-1][diag_FF] == "BING" or line[index+1][diag_RW] == "BING" or line[index+1][diag_FF] == "BING" or line[index-1][diag_RW] == "BING" or line[index-1][diag_FF] =="BING":
#                         tally += char
#                     else:
#                         splitty = char.split("BING")
#                         print(splitty)
#                         print(char, "CLEAR NUMB")

#             else:
#                 splitty = char[idx].split("BING")
#                 print(splitty, "splitty")
#         print(tally, "tally")
#         # print(line_3)
#         # print(line_2, index)
#         # for idx, char in enumerate(line_3):
#         #     # print(char, idx)
#         #     if char.isdigit():
#         #         print(char)
#         #         # num_len = len(line[index])
#         #         print("digit", index)
#         #     else:
#         #         print("empty", index)
#         # print(index, line)
#         # for index, char in enumerate(line):
#         #     print(index, char)

# gondola(container)


file = open("input/tester.txt")
test = file.read()
import re
input_2 = test.lower()
container = input_2.split("\n")


def circle_scan(array, index):
    if len(array) == 2 and array[0].isdigit() or array[1].isdigit():
        tally += int(array[0] or 0)
        tally += int(array[1] or 0)
    elif array == ["", ""]:
        dict["BING"] = tuple(index)
    elif len(array) == 1 and array[0].isdigit():
        dict[array[0]] == tuple(index)


def gondola(input):
    # regex_1 = [^\d.]
    engine_map = {}
    # print(input)
    tally = 0
    
    for index, line in enumerate(input):
        # pass
        # line_2 = line.replace([^a-zA-Z\d\s\.], "bar")
        auto_bings = re.sub("[^0-9a-zA-Z\.]", "BING", line)
        line_3 = re.split(r"[^0-9a-zA-Z$]", auto_bings)

        print(len(line_3), "LINEs")

        for idx, char in enumerate(line_3):
            print(char, idx)
            if char == '':
                continue
            elif char is not char.isalnum():
                part_nums = re.split("BING", char)
                print(part_nums, "PN")
                circle_scan(part_nums, idx)

                

        print(tally, "tally")
        # print(line_3)
        # print(line_2, index)
        # for idx, char in enumerate(line_3):
        #     # print(char, idx)
        #     if char.isdigit():
        #         print(char)
        #         # num_len = len(line[index])
        #         print("digit", index)
        #     else:
        #         print("empty", index)
        # print(index, line)
        # for index, char in enumerate(line):
        #     print(index, char)



            

gondola(container)