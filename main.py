from Play import Play
from Game import Game
import sqlite3

def main():
    # get connected with the database
    card_conn = sqlite3.connect("GameHistory.db")
    cur = card_conn.cursor()

    game = Play(cur, card_conn)
    game.playGame()

if __name__ == "__main__":
    main()