file = open("input/no_1.txt")
test = file.read()

def trebuchet(calib):
    cut = slice(0, 10)
    container = calib.split("\n")[cut]
    print(container)

    nums =[]
    if len(container) >= 1:
        total = 0
        for string in container:
            num_string = list(filter(str.isdigit, string))
            if len(num_string) == 0:
                continue
            elif len(num_string)==1:
                total = total + int(num_string[0])
            else:
                end = len(num_string)-1
                combo = int(num_string[0]+num_string[end])
                total = total + combo

    print(nums)
    print(total)

    return total



trebuchet(test)




