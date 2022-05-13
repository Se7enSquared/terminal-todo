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
    task_list = _load_tasks()
    id = len(task_list)
    task = Task(id, task, tag)
    task_list.append(task)
    _dump_tasks(task_list)


@app.command()
def delete(index: int):
    task_list = _load_tasks()
    for i, task in enumerate(task_list):
        if task.id == index:
             del task_list[i]
    with open("./data/tasks.json", "w") as f:
        json.dump(task_list, f, default=lambda obj: obj.encode(), indent=4)

@app.command()
def edit(index: int, task: str = None, tag: str = None):
    typer.echo(f"{index} edited")


@app.command()
def lst():
    pass


if __name__ == "__main__":
    app()
