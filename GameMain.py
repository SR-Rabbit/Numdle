import sys
import GameClass


game_session = GameClass.Numdle()
game_session.difficulty_length()
game_session.difficulty_guess()
game_session.generate()
game_session.value_check()
while game_session.game_condition is False:
    player_input = game_session.input_check()
    game_session.user_input_history(player_input)
    game_session.number_compare(player_input)
    game_session.lives_check()
    if player_input.lower() in game_session.quit_game:
        sys.exit("-----Exiting Game-----")
print(game_session.input_history)

# ----------------------------------------
# Number Guesser Game - Cows and Bulls
# [Program Premise]
# Player chooses number of digits to guess
# Program will automatically generate numbers for that number of digits
# Player have to guess the correct number, where the feedback after each attempt is cows and bulls
# Cows represents correctly guessed number in the correct position
# Bulls represents correctly gussed number in the wrong position
