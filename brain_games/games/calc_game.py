from random import choice
import random
from brain_games.engine import engine_game

OPERATORS = ["+", "-", "*"]


QUESTION = "What is the result of the expression?"


def get_number():
    number_left = random.randint(1, 100)
    number_right = random.randint(1, 100)
    operator = choice(OPERATORS)
    return f"{number_left} {operator} {number_right}"


def check_answer(number: str):
    num1_str, operator, num2_str = number.split()
    num1, num2 = int(num1_str), int(num2_str)

    if operator == "+":
        return str(num1+num2)
    elif operator == "-":
        return str(num1-num2)
    else:
        return str(num1*num2)

def calc_game() -> None:
    engine_game(question=QUESTION, func_check=check_answer, func_get_question=get_number)
