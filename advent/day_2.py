
file = open("input/no_2.txt")
test = file.read()
import re
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
        print(game, "GAME END")
        rounds = re.split(r';|: ', game)
        game_num = int(rounds[0].split(" ")[1])
        print(tally, "start Tally")
        tally +=game_num
        print(tally, "TALLY")
        print(game_num, "GAME START")
        print(rounds)
        print(len(rounds), "NUMBER OF ROUNDS")
        end = len(rounds)
        if len(rounds) == 3:
            end = (len(rounds)-1)
            print("NOOO")
        for round in rounds[1:end]:
            print(round, "ROUND")
            red = re.findall("\d+ r", round) or 0 
            green = re.findall("\d+ g", round) or 0
            blue = re.findall("\d+ b", round) or 0 
            print(red)
            print(blue)
            print(green)
            print("truuuest")
            if (red is not 0 and int(red[0].split(" ")[0]) > rc) or (blue is not 0 and int(blue[0].split(" ")[0]) > bc) or (green is not 0 and int(green[0].split(" ")[0])) > gc:
                tally = tally - game_num
                break
            else:
                continue

    print(tally, "TALLY HOO")
            
        


cube_game(12, 13, 14)


