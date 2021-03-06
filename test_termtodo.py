import json
from os import remove
from os.path import exists

import pytest

from task import Task
from termtodo import add, delete, edit, lst


@pytest.fixture(scope="module")
def task_list():
    if exists("./data/tasks.json"):
        remove("./data/tasks.json")
    add("pytest setup task", "pytest")
    add("pytest setup task2", "pytest")
    if exists("./data/tasks.json"):
        with open("./data/tasks.json") as f:
            task_list = json.load(f, object_hook=Task.decode)

    yield task_list

    if exists("./data/tasks.json"):
        remove("./data/tasks.json")


def test_add(task_list):
    add("test task", "Work")
    with open("./data/tasks.json") as f:
        test_task_list = json.load(f)
    assert len(test_task_list) == 3


def test_edit(task_list):
    edit(1, text="test task edited", tag="test tag edit", status='In progress')
    with open("./data/tasks.json") as f:
        task_list = json.load(f, object_hook=Task.decode)
    for task in task_list:
        if task.id == 1:
            assert task.text == 'test task edited'
            assert task.tag == 'test tag edit'
            assert task.status == 'In progress'


def test_delete(task_list):
    assert 0 in [int(x.id) for x in task_list]
    delete(1)
    with open("./data/tasks.json") as f:
        task_list = json.load(f, object_hook=Task.decode)
    assert 1 not in [int(x.id) for x in task_list]
