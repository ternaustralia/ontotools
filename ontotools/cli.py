import typer

from ontotools.commands import file, version, directory


app = typer.Typer()
app.add_typer(file.app, name="file")
app.add_typer(version.app, name="version")
app.add_typer(directory.app, name="dir")
