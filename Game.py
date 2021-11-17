import random
from Card import CardType
from csv import reader
from Player import Player
import collections


class Game:
    def __init__(self, cur):
        self.arcanas = collections.defaultdict(list) # 1-22 are major arcanas; 23-78 are minor arcanas
        self.curPlayer = None
        self.cur = cur

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

        with open('TarotCard.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            next(csv_reader)
            # Pass reader object to list() to get a list of lists
            for id, arcana, num, suit, name, meaning in list(csv_reader):
                self.arcanas[int(id)] = [num, suit, name, meaning]

    def add_Player(self):
        # add player to the game 
        newName = input('Please Enter your name:')
        newEmail = input('Please Enter your email:')
        newSecureQ = input('Please Enter your Secure Question:')
        newSecureA = input('Please Enter your Answer for secure question:')
        self.cur.execute(""" INSERT INTO players (name, email, SecureQ, SecureA) VALUES (?, ?, ?, ?) """, (newName, newEmail, newSecureQ, newSecureA))
        newID = self.cur.execute("""SELECT last_insert_rowid()""")
        newID = newID.fetchone()[0]
        self.curPlayer = Player(newID, newName, newEmail)
        print('New players created, with ID of ' + str(newID))

    def choose_Player(self):
        # choose which player want to log in
        curNum = self.cur.execute("""SELECT COUNT(*) FROM players;""")
        curNum = curNum.fetchone()[0]
        if (curNum == 0):
            print('There is no player in database, please add one first')
            return

        if (self.curPlayer != None):
            print('Current Player is: ' + str(self.curPlayer.get_id()))
            
        print('All players are listed here: ')
        # print(list_of_player.fetchall())
        list_of_player = self.cur.execute("""SELECT id FROM players""")
        for data in list_of_player:
            print(data[0])

        newID = int(input('Which ID do you like to log in? '))
        print('Please answer Security Question for Log In: ')
        print((self.cur.execute("""SELECT SecureQ FROM players WHERE id = ?""", (newID,))).fetchone()[0])
        input_secure_A = input()

        actual_secure_A = (self.cur.execute("""SELECT SecureA FROM players WHERE id = ?""", (newID,))).fetchone()[0]
        if actual_secure_A == input_secure_A:
            newName = (self.cur.execute("""SELECT name FROM players WHERE id = ?""", (newID,))).fetchone()[0]
            newEmail = (self.cur.execute("""SELECT email FROM players WHERE id = ?""", (newID,))).fetchone()[0]
            self.curPlayer = Player(newID, newName, newEmail)
            print('Login Success, you are with ID' + str(newID))
        else: 
            print('Login Failed, please try again')

    def get_history(self):
        # get history by id
        print('You are with ID' + str(self.curPlayer.get_id()))
        print('Please answer Security Question for Log In: ')
        print(self.cur.execute("""SELECT SecureQ FROM players WHERE id = ?""", (self.curPlayer.get_id(),)).fetchone()[0])
        input_secure_A = input()

        actual_secure_A = (self.cur.execute("""SELECT SecureA FROM players WHERE id = ?""", (self.curPlayer.get_id(),))).fetchone()[0]
        if actual_secure_A == input_secure_A:
            print('Verification Success.')
            player_history = (self.cur.execute("""SELECT * FROM history WHERE playerID = ?""", (self.curPlayer.get_id(),))).fetchall()
            print('History of ID: ' + str(self.curPlayer.get_id()))
            for data in player_history:
                print(data)
        else: 
            print('Verification Failed, please try again \n \n')

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
            graph = ''
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
            self.cur.execute(""" INSERT INTO history (playerID, cardPicked, result) VALUES (?, ?, ?) """, 
                            (self.curPlayer.get_id(), name, graph))



    def readDatabase(selfD):
        pass

    def writeDatabase(self):
        pass
