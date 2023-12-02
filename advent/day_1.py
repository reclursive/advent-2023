file = open("input/no_1.txt")
test = file.read()

def trebuchet(input):
    x= slice(0, 10)
    container = input.split("\n")[x]

    dict = {}
    no_calib = 0

    if len(container) >= 1:
        # total = 0
        for string in container:
            num_string = list(filter(str.isdigit, string))
            if len(num_string) <= 1:
                no_calib +=1
                continue
            else:
                key = string
                end = len(num_string)-1
                combo = int(num_string[0]+num_string[end])
                dict[key] = combo

    print(sum(dict.values()))
    print(dict)
    print(no_calib)

    return sum(dict.values())

trebuchet(test)




