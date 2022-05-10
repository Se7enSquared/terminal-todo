import pytest
from termtodo import add, delete, edit, lst

def test_add(capsys):
    add('test task', 'Work')
    captured = capsys.readouterr()
    assert captured.out == '"test task" added in Work\n'

def test_delete(capsys):
    delete(3)
    captured = capsys.readouterr()
    assert captured.out == '3 deleted\n'

