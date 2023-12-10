
file = open("input/tester.txt")
test = file.read()
import re
input_2 = test.lower()
container = input_2.split("\n")


def circle_scan(line, char_idx):
    pass
    # if line = 0:
    # elif line = len(input-1):
    # else:

    # line_up = line - 1
    # line_down = line + 1
    # right = char_idx+1
    # left = char_idx-1

def gondola(input):
    # regex_1 = [^\d.]
    engine_map = {}
    # print(input)
    
    for index, line in enumerate(input):
        tally = 0
        # pass
        # line_2 = line.replace([^a-zA-Z\d\s\.], "bar")
        auto_bings = re.sub("[^0-9a-zA-Z\.]", "BING", line)
        line_3 = re.split(r"[^0-9a-zA-Z$]", auto_bings)

        for idx, char in enumerate(line_3):
            print(char, idx)
            if char == '':
                continue
            elif char.isalnum():
                if len(char) == 1:
                    if line[index-1][char[idx]] == "BING" or line[index+1][char[idx]] == "BING":
                        tally += char
                    else:
                        continue
                elif len(char)>1:
                    length = len(char)+2
                    if line[index-1][char[idx]:length] == "BING" or line[index+1][char[idx]:length] == "BING":
                        tally += char
                    else:
                        continue
            else:
                length = len(char)+2
                line[index-1][char[idx]] ==
                print(char, idx)
                berb = "BLARGHH"
                print(berb)
        print(line_3)
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