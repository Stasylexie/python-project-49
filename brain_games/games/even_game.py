import random

from brain_games.engine import engine_game

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def get_number():
    number = random.randint(1, 100)
    return number


def first_game() -> None:
    engine_game(question=QUESTION, func_check=is_even,
                 func_get_question=get_number)


def check_answer():
    print("check answer here")
