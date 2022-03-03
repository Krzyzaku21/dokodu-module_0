# %%
"""
Code creates lotto simulation
"""
from random import randint
import time


def add_number() -> list:
    """
    function creates user numbers
    """
    lists = []
    while len(lists) < 6:
        try:
            your_number = int(input("Add numbers : "))
            if your_number not in lists:
                if your_number < 1 or your_number > 49:
                    print("Your numbers must be between 0 and 49")
                else:
                    lists.append(your_number)
            else:
                print("Number exists in the list of numbers")
        except ValueError:
            print("Your numbers must be number")
    lists = sorted(lists)
    return lists


def add_lottery_numbers() -> list:
    """
    function creates lottery numbers
    """
    lists = []
    while len(lists) < 6:
        try:
            number = randint(1, 49)
            if number not in lists:
                lists.append(number)
        except ValueError:
            print('something goes wrong')
    return sorted(lists)


def add_lottery_costs(num: int) -> int:
    """
    function takes numbers of range and create costs in PLN
    """
    num = num * 3
    return num


def how_much_pairs(user_list: list, lottery_list: list) -> int:
    """
    function return pairs for numbers
    """
    numbers_of_pair = 0
    if numbers_of_pair < 6:
        for i in user_list:
            for j in lottery_list:
                if i == j:
                    numbers_of_pair += 1
    return numbers_of_pair


def when_start_lottery() -> int:
    """
    function creates day lottery start
    """
    start_day = 0
    day = int(input(
        """
        Select day to start:
        1. Monday
        2. Tuesday
        3. Wednesday
        4. Thursday
        5. Friday
        6. Saturday
        7. Sunday
        """
    ))
    if 1 >= day <= 8:
        if day % 2 != 0:
            start_day += 1
        else:
            when_start_lottery()
    return start_day


def print_pairs(list_elements: list) -> str:
    """
    function printing pairs for numbers in lottery
    """
    for i in range(1, 6):
        print(f"pairs of {i} was {list_elements.count(i)}")


def print_dates(days):
    """
    function printing weeks, months, and years of time lottery
    """
    print(f"weeks {(days//7)}")
    print(f"months {(days//30)}")
    print(f"years {(days//365)}")


def print_your_age(day: int) -> str:
    """
    function printing winner age when he got 6 in lotto
    """
    user_year = int(input('How old now you? '))
    years = day//365
    your_age = user_year + years
    return f"You win lottery in {your_age} probably if you live"


def winner_numbers(user_numbers: list, game_numbers: list, lottery_day: int) -> str:
    """
    function take list of numbers and check it with lottery
    """
    number_of_lottery = 0
    pairs = []
    try:
        while user_numbers != game_numbers:
            # print(user_numbers, game_numbers)
            number_of_pairs = how_much_pairs(user_numbers, game_numbers)
            if number_of_pairs != 0:
                pairs.append(number_of_pairs)
            game_numbers = add_lottery_numbers()
            number_of_lottery += 1
    except ValueError:
        print('something goes wrong')
    finally:
        print_pairs(pairs)
        finally_day = lottery_day + (number_of_lottery * 2)
        print_dates(finally_day)
        cost = add_lottery_costs(number_of_lottery)
        print_your_age(finally_day)
        print("Full cost : " + f'{cost:,} ' + "PLN")
        print("Winner numbers : " + ", ".join(map(str, game_numbers)))


# %%
if __name__ == "__main__":
    start = time.time()
    PERSON_NUMBERS = add_number()
    LOTTERY_NUMBERS = add_lottery_numbers()
    PERSON_DAY = when_start_lottery()
    winner_numbers(PERSON_NUMBERS, LOTTERY_NUMBERS, PERSON_DAY)
    stop = time.time()
    print("Exec time for processes:", stop - start, "[s]")
