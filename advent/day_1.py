file = open("input/no_1.txt")
test = file.read()

def trebuchet(input):
    container = input.split("\n")

    dict = {}
    no_calib = 0

    if len(container) >= 1:
        for string in container:
            num_string = list(filter(str.isdigit, string))
            key = string
            if len(num_string) < 1:
                no_calib +=1
            elif len(num_string) ==1:
                combo = int(num_string[0]+num_string[0])
                dict[key] = combo
            else:
                end = len(num_string)-1
                combo_2 = int(num_string[0]+num_string[end])
                dict[key] = combo_2
                

    return sum(dict.values())

trebuchet(test)




