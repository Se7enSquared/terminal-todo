import json
from sqlite3 import dbapi2
import pytest
from termtodo import add, delete, edit, lst
from os.path import exists
from os import remove

from task import Task


@pytest.fixture(scope='module')
def task_list():
    if exists("./data/tasks.json"):
        remove("./data/tasks.json")
    add('pytest setup task', 'pytest')
    add('pytest setup task2', 'pytest')
    if exists("./data/tasks.json"):
        with open("./data/tasks.json") as f:
            task_list = json.load(f,object_hook=Task.decode)

    yield task_list

    if exists("./data/tasks.json"):
        remove("./data/tasks.json")

def test_add(task_list):
    add('test task', 'Work')
    with open("./data/tasks.json") as f:
        test_task_list = json.load(f)
    assert len(test_task_list) == 2

def test_delete(task_list):
    assert 0 in [int(x.id) for x in task_list]
    delete(1)
    with open("./data/tasks.json") as f:
        task_list = json.load(f,object_hook=Task.decode)
    assert 1 not in [int(x.id) for x in task_list]

