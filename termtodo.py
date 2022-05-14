import json
from collections import namedtuple
from os import remove
from os.path import exists

import typer
from rich.console import Console

from task import Task

console = Console()
app = typer.Typer()


def _load_tasks():
    if exists("./data/tasks.json"):
        with open("./data/tasks.json") as f:
            task_list = json.load(f, object_hook=Task.decode)
    else:
        task_list = []
    return task_list


def _dump_tasks(task_list):
    with open("./data/tasks.json", "w") as f:
        json.dump(task_list, f, default=lambda obj: obj.encode(), indent=4)


@app.command()
def add(task: str, tag: str):
    """Add a new task | command: add description tag"""
    task_list = _load_tasks()
    id = len(task_list)
    task = Task(id, task, tag)
    task_list.append(task)
    _dump_tasks(task_list)


@app.command()
def delete(index: int):
    """delete task | command: delete id"""
    task_list = _load_tasks()
    lst()
    for i, task in enumerate(task_list):
        if task.id == index:
            del task_list[i]
    lst()
    _dump_tasks(task_list)


@app.command()
def edit(
    id: int,
    text: str = typer.Option(None, help="set task text"),
    tag: str = typer.Option(None, help="set task tag"),
    status: str = typer.Option(None, help="set status"),
):
    """edit given task and specified attr | command edit id text= tag=..."""
    task_list = _load_tasks()
    lst()
    for i, task in enumerate(task_list):
        if task.id == int(id):
            target_task = task
            del task_list[i]
            break
    target_task.edit(text, tag, status)
    task_list.append(target_task)
    typer.echo(f"Task id# {task.id} edited")
    _dump_tasks(task_list)
    lst()


@app.command()
def lst():
    """display the task list No args."""
    task_list = _load_tasks()
    print(
        "\nT A S K  L I S T\n----------------\n\n")
    for task in task_list:
        print(task)
    print("\n=================================================================\n")


if __name__ == "__main__":
    app()
