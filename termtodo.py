import typer
from datetime import datetime

app = typer.Typer()

@app.command()
def init(dbname: str):
    #initialize new todo db
    pass

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