import math
import random
from brain_games.engine import engine_game



QUESTION = "Find the greatest common divisor of given numbers."


def get_number():
    number_left = random.randint(1, 100)
    number_right = random.randint(1, 100)
    return f"{number_left} {number_right}"


def check_answer(number: str):
    num1_str, num2_str = number.split()
    num1, num2 = int(num1_str), int(num2_str)
    return str(math.gcd(num1, num2))

def gcd_game() -> None:
    engine_game(question=QUESTION, func_check=check_answer, func_get_question=get_number)

