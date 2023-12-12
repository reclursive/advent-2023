file = open("input/tester.txt")
test = file.read()
import re
input_2 = test.lower()
container = input_2.split("\n")
engine_map = {}
tally = 0
bing_count = 0

def fast_filt(pair):
    key, value = pair
    if "B" in key:
        return True
    else:
        return False 

def compare_remaining(remain_dict):
    global tally
    bingo = dict(filter(fast_filt, remain_dict.items()))
    print(bingo)
    for key,value in remain_dict.items():
        if key.isnumeric():
            length = len(key) +2
            upper_diag = (value[0]-1, value[1]-1) or (value[0]-1, [i for i in range(value[1], value[1]+length)])
            lower_diag =(value[0]+1, value[1]-1) or (value[0]+1, [i for i in range(value[1], value[1]+length)])
            print(key, value)
            if lower_diag in bingo.values() or upper_diag in bingo.values():
                tally += int(key)
                print("HITTT", key)
                continue

def circle_scan(array, x, y):
    global tally
    global bing_count
    
    if len(array) == 2:
        if array[0].isdigit() and array[1].isdigit():
            tally += int(array[0]) +int(array[1])
            array = ' '.join(array)
            tally += int(array[0]) + int(array[1])
        else:
            bing_count += 1
            engine_map["B"+str(bing_count)] = (x, y)
    elif len(array) == 1 and array[0].isdigit():
        num = array[0]
        engine_map[num] = (x, y)

    return compare_remaining(engine_map)

def gondola(input):
    for index, line in enumerate(input):
        auto_bings = re.sub("[^0-9a-zA-Z\.]", "B", line)
        line_3 = re.split(r"[^0-9a-zA-Z$]", auto_bings)
        for idx, char in enumerate(line_3):
            print(idx, index, char, "MEEP")
            if char == '':
                continue
            elif char is not char.isalnum():
                print("SPLITTY", char)
                part_nums = re.split("B", char)
                print(part_nums, "PN")
                circle_scan(part_nums, index, idx)
   
gondola(container)