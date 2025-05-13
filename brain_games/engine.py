from typing import Callable

from brain_games.cli import welcome_user


def engine_game(
    question: str, func_check: Callable, func_get_question: Callable
) -> None:
    name = welcome_user()
    print(question)

    for _ in range(3):
        number = func_get_question()  
        print(f"Question: {number}")

        user_answer = input("Your answer: ").strip().lower()

        correct_answer = func_check(number) 

        if user_answer != correct_answer:
            print(
                f"""'{user_answer}' is wrong answer ;(. 
                Correct answer was '{correct_answer}'."""
            )
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
    else:
        print(f"Congratulations, {name}!")
