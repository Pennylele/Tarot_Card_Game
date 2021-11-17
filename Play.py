import Game

class Play:
    def __init__(self): # Game instance
        self.game = Game.Game()

    def playGame(self):
        print("Welcome to the Tarot Game!")
        print("Shall we begin?")

        while True:
            print("We have Four types of card drawing methods: \n\n"
                  "1. Drawing one card.\n"
                  "2. Drawing two cards.\n"
                  "3. Drawing three cards (Past, Present, Future)\n"
                  "4. Drawing creative cards (Pick one number and a suit to creative a card of your own).\n"
                  "Please type 1, 2 ,3, or 4 to indicate your choice. If you want to exist the game, type 9.\n")
            choice = input()
            while choice not in ("1", "2", "3", "4"):
                print("Invalid choice. Please type in 1, 2, 3, or 4.")
                choice = input()

            if choice == 9:
                print("Goodbye!")
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
            if ans == "N":
                print("Goodbye!")
                exit()
            else:
                print("#" * 20 + "NEW GAME" + "#" * 20)
                continue

    def choice_equal_one(self):
        print("Good choice! \n"
              "1. Pick from all tarot cards, type 0;\n"
              "2. Pick from Major Arcana only, type 1;\n"
              "3. Pick from Minor Arcana only, type 2.\n")
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



