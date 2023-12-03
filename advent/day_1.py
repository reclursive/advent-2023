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

# PART ONE
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
#                 temp = num_string*2
#                 combo = "".join(temp)
#                 dict[key] = int(combo)
#             else:
#                 end = len(num_string)-1
#                 combo_2 = num_string[::len(num_string)-1]
#                 final_num = "".join(combo_2)
#                 dict[key] = int(final_num)
                
    
#     print(sum(dict.values()))

# trebuchet(test)


#Part two

file = open("input/no_1.txt")
test = file.read()



def trebuchet(input):
    noms = {
    "one": "OOOOO",
    "two": "^^^^",
    "three": "******",
    "four": "NNNNNNNNN",
    "five": "MMMMMMMMM",
    "six": "}}}}}}}}}}",
    "seven": "UUUUUU",
    "eight": "8",
    "nine": "9"
    }

    # for key, value in enumerate(noms):
    #     for substring in input:
    #         if key in 
    #             input[char] = data.replace(key, noms[key])

        input_2 = str(input).lower()
        container = input_2.split("\n")

    new_dict = {}
    if len(container) >= 1:
        for string in container:
                key = string
                new_dict[key] = ["",""]
                sorted_dict = dict(sorted(new_dict.items()))
        for item in sorted_dict:
            length = len(item)
            if item[0].isdigit():
                new_dict[item][0]=item[0]    
                start = item[-1]
            elif item[-1].isdigit():
                new_dict[item][1]=item[-1]

            


    print(sorted_dict)
    
trebuchet(test)


