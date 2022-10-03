import random
import sys


class Numdle:
    """Number Guessing Game - Wordle + Numbers = Numdle"""

    def __init__(self):
        self.generated_number_list = []
        self.generated_number_full = ""
        self.length = 0
        self.guesses = 0
        self.guess_mode = False
        self.guess_lives = 0
        self.game_condition = False
        self.quit_game = ["quit", "exit"]
        self.input_history = {}

    def difficulty_length(self):
        """Set the Difficulty of the game - Sets the number of digits to generate."""
        length = int(input("Enter Digits Length: "))
        while length > 10 or length <= 0:
            print("Digits length cannot be smaller than 1 or larger than 10!")
            length = int(input("Enter Digits Length: "))
        self.length = length

    def difficulty_guess(self):
        """Set the Difficulty of the game - Determine if 'lives' are enabled."""
        choices = ["Y", "N"]

        user_choice = input("Enables lives?\nEnter Y/N: ")
        while user_choice.upper() not in choices:
            user_choice = input("Please Enter Y or N: ")
        self.guess_mode = user_choice.upper() == "Y"

        if self.guess_mode:
            while self.guess_lives < 1 or self.guess_lives > 100:
                self.guess_lives = int(
                    input("Enter number of 'lives' - Must be between 1 and 100.\n>>: ")
                )

    def number_compare(self, player_guess):
        """Compares players guess to the actual number."""
        generated_number_copy = list(self.generated_number_full).copy()
        player_guess_list = list(player_guess)
        cow = 0
        for g_num, p_num in zip(list(self.generated_number_full), player_guess_list):
            if g_num == p_num:
                cow += 1
                generated_number_copy.remove(g_num)

        bull = sum(
            x in player_guess_list
            for x, _ in zip(generated_number_copy, player_guess_list)
        )

        print(f"\n{cow} cow(s) and {bull} bull(s)\n")
        if cow != self.length:
            self.guesses += 1

        if cow == self.length:
            self.game_condition = True
            print(
                f"""You Win!\nThe Number was [{self.generated_number_full}].
                  \nYou made {self.guesses + 1} guesses!"""
            )

    def lives_check(self):
        """Checks and compares if the player is out of guesses or lives."""
        if self.guess_mode is True:
            print(f"Remaining Lives: {self.guess_lives - self.guesses}\n")
            if (self.guess_lives - self.guesses) == 0:
                self.game_condition = True
                print(
                    f"""GAME OVER - Out of lives!
                    \nThe Number was [{self.generated_number_full}]."""
                )

    def generate(self):
        """Generate the randomised digits, with the number of digits dependent on the difficulty."""
        self.generated_number_list = [
            random.randrange(0, 10, 1) for _ in range(self.length)
        ]
        self.generated_number_full = "".join(map(str, self.generated_number_list))

    def value_check(self):
        """Checks the setting values"""
        print(
            f"""---------------
            \nGenerated Number: {self.generated_number_full}
            \nDifficulty-Length: {self.length}
            \nDifficulty-Lives Mode: {self.guess_mode}
            \n---------------"""
        )
        if self.guess_mode is True:
            print(f"Lives: {self.guess_lives}")

    def input_check(self):
        """Gets player input and check if its legal."""
        while True:
            players_input = input(
                f"Enter a {self.length}-digit number or 'quit' to exit game\nEnter Value: "
            )
            if players_input.isdigit() and len(players_input) == self.length:
                return players_input
            print(f"Please enter a {self.length}-digit number.\n")

    def user_input_history(self, player_guess):
        """Keeps track of the users inputs."""
        self.input_history[f"Guess {self.guesses + 1}"] = player_guess
        return self.input_history


if __name__ == "__main__":
    Session = Numdle()
    Session.difficulty_length()
    Session.difficulty_guess()
    Session.generate()
    Session.value_check()
    while Session.game_condition is False:
        player_input = Session.input_check()
        Session.user_input_history(player_input)
        Session.number_compare(player_input)
        Session.lives_check()
        if player_input.lower() in Session.quit_game:
            sys.exit("-----Exiting Game-----")
    print(Session.input_history)
