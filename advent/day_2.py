
# file = open("input/tester.txt")
# test = file.read()
# import re

# #  12 red cubes, 13 green cubes, and 14 blue cubes
# # semi_colon = ";"
# # for semi_colon in test:
# # print(test)
# input_2 = str(test.lower())
# container = input_2.split("\n")

# #game params
# rc = 12
# gc = 13
# bc = 14


# valid_game = []

# def check_bag(round): 
#     invalid_round = 0
#     round_split = round.split(" ")
#     # print(round_split)
#     for index, item in enumerate(round_split[1:]):
#         print(round_split)
#         print(item +"ITEM")
#         # if index == 0:
#         #     continue
#         if item.isalpha():
#             print("ALPHA")
#             continue
#         elif item[0] == 'game':
#             continue
#         elif item.isalpha() and round_split[index] == len(round_split)-1 and not '':
#             break
#         elif item.isdigit():
#             if index == len(round_split)+1:
#                 continue
#             indx = index
#             print("DIGIT")
#             next_one_index = (indx + 1) % len(round_split)
#             next_one = round_split[next_one_index]
#             first_letter = str(next_one[0])
#             print(first_letter + "dsrgr")
#             if first_letter[0] == 'r' and int(item) > rc:
#                 invalid_round = True
#                 continue
#             elif first_letter[0] == 'g' and int(item) > gc:
#                 invalid_round = True 
#                 continue
#             elif first_letter[0] == 'b' and int(item) > bc:
#                 invalid_round = True
#                 continue
#             else:
#                 invalid_round = False

        
#         print(str(invalid_round))
#         return invalid_round

                


# def cube_game(rc, gc, bc):
#     tally = 0
#     for game in container:
#         print(game)
#         rounds = re.split(r';|: ', game)
#         game_num = rounds[0]
#         print(rounds)
#         print(len(rounds))
#         if (len(rounds) <= 4 ):
#             first = rounds[1]
#             if check_bag(first) == False:
#                 valid_game.append(game_num)
#                 continue
       
#         for round in rounds:
#             if check_bag(round)== True:
#                 continue
#             elif check_bag(round)==False:
#                     valid_game.append(game_num)
#     print(valid_game)

#     for game in valid_game:
#         game_split = game.split(" ")
#         id = game_split[1]
#         print(id)
#         tally = tally + int(id)

#         print(tally)
                    
#         # key = game_index
#         # colon = game.indexOf(":")
#         # new_dict[key]= 



# cube_game(12, 13, 14)







file = open("input/tester.txt")
test = file.read()
import re

#  12 red cubes, 13 green cubes, and 14 blue cubes
# semi_colon = ";"
# for semi_colon in test:
# print(test)
input_2 = str(test.lower())
container = input_2.split("\n")

#game params
rc = 12
gc = 13
bc = 14


valid_game = []

# def check_bag(round): 
#     invalid_round = 0
#     round_split = round.split(" ")
#     # print(round_split)
#     for index, item in enumerate(round_split[1:]):
#         print(round_split)
#         print(item +"ITEM")
#         # if index == 0:
#         #     continue
#         if item.isalpha():
#             print("ALPHA")
#             continue
#         elif item[0] == 'game':
#             continue
#         elif item.isalpha() and round_split[index] == len(round_split)-1 and not '':
#             break
#         elif item.isdigit():
#             if index == len(round_split)+1:
#                 continue
#             indx = index
#             print("DIGIT")
#             next_one_index = (indx + 1) % len(round_split)
#             next_one = round_split[next_one_index]
#             first_letter = str(next_one[0])
#             print(first_letter + "dsrgr")
#             if first_letter[0] == 'r' and int(item) > rc:
#                 invalid_round = True
#                 continue
#             elif first_letter[0] == 'g' and int(item) > gc:
#                 invalid_round = True 
#                 continue
#             elif first_letter[0] == 'b' and int(item) > bc:
#                 invalid_round = True
#                 continue
#             else:
#                 invalid_round = False

        
#         print(str(invalid_round))
#         return invalid_round

                


def cube_game(rc, gc, bc):
    tally = 0
    for index, game in enumerate(container):
        rounds = re.split(r'; ', game)
        if len(container)>0:
            for indx, round in enumerate(rounds):
                # id_match = re.match(r"Game " + "[1-9][0-9]|1[0-9]{2}|[0-9]", round[0])
                # id = id_match.group()
                find_id= round
               
                print(find_id)
              
                if len(round)> 0:
                    print(round, "ROUND UPPP")
                    red = re.match(r"[1-9][0-9]|1[0-9]{2}|[0-9]" + " red", round) or 0
                    green = re.match(r"[1-9][0-9]|1[0-9]{2}|[0-9]" + " green", round) or 0
                    blue = re.match(r"[1-9][0-9]|1[0-9]{2}|[0-9]" + " blue", round) or 0
                    acr = red.group()
                    acg = green.group()
                    acb = blue.group()
                    print(acr)
                    if acr > intrc or acg > gc or acb > bc:
                        continue
                    else:
                        print(amount_cubes,  "amountttttt")
            
        # tally += int(id)
        # if (len(rounds) <= 4 ):
        #     first = rounds[1]
        #     if check_bag(first) == False:
        #         valid_game.append(game_num)
        #         continue
       
    #     for round in rounds:
    #         if check_bag(round)== True:
    #             continue
    #         elif check_bag(round)==False:
    #                 valid_game.append(game_num)
    # print(valid_game)

    # for game in valid_game:
    #     game_split = game.split(" ")
    #     id = game_split[1]
    #     print(id)
    #     tally = tally + int(id)

    #     print(tally)
                    
        # key = game_index
        # colon = game.indexOf(":")
        # new_dict[key]= 



cube_game(12, 13, 14)



