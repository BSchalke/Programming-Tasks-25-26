import pytest

from File_Stats_Tool import compute_txt
from Simple_Logger_System import create_logger, add_log, view_log, clear_log
from Contact_Book import add_contact, search_contact, display_contacts

class TestFileStats:
    def test_all(self):
        assert compute_txt("words.txt") == (4, 18, 79, ("line",4))

class TestLogger:
    def test_all(self, capsys):
        clear_log("simple.log")
        logger = create_logger("simple.log")
        add_log(logger, "This is a test log")
        view_log("simple.log")
        captured = capsys.readouterr()
        expected = "This is a test log"
        print(captured.out[-len(expected):])
        assert captured.out[-len(expected)-2:] == expected+"\n\n"

class TestContact:
    def test_search(self):
        add_contact("test.txt", "test", "1234", "test@test")
        assert search_contact("test.txt", "test") == "test,1234,test@test"