
file = open("input/tester.txt")
test = file.read()
import re

#  12 red cubes, 13 green cubes, and 14 blue cubes
# semi_colon = ";"
# for semi_colon in test:
# print(test)
input_2 = test.lower()
container = input_2.split("\n")

#game params
rc = 12
gc = 13
bc = 14


valid_game = []


def check_bag(round): 
    round_split = round.split(" ")
    # print(round_split)
    invalid_round = False
    

    for index, item in enumerate(round_split[1:]):
        print(item +"hayayay")
        if item.isalpha() and index == len(round_split)-1:
            return invalid_round
        elif item.isdigit():
            first_letter = round_split[index +1][0]
            print(first_letter)
            if (first_letter) and (first_letter == 'r') and (int(item) > rc):
                invalid_round = True
                print("checkeroni")
                return invalid_round
            elif first_letter and first_letter == 'g' and int(item) > gc:
                invalid_round = True
                return invalid_round
            elif first_letter and first_letter == 'b' and int(item) > bc:
                invalid_round = True
                return invalid_round

                


def cube_game(rc, gc, bc):
    for game in container:
        rounds = re.split(r'; |: ', game)
        game_num = rounds[0]
        # print(rounds)
        # print(len(rounds))
        if (len(rounds) <= 3 ):
            round_1 = rounds[1]
            check_bag(round_1)
       
        for round in rounds:
            if check_bag(round)== False:
                continue
            else:
                valid_game.append(game_num)
                print(valid_game)

                    
        # key = game_index
        # colon = game.indexOf(":")
        # new_dict[key]= 



cube_game(12, 13, 14)





