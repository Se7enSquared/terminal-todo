import json
from collections import namedtuple
from os import remove
from os.path import exists

import typer
from rich.console import Console

from task import Task

console = Console()
app = typer.Typer()


@app.command()
def add(task: str, category: str):
    if exists("./data/tasks.json"):
        with open("./data/tasks.json") as f:
            task_list = json.load(f)
    else:
        task_list = []
    id = len(task_list)
    task = Task(id, task, category, "new")
    task_list.append(task)
    with open("./data/tasks.json", "w") as f:
        json.dump(task_list, f, default=lambda obj: obj.encode(), indent=4)


@app.command()
def delete(index: int):
    typer.echo(f"{index} deleted")


@app.command()
def edit(index: int, task: str = None, tag: str = None):
    typer.echo(f"{index} edited")


@app.command()
def lst():
    pass


if __name__ == "__main__":
    app()
