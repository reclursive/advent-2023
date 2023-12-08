
file = open("input/no_3.txt")
test = file.read()
import re
input_2 = test.lower()
container = input_2.split("\n")

def gondola(input):
    regex_1 = [^\d.]
    engine_map = {}
    for index, line in enumerate(input):
        print(index, line)
        for index, char in enumerate(line):
            print(index, char)
            if char == ".":
                continue
            if char == 


            
    print()
gondola(container)