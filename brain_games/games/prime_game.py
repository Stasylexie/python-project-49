import random

from brain_games.engine import engine_game

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_number():
    number_left = random.randint(1, 100)
    return f"{number_left}"


def check_answer(n: str):
    n = int(n)
    if n < 2:
        return "no"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "no"
    return "yes"


def prime_game() -> None:
    engine_game(question=QUESTION, func_check=check_answer, 
                func_get_question=get_number)

