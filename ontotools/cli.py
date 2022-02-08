import typer

from ontotools.commands import file


app = typer.Typer()
app.add_typer(file.app, name="file")
