import pytest

from binary_search_tester import binary_search
from bubble_sort import bubble_sort
from grid_path_counter import count_paths_recursive
from insertion_sort import insertion

class TestBinarySearch:
    def test_normal(self):
        assert binary_search([1,2,3,4,5,6],4) == 3

    def test_not(self):
        assert binary_search([1,2,3,4,5,6],8) == -1

    def test_empty(self):
        assert binary_search([],5) == -1

class TestBubbleSort:
    def test_normal_sort(self):
        assert bubble_sort([6,2,0,1,2])[0] == [0,1,2,2,6]

    def test_empty(self):
        assert bubble_sort([])[0] == []

    def test_sorted(self):
        assert bubble_sort([1,2,3])[0] == [1,2,3]

class TestGrid:
    def test_normal(self):
        assert count_paths_recursive(4,2) == 4

    def test_empty(self):
        assert count_paths_recursive(0,0) == 0

    def test_one(self):
        assert count_paths_recursive(1,8) == 1

class TestInsertion:
    def test_normal(self):
        assert insertion([5,8,1,2,3])[0] == [1,2,3,5,8]

    def test_against_bubble(self):
        array = [5,8,9,2,1,1,2,3,5,6,8,2,4,0,99,34,653,234,65,2,3,43,7]
        assert insertion(array)[0] == bubble_sort(array)[0]

    def test_empty(self):
        assert insertion([])[0] == []