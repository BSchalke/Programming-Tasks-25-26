"""
Week 01 - Core Fundamentals
AQA A-Level Computer Science (7517) - Year 12
═══════════════════════════════════════════════════════════════════════════════

This file tests all six Week 01 tasks. You need to fill in the TODO sections to complete the tests.
The names of the file currently have numbers in front to identify which ones aren't complete, pytest will not work if there is a number there,
so you will need to rename the files to remove the numbers once you have completed them.
The test file will not run until all the TODOs are filled in and the files are renamed.

    Task 1 │ average_calculator.py
    Task 2 │ min_max_finder.py
    Task 3 │ array_reversal.py
    Task 4 │ linear_search.py
    Task 5 │ string_parser.py
    Task 6 │ temperature_converter.py

HOW TO RUN
──────────
    python -m pytest test_week01.py -v

YOUR JOB IN THIS FILE
─────────────────────
Everywhere you see a # TODO comment, you need to fill in:
    - The function call  →  what function are you testing?
    - The test data      →  what values are you passing in?
    - The expected result→  what should the function return?

The first test in each section has been completed as an example.
═══════════════════════════════════════════════════════════════════════════════
"""

import pytest

from average_calculator   import calculate_average
from min_max_finder       import find_min, find_max
from array_reversal       import reverse_array
from linear_search        import linear_search
from string_parser        import count_words, is_palindrome
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  TASK 1 — Average Calculator                                           ║
# ║  File: average_calculator.py                                           ║
# ║  Function: calculate_average(values)                                   ║
# ║      • Takes a list of numbers                                         ║
# ║      • Returns the mean as a float                                     ║
# ║      • Must NOT use sum() or statistics.mean()                         ║
# ╚═════════════════════════════════════════════════════════════════════════╝

class TestAverageCalculator:

    # EXAMPLE — this test has been written for you to show the pattern
    # Reminder that the titles of the assert line is the name of the function you create called calculate_average()
    # If you have changed the name of the function, you will need to change it here too for the test to work.
    def test_average_of_three_numbers(self):
        assert calculate_average([10, 20, 30]) == 20.0

    # ── CORE ──────────────────────────────────────────────────────────────

    def test_average_of_two_numbers(self):
        # TODO: call calculate_average() with two numbers that give a whole number average
        # e.g. calculate_average([???, ???]) == ???
        assert calculate_average([5, 7]) == 6.0

    def test_average_single_value(self):
        # TODO: a list with one value should return that value as a float
        assert calculate_average([1]) == 1 and isinstance(calculate_average([1]), float)

    def test_average_returns_float_type(self):
        # TODO: call calculate_average() and check the result is of type float
        result = calculate_average([4, 6, 7.5])
        assert isinstance(result, float)

    # ── EXPECTED ──────────────────────────────────────────────────────────

    def test_average_with_negative_numbers(self):
        # TODO: include at least one negative number in the list
        assert calculate_average([-1, -5, 9]) == 1

    def test_average_decimal_result(self):
        # TODO: choose values whose mean is not a whole number, e.g. [1, 2]
        assert calculate_average([1,2]) == pytest.approx(1.5)

    # ── STRETCH ───────────────────────────────────────────────────────────

    def test_average_empty_list_raises_error(self):
        # TODO: an empty list has no mean — what error should be raised?
        with pytest.raises(ValueError):
            calculate_average([])


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  TASK 2 — Min / Max Finder                                             ║
# ║  File: min_max_finder.py                                               ║
# ║  Functions: find_min(values)  /  find_max(values)                      ║
# ║      • Each takes a list of numbers                                    ║
# ║      • Returns the smallest / largest value                            ║
# ║      • Must NOT use Python's built-in min() or max()                   ║
# ╚═════════════════════════════════════════════════════════════════════════╝

class TestMinMaxFinder:

    # EXAMPLE
    def test_find_max_basic(self):
        assert find_max([3, 1, 4, 1, 5, 9]) == 9

    # ── CORE ──────────────────────────────────────────────────────────────

    def test_find_min_basic(self):
        # TODO: call find_min() with a list and check it returns the smallest value
        assert find_min(  # TODO
        ) == # TODO

    def test_find_max_single_element(self):
        # TODO: a list with one element — max should equal that element
        assert find_max(  # TODO
        ) == # TODO

    def test_find_min_single_element(self):
        # TODO: a list with one element — min should equal that element
        assert find_min(  # TODO
        ) == # TODO

    # ── EXPECTED ──────────────────────────────────────────────────────────

    def test_find_min_with_negative_numbers(self):
        # TODO: include negative numbers — which should be the minimum?
        assert find_min(  # TODO
        ) == # TODO

    def test_find_max_with_negative_numbers(self):
        # TODO: a list of only negative numbers — which is the maximum?
        assert find_max(  # TODO
        ) == # TODO

    def test_find_min_all_same_values(self):
        # TODO: what should find_min return if every element is identical?
        assert find_min(  # TODO
        ) == # TODO

    # ── STRETCH ───────────────────────────────────────────────────────────

    def test_find_min_empty_list_raises_error(self):
        # TODO: what happens if the list is empty? what error should be raised?
        with pytest.raises(  # TODO
        ):
            find_min([])

    def test_find_max_empty_list_raises_error(self):
        # TODO: same question for find_max
        with pytest.raises(  # TODO
        ):
            find_max([])


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  TASK 3 — Array Reversal                                               ║
# ║  File: array_reversal.py                                               ║
# ║  Function: reverse_array(values)                                       ║
# ║      • Takes a list                                                    ║
# ║      • Returns a new list in reverse order                             ║
# ║      • Must NOT use Python's built-in reverse() or [::-1]              ║
# ╚═════════════════════════════════════════════════════════════════════════╝

