import random


def function_A(min_val, max_val):
    """
    Generate a random integer between min_val and max_val (inclusive).

    Args:
    - min_val (int): The minimum value.
    - max_val (int): The maximum value.

    Returns:
    - int: A random integer.
    """
    return random.randint(min_val, max_val)


def function_B():
    """
    Generate a random arithmetic operator: +, -, or *.

    Returns:
    - str: A random arithmetic operator.
    """
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, operator):
    """
    Perform an arithmetic operation based on the provided numbers and operator.

    Args:
    - n1 (int): The first operand.
    - n2 (int): The second operand.
    - operator (str): The arithmetic operator.

    Returns:
    - tuple: A tuple containing the problem expression and the correct answer.
    """
    problem_expression = f"{n1} {operator} {n2}"

    if operator == '+':
        correct_answer = n1 + n2
    elif operator == '-':
        correct_answer = n1 - n2
    else:
        correct_answer = n1 * n2

    return problem_expression, correct_answer


def math_quiz():
    """
    Main function for the Math Quiz Game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = function_A(1, 10)
        n2 = function_A(1, 5)
        operator = function_B()

        problem, answer = function_C(n1, n2, operator)

        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
