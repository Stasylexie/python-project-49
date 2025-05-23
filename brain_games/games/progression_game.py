import random

from brain_games.engine import engine_game

QUESTION = "What number is missing in the progression?"


def generate_progression(lenght=10, min_lenght=5):
    lenght = random.randint(min_lenght, lenght)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = [start + step * i for i in range(lenght)]

    return progression


def hide_number():
    progression = generate_progression()
    if len(progression) <= 5:
        index = 2
    else: 
        index = random.randint(2, len(progression) - 3)

    progression_w_gap = progression[:]
    progression_w_gap[index] = '..'
    progression_w_gap = list(map(str, progression_w_gap))
    progression_w_gap = " ".join(progression_w_gap)

    return progression_w_gap


def check_answer(progression):
    progression = progression.split()
    index = progression.index('..')

    step = (int(progression[-1]) 
            - int(progression[0])) // (len(progression) - 1)

    expected_number = None

    if index == 0:
        expected_number = int(progression[1]) - step
    elif index == len(progression) - 1:
        expected_number = int(progression[-2]) + step
    else:
        expected_number = int(progression[index - 1]) + step

    return str(expected_number)


def progression_game() -> None:
    engine_game(question=QUESTION, func_check=check_answer, 
                func_get_question=hide_number)

