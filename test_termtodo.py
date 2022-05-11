import json
import pytest
from termtodo import add, delete, edit, lst
from os.path import exists
from os import remove


def test_setup():
    if exists("./data/tasks.json"):
        remove("./data/tasks.json")
    assert not exists("./data/tasks.json")

def test_add():
    add('test task', 'Work')
    with open("./data/tasks.json") as f:
        test_task_list = json.load(f)
    assert len(test_task_list) == 1

def test_delete(capsys):
    delete(3)
    captured = capsys.readouterr()
    assert captured.out == '3 deleted\n'

