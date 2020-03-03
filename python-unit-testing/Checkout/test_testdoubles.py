from .LineReader import readfromfile
from unittest.mock import MagicMock


# def test_cancallreadfromfile():
#     readfromfile("blah")

def test_returnscorrectstring(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result = readfromfile("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"
