import Player
import Play

class Login:
    def __init__(self, cur):
        self.cur = cur

    # enforce unique user email.
    def add_Player(self):
        # add player to the game
        newName = input('Please Enter your name: ')
        newEmail = input('Please Enter your email: ') # check if this email exists already
        email_check = self.cur.execute("""SELECT * FROM players WHERE email = ?""", (newEmail,)).fetchone()
        if email_check:
            print("This email is taken. Please log in as an existing player.")
            self.player_login()
        newSecureQ = input('Please Enter your Secure Question: ')
        newSecureA = input('Please Enter your Answer for secure question: ')
        self.cur.execute(""" INSERT INTO players (name, email, SecureQ, SecureA) VALUES (?, ?, ?, ?) """, (newName, newEmail, newSecureQ, newSecureA))
        newID = self.cur.execute("""SELECT last_insert_rowid()""")
        newID = newID.fetchone()[0]
        print("New player created! Hello, {}!".format(newName))
        player = Player.Player(newID, newName, newEmail)
        return player

    # player uses email and secure asnwers to log in. Also deals with authentication failures.
    def player_login(self):
        Email = input('Please Enter your email: ')
        player = self.cur.execute("""SELECT * FROM players WHERE email = ?""", (Email,)).fetchone()
        if not player:
            print("No such email exists. Login Failed.")
            return False
        else:
            secureQ = player[3]
            secureA = player[4]
            print(secureQ)
            player_ans = input('Please Enter your Answer for secure question:\n')
            if secureA != player_ans:
                print("Anthentication failed.")
                return False
            else:
                player_id = player[0]
                player_name = player[1]
                print("Login Success! Hello, {}!".format(player_name))
                player = Player.Player(player_id, player_name, Email)
                return player