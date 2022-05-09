import typer
from datetime import datetime
import sqlite3
from dbmanager import DatabaseManager

app = typer.Typer()

@app.command()
def init(dbname: str):
    try:
        DatabaseManager.check_database(dbname)
    except sqlite3.OperationalError:
        DatabaseManager(dbname)


@app.command()
def add(item: str, priority: int, due: datetime, status='new'):
    #add todo
    #id = biggest id + 1
    #item
    #priority in 1, 2, 3
    #due date
    #status in new, in progress, done
    pass

@app.command()
def list():
    #show all todo
    pass

@app.command()
def done(id: int):
    #mark done
    pass

@app.command()
def delete(id:int):
    #delete given todo
    pass

@app.command()
def clear():
    #clear all todo
    pass

if __name__ == '__main__':
    app()