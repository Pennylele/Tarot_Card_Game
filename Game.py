import random
from Card import CardType
from csv import reader
import collections


class Game:
    def __init__(self):
        self.arcanas = collections.defaultdict(list) # 1-22 are major arcanas; 23-78 are minor arcanas

        with open('TarotCard.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            next(csv_reader)
            # Pass reader object to list() to get a list of lists
            for id, arcana, num, suit, name, meaning in list(csv_reader):
                self.arcanas[int(id)] = [num, suit, name, meaning]


    def current_Player(self):
        # add later - with player id passed in as a parameter
        pass

    def get_history(self):
        # get history by id
        pass

    def pick_one_card(self, choice=0): # choice should be among 0, 1 or 2
        if choice == CardType.MAJOR.value:
            card_no = random.randint(1, 22)
        elif choice == CardType.MINOR.value:
            card_no = random.randint(23, 78)
        else:
            card_no = random.randint(1, 78)

        self.print_card([self.arcanas[card_no]])


    def pick_two_card(self):
        cards = []
        minor_card_no = random.randint(1, 22)
        major_card_no = random.randint(23, 78)
        cards.append(self.arcanas[minor_card_no])
        cards.append(self.arcanas[major_card_no])
        self.print_card(cards)


    def pick_three_card(self):
        past = random.randint(1, 78)
        present = random.randint(1, 78)
        future = random.randint(1, 78)
        cards = []
        cards.append(self.arcanas[past])
        cards.append(self.arcanas[present])
        cards.append(self.arcanas[future])
        self.print_card(cards)


    def pick_creative_card(self, num, suit):
        for i in range(23, 79):
            card_info = self.arcanas[i]
            if card_info[0] == num and card_info[1] == suit:
                self.print_card([card_info])


    def print_card(self, cards): # cards is a list of card's info
        for i, card in enumerate(cards):
            name, meaning = card[2], card[3]
            if len(cards) == 3:
                if i == 0:
                    graph = "#" * 20 + "\n\n" + "PAST: " + name + "\n\n" + "#" * 20 + "\n" + meaning
                elif i == 1:
                    graph = "#" * 20 + "\n\n" + "PRESENT: " + name + "\n\n" + "#" * 20 + "\n" + meaning
                else:
                    graph = "#" * 20 + "\n\n" + "FUTURE: " + name + "\n\n" + "#" * 20 + "\n" + meaning
                print(graph)
            else:
                graph = "#" * 20 + "\n\n" + name + "\n\n" + "#" * 20 + "\n" + meaning
                print(graph)


    def readDatabase(selfD):
        pass

    def writeDatabase(self):
        pass
