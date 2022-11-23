import typer

from ontotools.commands import file, version, directory, vocab


app = typer.Typer()
app.add_typer(file.app, name="file", help="File-related commands.")
app.add_typer(version.app, name="version", help="Version-related commands.")
app.add_typer(directory.app, name="dir", help="Directory-related commands.")
app.add_typer(vocab.app, name="vocab", help="Vocab-related commands.")
