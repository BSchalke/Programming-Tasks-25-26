import pytest

from Dice_Roll import find_avg
from Array_Adder import create_2d, edit_2d, del_2d
from Temp_Stats_CSV import get_values
from File_word_Search import count_term

class TestDiceRoll:
    def test_normal(self):
        assert find_avg({1:5, 2:3, 3:2, 4:10, 5:20, 6:0}) == pytest.approx(3.925)


class TestArrayAdder:
    def test_create(self):
        assert create_2d(2,2) == [[None, None],[None, None]]

    def test_edit(self):
        array = create_2d(2,2)
        assert edit_2d(array, 1, 1, "test") == [["test", None], [None, None]]

    def test_del(self):
        array = create_2d(2,2)
        array = edit_2d(array, 1, 1, "test")
        assert del_2d(array, 1, 1) == [[None, None], [None, None]]

class TestTempStats:
    def test_get_values(self):
        assert get_values(["dsa 23.0\n", "dsadssa 56.0\n", "dsja 99.0\n"]) == (23.0, 99.0, pytest.approx(59.3333333))

class TestFileWordSearch:
    def test_multi(self):
        assert count_term("cano.txt", "isn") == 26

    def test_single(self):
        assert count_term("cano.txt", "sherlock") == 1

    def test_none(self):
        assert count_term("cano.txt", "bumboclart") == 0