import typer
from collections import namedtuple
from rich.console import Console
from rich.table import Table

STATUS_PREFIXES = {
    "New": "[ ]",
    "In Progress": "[>]",
    "Done": "[X]",
    "Cancelled": "[-]",
}

console = Console()
app = typer.Typer()


@app.command()
def add(task: str, tag: str):
    typer.echo(f'"{task}" added in {tag}')


@app.command()
def delete(index: int):
    typer.echo(f"{index} deleted")


@app.command()
def edit(index: int, task: str = None, tag: str = None):
    typer.echo(f"{index} edited")


@app.command()
def lst():

    task = namedtuple("task", "task category status")

    tasks = [
        task("Finish Report and Email to Boss", "Work", "New"),
        task("Look for lost keys", "Personal", "Done"),
        task("Set doc appointment for annie", "Personal", "In Progress"),
        task("Submit timecard", "Work", "Cancelled"),
    ]

    for task in tasks:
        console.print(f"{STATUS_PREFIXES[task.status]} {task[0]} [{task[1]}]")


if __name__ == "__main__":
    app()
