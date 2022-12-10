
from enum import Enum, auto


class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


shape_from_letter = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
}

winner: dict[Shape, Shape] = {
    Shape.ROCK: Shape.PAPER,
    Shape.PAPER: Shape.SCISSORS,
    Shape.SCISSORS: Shape.ROCK,
}

shape_value: dict[Shape, int] = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}


class Outcome(Enum):
    WIN = auto()
    DRAW = auto()
    LOSS = auto()


outcome_from_letter = {
    "X": Outcome.LOSS,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}

outcome_value: dict[Outcome, int] = {
    Outcome.LOSS: 0,
    Outcome.DRAW: 3,
    Outcome.WIN: 6,
}


def get_my_shape(oponent_shape: Shape, goal_outcome: Outcome) -> Shape:
    if goal_outcome == Outcome.LOSS:
        return winner[winner[oponent_shape]]
    if goal_outcome == Outcome.DRAW:
        return oponent_shape
    if goal_outcome == Outcome.WIN:
        return winner[oponent_shape]


def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_round_score(oponent_shape: Shape, goal_outcome: Outcome) -> int:
    my_shape = get_my_shape(oponent_shape, goal_outcome)
    shape_score = shape_value[my_shape]
    outcome_score = outcome_value[goal_outcome]
    return shape_score + outcome_score


def get_score(lines):
    score = 0
    for line in lines:
        opponent_shape = shape_from_letter[line[0]]
        goal_outcome = outcome_from_letter[line[2]]
        score += get_round_score(opponent_shape, goal_outcome)
    return score


def main():
    lines = read_input()
    my_score = get_score(lines)
    print(f"{my_score = }")


if __name__ == "__main__":
    main()