class TestArrayReversal:

    # EXAMPLE
    def test_reverse_basic_list(self):
        assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    # ── CORE ──────────────────────────────────────────────────────────────

    def test_reverse_two_elements(self):
        # TODO: reverse a list of exactly two elements
        assert reverse_array(  # TODO
        ) == # TODO

    def test_reverse_returns_list_type(self):
        # TODO: check the return type is a list
        result = reverse_array(  # TODO
        )
        assert isinstance(result, # TODO
        )

    def test_reverse_preserves_all_elements(self):
        # TODO: reversed list should contain exactly the same elements, just reordered
        original = # TODO
        result = reverse_array(original)
        assert sorted(result) == sorted(original)

    # ── EXPECTED ──────────────────────────────────────────────────────────

    def test_reverse_single_element(self):
        # TODO: reversing a one-element list should return the same list
        assert reverse_array(  # TODO
        ) == # TODO

    def test_reverse_string_list(self):
        # TODO: lists of strings should reverse just like lists of numbers
        assert reverse_array(  # TODO: e.g. ["a", "b", "c"]
        ) == # TODO

    def test_reverse_does_not_modify_original(self):
        # TODO: reverse_array should return a NEW list, not change the original
        original = [1, 2, 3]
        reverse_array(original)
        assert original == # TODO: what should original still equal after the call?

    # ── STRETCH ───────────────────────────────────────────────────────────

    def test_reverse_empty_list_returns_empty(self):
        # TODO: reversing an empty list should return an empty list, not raise an error
        assert reverse_array([]) == # TODO


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  TASK 4 — Linear Search                                                ║
# ║  File: linear_search.py                                                ║
# ║  Function: linear_search(values, target)                               ║
# ║      • Takes a list and a target value                                 ║
# ║      • Returns the index of the target if found                        ║
# ║      • Returns -1 if the target is not in the list                     ║
# ╚═════════════════════════════════════════════════════════════════════════╝

class TestLinearSearch:

    # EXAMPLE
    def test_search_target_found_in_middle(self):
        assert linear_search([10, 20, 30, 40, 50], 30) == 2

    # ── CORE ──────────────────────────────────────────────────────────────

    def test_search_target_not_found_returns_minus_one(self):
        # TODO: search for a value that is NOT in the list — should return -1
        assert linear_search(  # TODO
        ) == -1

    def test_search_target_at_first_index(self):
        # TODO: what index should be returned when the target is the first element?
        assert linear_search(  # TODO
        ) == # TODO

    def test_search_target_at_last_index(self):
        # TODO: what index should be returned when the target is the last element?
        assert linear_search(  # TODO
        ) == # TODO

    # ── EXPECTED ──────────────────────────────────────────────────────────

    def test_search_single_element_found(self):
        # TODO: list with one element, searching for that element
        assert linear_search(  # TODO
        ) == 0

    def test_search_single_element_not_found(self):
        # TODO: list with one element, searching for a different value
        assert linear_search(  # TODO
        ) == -1

    def test_search_returns_first_occurrence(self):
        # TODO: if the target appears more than once, the FIRST index should be returned
        assert linear_search(  # TODO: e.g. [5, 3, 5, 7], target=5
        ) == # TODO

    # ── STRETCH ───────────────────────────────────────────────────────────

    def test_search_empty_list_returns_minus_one(self):
        # TODO: searching an empty list should return -1, not raise an error
        assert linear_search(  # TODO
        ) == -1

    def test_search_string_values(self):
        # TODO: linear search should work on lists of strings too
        assert linear_search(  # TODO: e.g. ["cat", "dog", "fish"], target="dog"
        ) == # TODO


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  TASK 5 — String Parser                                                ║
# ║  File: string_parser.py                                                ║
# ║  Functions: count_words(text)  /  is_palindrome(text)                  ║
# ║      count_words:                                                      ║
# ║          • Takes a string                                              ║
# ║          • Returns the number of words as an integer                   ║
# ║      is_palindrome:                                                    ║
# ║          • Takes a string                                              ║
# ║          • Returns True if it reads the same forwards and backwards    ║
# ║          • Should ignore case and spaces                               ║
# ╚═════════════════════════════════════════════════════════════════════════╝

