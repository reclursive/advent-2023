file = open("input/no_3.txt")
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
    for key,value in remain_dict.items():
        length = len(key) +1
        upper = value[0]-1
        lower = value[0]+1
        right = [i for i in range(value[1], value[1]+length)]
        left = value[1]-1
        upper_diag = (upper, right) 
        upper_left = (upper, left)
        lower_diag = (lower, right)
        lower_left = (lower, left)
        if "m" in key:
            dup = key.split("m")[0]
            tally += int(dup[0])
        elif key.isnumeric():
            if lower_diag in bingo.values() or upper_diag in bingo.values() or upper_left in bingo.values() or lower_left in bingo.values():
                tally += int(key) 
                continue
            else:
                continue
        elif key[0] is not 'B':
            if lower_diag in bingo.values() or upper_diag in bingo.values() or upper_left in bingo.values() or lower_left in bingo.values():
                dup = int(key.split("m")[0])
                tally += dup
                continue


    return remain_dict, tally



def circle_scan(array, x, y):
    global engine_map
    global tally
    global bing_count
    if array[0] == 'B':
        bing_count += 1
        engine_map["B"+str(bing_count)] = (x, y)
    if len(array) == 2:
        if array[0].isdigit() and array[1].isdigit():
            tally += int(array[0]) +int(array[1])
        elif array[1].isnumeric():
            tally += int(array[1])
    elif len(array) == 1 and array[0].isnumeric():
        if array[0] in engine_map.keys():
            dif = "m"+ str(y+x)
            engine_map[array[0] + dif] = (x, y)
        else:
            engine_map[array[0]] = (x, y)
    return engine_map

def gondola(input):
    global engine_map
    global tally
    for index, line in enumerate(input):
        auto_bings = re.sub("[^0-9a-zA-Z\.]", "B", line)
        line_3 = re.split(r"[^0-9a-zA-Z]", auto_bings)
        for idx, char in enumerate(line_3):
            if char == '':
                continue
            elif len(char)>1 and char[0] == 'B':
                part_numsB = char.split("B")
                engine = circle_scan(part_numsB, index, idx)
            elif char == 'B':
                part_numsC = ['B']
                engine = circle_scan(part_numsC, index, idx)
            elif char is not char.isalnum():
                part_numsN = re.split("B", char)
                engine = circle_scan(part_numsN, index, idx)
            else:
                continue
    return compare_remaining(engine)
   
print(gondola(container))

