import random
import Card
from csv import reader
import collections


class Game:
    def __init__(self, cur, card_conn, player=None):
        self.arcanas = collections.defaultdict(list) # 1-22 are major arcanas; 23-78 are minor arcanas
        self.cur = cur
        self.player = player
        self.card_conn = card_conn

        # create table if not already exist
        cur.execute(""" CREATE TABLE IF NOT EXISTS players (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        email text, 
                                        SecureQ text NOT NULL, 
                                        SecureA text NOT NULL
                                    ); """)
        
        cur.execute(""" CREATE TABLE IF NOT EXISTS history (
                                        historyID integer PRIMARY KEY AUTOINCREMENT,
                                        playerID integer,
                                        cardPicked text NOT NULL,
                                        result text NOT NULL
                                    ); """)

        # Read the card database
        with open('TarotCard.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            next(csv_reader)
            # Pass reader object to list() to get a list of lists
            for id, arcana, number, suit, name, meaning in list(csv_reader):
                id = int(id)
                if 1 <= id <= 22:
                    self.arcanas[id] = Card.MajorArcana(id, arcana, number, suit, name, meaning)
                else:
                    self.arcanas[id] = Card.MinorArcana(id, arcana, number, suit, name, meaning)


    def set_player(self, player):
        self.player = player


    def get_history(self, player):
        # get history by id
        player_id = player.get_id()
        player_history = (self.cur.execute("""SELECT * FROM history WHERE playerID = ?""", (player_id,))).fetchall()
        print('History of Cards: ')
        print("#" * 20)
        for data in player_history:
            print("{} -> {}".format(data[2], data[3]))
        print("#" * 20 + "\n")

    def pick_one_card(self, choice=0): # choice should be among 0, 1 or 2
        if choice == Card.CardType.MAJOR.value:
            card_no = random.randint(1, 22)
        elif choice == Card.CardType.MINOR.value:
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
            card = self.arcanas[i]
            if card.get_number() == num and card.get_suit() == suit:
                self.print_card([card])


    def print_card(self, cards): # cards is a list of card's info
        for i, card in enumerate(cards):
            name, meaning = card.get_name(), card.get_meaning()
            if len(cards) == 3:
                if i == 0:
                    graph = "#" * 20 + "\n\n" + "PAST: " + name + "\n\n" + "#" * 20 + "\n" + meaning
                elif i == 1:
                    graph = "#" * 20 + "\n\n" + "PRESENT: " + name + "\n\n" + "#" * 20 + "\n" + meaning
                else:
                    graph = "#" * 20 + "\n\n" + "FUTURE: " + name + "\n\n" + "#" * 20 + "\n" + meaning
            else:
                graph = "#" * 20 + "\n\n" + name + "\n\n" + "#" * 20 + "\n" + meaning
            print(graph)

            self.record_history(card)


    def record_history(self, card):
        if self.player:
            self.cur.execute(""" INSERT INTO history (playerID, cardPicked, result) VALUES (?, ?, ?) """,
                            (self.player.get_id(), card.get_name(), card.get_meaning()))

        self.card_conn.commit()