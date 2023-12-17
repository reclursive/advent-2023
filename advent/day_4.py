file = open("input/no_4.txt")
test = file.read()
import re
input_2 = test.lower()
container = input_2.split("\n")
total_tally = 0

#oop approach 
#first sort with winning ticket
#then sort hand 
# then apply check only while within range to speed up process
#while index is between and under range


class Lottery:
    def __init__(self, bundle):
        self.bundle = bundle
        self.length = len(bundle)

    def card_compare(self):
        global total_tally
        for card in self.bundle:
            card_wins = 0
            c_and_h = card.split(" | ")
            card_num = c_and_h[0]
            main_hand = sorted(list(filter(None, c_and_h[1].split(" "))), key=float)  
            winning_nums = card_num.split(":")[1]
            winning_nums2 = winning_nums.split(" ")
            winning_final = sorted(list(filter(None, winning_nums2)), key=float)  

            for num in main_hand:
                if int(num) < int(winning_final[0]):
                    continue
                elif int(num) <= int(winning_final[-1]):
                    if num in winning_final:
                        if card_wins == 0 or card_wins ==1:
                            card_wins += 1
                        else:
                            card_wins = card_wins*2     
                    else:
                        continue
            total_tally += card_wins
        return total_tally


         

powerBall = Lottery(container)

print(powerBall.card_compare())






