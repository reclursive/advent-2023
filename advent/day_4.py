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

#pseudo for part 2 of problem
#eumerate initial card in bundle so that following cards inclusive of original card number
#can be pointed to 
#specifies COPIES and not actual card
#avoid append 
    def card_win(self):
        global total_tally
        for index, card in enumerate(self.bundle):
            index = index+1
            # print(index, card)
            num_wins = 0
            card_box = []
            c_and_h = card.split(" | ")
            print(c_and_h)
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
                        if num_wins == 0:
                            num_wins += 1
                            copy = list(self.bundle[index+1]).copy()
                            card_box.append(copy)
                        else:
                            num_wins += num_wins
                            copy2 = list(self.bundle[index+num_wins]).copy()
                            card_box.append(copy2)    
                    else:
                        continue
            print(card_box, "CB")    



         

powerBall = Lottery(container)

print(powerBall.card_win())






