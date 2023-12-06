
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


def cube_game(rc, gc, bc):
    tally = 0
    for game in container:
        print(game)
        rounds = re.split(r';|: ', game)
        game_num = rounds[0].split(" ")[1]
        print(game_num, "NUMBIEE")
        print(rounds)
        print(len(rounds))
        end = len(rounds)
        if len(rounds) == 3:
            end = (len(rounds)-1)
            print("NOOO")
        for round in rounds[1:end]:
            print(round)
            red = re.findall("\d+ r", round) or 0
            green = re.findall("\d+ g", round) or 0
            blue = re.findall("\d+ b", round) or 0
            print("truuuest")
            print(red, "reed")
            print(blue, "bluuuue")
            print(green, "greeeenk")

            # if red > rc or green > gc or blue > bc:
            #     break
            # else:
            #     tally = tally + int(game_num)
    
        print(tally)

cube_game(12, 13, 14)