class TestStringParser:

    # EXAMPLE
    def test_count_words_basic_sentence(self):
        assert count_words("the cat sat on the mat") == 6

    # ── CORE ──────────────────────────────────────────────────────────────

    def test_count_words_single_word(self):
        # TODO: a single word string should return 1
        assert count_words(  # TODO
        ) == 1

    def test_count_words_returns_int_type(self):
        # TODO: check the return type is int
        result = count_words(  # TODO
        )
        assert isinstance(result, # TODO
        )

    def test_is_palindrome_true_for_palindrome(self):
        # TODO: "racecar" is a palindrome — should return True
        assert is_palindrome(  # TODO
        ) is True

    def test_is_palindrome_false_for_non_palindrome(self):
        # TODO: a word that is NOT a palindrome — should return False
        assert is_palindrome(  # TODO
        ) is False

    # ── EXPECTED ──────────────────────────────────────────────────────────

    def test_count_words_empty_string(self):
        # TODO: an empty string has no words — should return 0
        assert count_words(  # TODO
        ) == # TODO

    def test_count_words_extra_spaces(self):
        # TODO: "hello   world" has two words despite the extra spaces
        assert count_words(  # TODO
        ) == # TODO

    def test_is_palindrome_ignores_case(self):
        # TODO: "Racecar" should still be a palindrome despite the capital R
        assert is_palindrome(  # TODO
        ) is True

    def test_is_palindrome_single_character(self):
        # TODO: any single character is a palindrome
        assert is_palindrome(  # TODO
        ) is True

    # ── STRETCH ───────────────────────────────────────────────────────────

    def test_is_palindrome_ignores_spaces(self):
        # TODO: "never odd or even" is a palindrome when spaces are ignored
        assert is_palindrome(  # TODO
        ) is True

    def test_count_words_only_spaces_returns_zero(self):
        # TODO: a string of only spaces should return 0
        assert count_words(  # TODO
        ) == 0


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  TASK 6 — Temperature Converter                                        ║
# ║  File: temperature_converter.py                                        ║
# ║  Functions: celsius_to_fahrenheit(c)  /  fahrenheit_to_celsius(f)      ║
# ║      Formulae:                                                         ║
# ║          °F = (°C × 9/5) + 32                                          ║
# ║          °C = (°F − 32) × 5/9                                          ║
# ╚═════════════════════════════════════════════════════════════════════════╝

class TestTemperatureConverter:

    # EXAMPLE
    def test_celsius_to_fahrenheit_boiling_point(self):
        assert celsius_to_fahrenheit(100) == pytest.approx(212.0)

    # ── CORE ──────────────────────────────────────────────────────────────

    def test_celsius_to_fahrenheit_freezing_point(self):
        # TODO: 0°C should equal 32°F — a good known reference point
        assert celsius_to_fahrenheit(  # TODO
        ) == pytest.approx(  # TODO
        )

    def test_fahrenheit_to_celsius_boiling_point(self):
        # TODO: 212°F should convert back to 100°C
        assert fahrenheit_to_celsius(  # TODO
        ) == pytest.approx(  # TODO
        )

    def test_fahrenheit_to_celsius_freezing_point(self):
        # TODO: 32°F should convert to 0°C
        assert fahrenheit_to_celsius(  # TODO
        ) == pytest.approx(  # TODO
        )

    # ── EXPECTED ──────────────────────────────────────────────────────────

    def test_celsius_to_fahrenheit_body_temperature(self):
        # TODO: 37°C (body temperature) ≈ 98.6°F
        assert celsius_to_fahrenheit(  # TODO
        ) == pytest.approx(  # TODO, rel=1e-3
        )

    def test_celsius_to_fahrenheit_negative(self):
        # TODO: -40°C is the point where Celsius and Fahrenheit are equal (-40°F)
        assert celsius_to_fahrenheit(  # TODO
        ) == pytest.approx(  # TODO
        )

    def test_roundtrip_celsius_to_fahrenheit_and_back(self):
        # TODO: converting to °F and back to °C should give the original value
        original_celsius = # TODO: pick any temperature
        converted = fahrenheit_to_celsius(celsius_to_fahrenheit(original_celsius))
        assert converted == pytest.approx(  # TODO
        )

    # ── STRETCH ───────────────────────────────────────────────────────────

    def test_celsius_to_fahrenheit_absolute_zero(self):
        # TODO: absolute zero is -273.15°C — what is that in Fahrenheit?
        # Hint: -273.15°C = -459.67°F
        assert celsius_to_fahrenheit(  # TODO
        ) == pytest.approx(  # TODO, rel=1e-3
        )

    def test_fahrenheit_to_celsius_returns_float(self):
        # TODO: the result should always be a float, even for whole-number inputs
        result = fahrenheit_to_celsius(  # TODO
        )
        assert isinstance(result, # TODO
        )
