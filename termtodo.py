import typer

app = typer.Typer()

@app.command()
def init():
    #initialize new todo db

if __name__ == '__main__':
    app()