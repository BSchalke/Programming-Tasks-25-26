import pytest

from Grade_Calculation import get_grade
from Password_Strength import check_password
from queue_simulation import Queue
from Shopping_List import create_shopping, edit_shopping, display_shopping
from Simple_Login import login

class TestGradeCalculator:
    def test_normal(self):
        assert get_grade(65) == "B"

    def test_boundary(self):
        assert get_grade(39) == "D"

    def test_invalid(self):
        assert get_grade(105) == "Invalid percentage"


class TestPasswordStrength:
    def test_weak(self):
        assert check_password("help") == "weak"

    def test_medium(self):
        assert check_password("ThisIsOk!") == "medium"

    def test_strong(self):
        assert check_password("ThisIsAVeryStr0ngPassw0rd!") == "strong"


class TestQueue:
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("Test")
        assert queue.values[0] == "Test"

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("Test1")
        queue.enqueue("Test2")
        assert queue.dequeue() == "Test1"

    def test_size(self):
        queue = Queue()
        queue.enqueue("1")
        queue.enqueue("2")
        queue.enqueue("3")
        assert queue.size == 3

class TestShopping:
    def test_edit(self):
        shopping = ["1","2","3","4"]
        edit_shopping(shopping, 3, "5")
        assert shopping == ["1", "2", "3", "5"]

    def test_display(self, capsys):
        display_shopping(["a","b","c"])
        captured = capsys.readouterr()
        expected = "1:\ta\n2:\tb\n3:\tc\n"
        assert captured.out == expected

class TestLogin:
    def test_incorrect(self):
        assert login("help", "me") == False

    def test_incorrect_user(self):
        assert login("help", "TheseSillyTasksDontMakeSenseAndThisPasswordIs100%Random") == False

    def test_incorrect_pass(self):
        assert login("Ben", "NO") == False

    def test_correct(self):
        assert login("Ben", "TheseSillyTasksDontMakeSenseAndThisPasswordIs100%Random") == True
