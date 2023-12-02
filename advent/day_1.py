# file = open("input/no_1.txt")
# test = file.read()

# def trebuchet(input):
#     container = input.split("\n")

#     dict = {}

#     if len(container) >= 1:
#         for string in container:
#             num_string = list(filter(str.isdigit, string))
#             key = string
#             if len(num_string) < 1:
#                 continue
#             elif len(num_string) ==1:
#                 combo = int(num_string[0]+num_string[0])
#                 dict[key] = combo
#             else:
#                 end = len(num_string)-1
#                 combo_2 = int(num_string[0]+num_string[end])
#                 dict[key] = combo_2
                

#     return sum(dict.values())

# trebuchet(test)


file = open("input/no_1.txt")
test = file.read()

def trebuchet(input):
    container = input.split("\n")

    dict = {}

    if len(container) >= 1:
        for string in container:
            num_string = list(filter(str.isdigit, string))
            key = string
            if len(num_string) < 1:
                continue
            elif len(num_string) ==1:
                temp = num_string*2
                combo = "".join(temp)
                dict[key] = int(combo)
            else:
                end = len(num_string)-1
                combo_2 = num_string[::len(num_string)-1]
                final_num = "".join(combo_2)
                dict[key] = int(final_num)
                
    
    print(sum(dict.values()))

trebuchet(test)



