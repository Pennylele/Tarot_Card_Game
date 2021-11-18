import Game
import Player_login

class Play:
    def __init__(self, cur): # Game instance
        self.game = Game.Game(cur, player=None)
        self.cur = cur
        self.player = None

    def get_player(self):
        return self.player

    # Have user choose either to play as a registered player or a guest
    def playGame(self, card_conn):
        print("Welcome to the Tarot Game!")
        print("CHOOSE TO PLAY:\n"
          "1. As an existing Player (login required)\n"
          "2. Register as a New Player.\n"
          "3. As a Guest.\n")
        choice = input()
        while choice not in ("1", "2", "3"):
            print("Invalid choice. Please type in 1, 2, or 3.")
            choice = input()

        if choice == "3":
            self.start_a_play()
        elif choice == "2":
            login = Player_login.Login(self.cur)
            player = login.add_Player()
            self.player = player
            self.game.set_player(player)
            self.login_screen()
        elif choice == "1":
            login = Player_login.Login(self.cur)
            player = login.player_login()
            if player == False:
                self.playGame()
            self.player = player
            self.game.set_player(player)
            self.login_screen()

        card_conn.commit()

    # Once the user logged in, they can see this screen that gives them the choices or loading their history.
    def login_screen(self):
        print("SHALL WE BEGIN? \n"
            "1. Play a Game \n"
            "2. Load History \n"
            "9. Quit the Game")
        choice = input()
        while choice not in ("1", "2", "9"):
            print("Invalid choice. Please type in 1, 2, or 9.")
            choice = input()

        if choice == "9":
            print("Goodbye!")
            exit()
        elif choice == '1':
            self.start_a_play()
        elif choice == '2':
            if self.player == None:
                print("PLEASE CHOOSE TO LOGIN OR REGISTER:")
                print("1. log in\n"
                      "2. register\n")
                choice = input()
                while choice not in ("1", "2"):
                    print("Invalid choice. Please type in 1 or 2.")
                    choice = input()

                if choice == "1":
                    login = Player_login.Login(self.cur)
                    player = login.player_login()
                    if player != False:
                        self.player = player
                        self.game.set_player(player)
                    else:
                        self.login_screen()
                elif choice == "2":
                    login = Player_login.Login(self.cur)
                    player = login.add_Player()
                    self.player = player
                    self.game.set_player(player)
            self.game.get_history(self.player)
            self.login_screen()

            
    # This screen shows up once the user choose to "play a game" or "play as a guest"
    # If as a guest, they get the chance to log in or register after playing the current round.
    def start_a_play(self):
        print("We have Four types of card drawing methods: \n\n"
              "1. Drawing one card.\n"
              "2. Drawing two cards.\n"
              "3. Drawing three cards (Past, Present, Future)\n"
              "4. Drawing creative cards (Pick one number and a suit to creative a card of your own).\n"
              "Please type 1, 2 ,3, or 4 to indicate your choice. If you want to exist the game, type 9.\n")
        choice = input()
        while choice not in ("1", "2", "3", "4", "9"):
            print("Invalid choice. Please type in 1, 2, 3, 4 or 9.")
            choice = input()

        if choice == 9:
            print("Thanks for playing!")
            exit()
        elif choice == '1':
            self.choice_equal_one()
        elif choice == '2':
            self.choice_equal_two()
        elif choice == '3':
            self.choice_equal_three()
        else:
            self.choice_equal_four()

        ans = input("Play Again? (Y/N)\n")
        if ans == "N" or ans == "n":
            print("Thanks for playing!")
            exit()
        elif ans == "Y" or ans == "y":
            print("#" * 20 + "NEW GAME" + "#" * 20)
            self.login_screen()
        else:
            print("Unexpected input, exiting game. ")
            exit()

    def choice_equal_one(self):
        print("Good choice! \n"
              "1. Pick from all tarot cards, type 1;\n"
              "2. Pick from Major Arcana only, type 2;\n"
              "3. Pick from Minor Arcana only, type 3.\n")
        option = input()
        while option not in ("1", "2", "3"):
            print("Invalid choice. Please type in 1, 2, or 3.")
            option = input()

        self.game.pick_one_card(int(option))


    def choice_equal_two(self):
        return self.game.pick_two_card()

    def choice_equal_three(self):
        return self.game.pick_three_card()

    def choice_equal_four(self):
        print("Good choice!")
        num = input("Give me a number between 1 to 14.\n")
        while num not in [str(i) for i in range(1, 15)]:
            print("Invalid choice. Please type in a number between 1 to 14.")
            num = input()

        suit = input("Give me a suit number among\n"
                     "1. Wands,\n"
                     "2. Cups,\n"
                     "3. Pentacles,\n"
                     "4. Swords.\n")
        while suit not in ("1", "2", "3", "4"):
            print("Invalid choice. Please type in a number between 1 to 4.")
            suit = input()

        return self.game.pick_creative_card(num, suit)



