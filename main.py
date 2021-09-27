import enum
import random


class Move(enum.Enum):
    STEN = 1
    SAX = 2
    PASE = 3
    
    def __str__(self) -> str:
        if self == Move.STEN:
            return "sten"
        if self == Move.SAX:
            return "sax"
        if self == Move.PASE:
            return "påse"
        return ""

class Winner(enum.Enum):
    PLAYER = 0
    COMPUTER = 1
    DRAW = 2


def get_wins_over_move(move: Move) -> Move:
    """
        Returns the move the supplied move wins over
    """
    if move == Move.PASE:
        return Move.STEN
    return Move(move.value+1)


def get_computer_move() -> Move:
    return random.choice((Move.STEN, Move.SAX, Move.PASE))


def checkResults(user, computer):
    if user == get_wins_over_move(computer):
        return Winner.COMPUTER
    if computer == get_wins_over_move(user):
        return Winner.PLAYER
    return Winner.DRAW


def get_points_to_win() -> int:
    while True:
        try:
            points_to_win = int(
                input("Hur många poäng behövs för att vinna? "))
            if points_to_win < 1:
                raise ValueError
            print()
            return points_to_win

        except ValueError:
            print("Max poängen du angav var inte ett positivt heltal")
            continue


def get_move() -> Move:
    print("Gör ditt val:")
    print("1: Sten")
    print("2: Sax")
    print("3: Påse")
    while True:
        try:
            move_as_int = int(input("> "))
            move_as_Move = Move(move_as_int)
            return move_as_Move
        except ValueError:
            print("Ditt val var inte ett heltal mellan 1 och 3")
            continue

def print_results(user_points: int, computer_points: int) -> None:
    print()
    print("Slutställning")
    print("-------------")
    print(f"Datorn:	{computer_points} poäng")
    print(f"Användaren: {user_points} poäng")

def main() -> None:
    print("*****************")
    print("Sten - Sax - Påse")
    print("*****************")
    print()
    points_to_win = get_points_to_win()

    player_points = 0
    computer_points = 0
    while True:
        move = get_move()
        computer_move = get_computer_move()
        winner = checkResults(move, computer_move)
        if winner == Winner.DRAW:
            print("Oavgjort")
            print()
            continue
        if winner == Winner.PLAYER:
            print()
            print(f"Datorn valde {computer_move}, du valde {move}. Du vann")
            player_points += 1
            if player_points == points_to_win:
                print_results(player_points, computer_points)
                break
        if winner == Winner.COMPUTER:
            print()
            print(
                f"Datorn valde {computer_move}, du valde {move}. Datorn vann")
            computer_points += 1
            if computer_points == points_to_win:
                print_results(player_points, computer_points)
                break
            


main()
