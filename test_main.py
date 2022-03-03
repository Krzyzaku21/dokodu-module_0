"""
test main.py file
"""
from unittest.mock import patch, call
from main import (
    add_number,
    add_lottery_numbers,
    add_lottery_costs,
    when_start_lottery,
    print_your_age,
    print_dates,
    how_much_pairs
)


def test_add_number():
    """
    function test add_number
    """
    # @ given
    with patch('builtins.input', side_effect=[33, 22, 11, 44, 15, 23]):
        # @when
        return_value = add_number()
        # @then
        # * check elements in list length is 6
        assert len(return_value) == 6
        # * check values in list append and sorted
        assert return_value == [11, 15, 22, 23, 33, 44]
        # * check first value is highter or same like 1
        assert return_value[0] >= 1
        # * check first value is lower or same like 49
        assert return_value[-1] <= 49
        # * check number 11 is in list
        assert 11 in return_value
        # * check add_number return list
        assert isinstance(return_value, list)
        # * for element in list
        for i in return_value:
            # * check all types of numbers
            assert isinstance(i, int)


def test_add_lottery_numbers():
    """
    function test add_lottery_numbers
    """
    # @ given
    # @ when
    for _ in range(500):
        numbers = add_lottery_numbers()
        # @ then
        # * check len == 6
        assert len(numbers) == 6
        # * check first value is highter or same like 1
        assert numbers[0] >= 1
        # * check first value is lower or same like 49
        assert numbers[-1] <= 49


def test_add_lottery_costs():
    """
    function test add_lottery_costs
    """
    # @ given
    sample = 10000000
    # @ when
    result = add_lottery_costs(sample)
    # @ then
    # * check prise in finally is 3 times highter than sample
    assert result == 3 * sample
    # * check type of result is int
    assert isinstance(result, int)


def test_when_start_lottery():
    """
    function test when_start_lottery
    """
    # @ given
    for number in range(1, 8):
        with patch('builtins.input', side_effect=[number]):
            # @ when
            return_value = when_start_lottery()
            # @ then
            if return_value == 1:
                assert (return_value % 2) == 1
            else:
                assert (return_value % 2) == 0


@patch('builtins.print')
def test_print_dates(mock_print):
    """
    function test print_dates
    """
    # @ given
    days = 365
    weeks = (days//7)
    months = (days//30)
    years = (days//365)
    # @ when
    print_dates(days)
    # @then
    assert weeks == days//7
    assert months == days//30
    assert years == days//365
    mock_print.assert_has_calls([
        call(f"weeks {weeks}"),
        call(f"months {months}"),
        call(f"years {years}")
    ])


def test_print_your_age():
    """
    function test print_your_age
    """
    # @ given
    day = 365
    user_year = 32
    with patch('builtins.input', side_effect=[user_year]):
        # @ when
        result = print_your_age(day)
        years = day//365
        your_age = user_year + years
        # @ then
        assert your_age == 33
        assert result == f'You win lottery in {your_age} probably if you live'


def test_how_much_pairs():
    """
    function test how_much_pairs
    """
    # @ given
    user_nums = [1, 2, 3, 4, 5, 6]
    lottery_nums = [6, 5, 4, 3, 2, 33]
    # @ when
    result = how_much_pairs(user_nums, lottery_nums)
    # @ then
    assert result == 5
