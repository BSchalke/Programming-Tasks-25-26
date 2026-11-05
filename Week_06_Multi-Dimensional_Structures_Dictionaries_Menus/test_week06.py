import pytest

from Dictionary_Data_Merger import sum_dicts
from Multi_Dimension_Array_Rotation import rotate_matrix
from Student_Grades_Table import get_avg

class TestDictDataMerg:
    def test_normal(self):
        dict1 = {"Apples": 5, "Milk": 10, "Something else": 2}
        dict2 = {"Apples": 1, "Goo": 9, "Milk": 22}
        assert sum_dicts(dict1, dict2) == {"Apples": 6, "Milk": 32, "Something else": 2, "Goo": 9}

    def test_empty(self):
        assert sum_dicts({}, {}) == {}

class TestMatrixRotation:
    def test_normal_mat(self):
        assert rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8]]) == [[5, 1], [6, 2], [7, 3], [8, 4]]

    def test_empty_mat(self):
        assert rotate_matrix([[]]) == []

class TestStudentGrades:
    def test_avg(self):
        assert get_avg({"Alice": [80, 85, 90], "Ben": [70, 60, 75]}) == pytest.approx(76.666666667)