from rich import print
from rich.table import Table
from rich.progress import track
import time

# Colorful text
print("[bold magenta]Welcome to Rich![/bold magenta] :sparkles:")
print("[green]This is green[/green] and [yellow]this is yellow[/yellow].")

# Table Example
table = Table(title="Top Libraries")

table.add_column("Library", style="cyan", no_wrap=True)
table.add_column("Purpose", style="magenta")

table.add_row("Rich", "Beautiful terminal formatting")
table.add_row("Typer", "CLI app made easy")
table.add_row("Pydantic", "Data validation using type hints")

print(table)

# Progress bar
print("\n[bold blue]Doing some work...[/bold blue]")
for step in track(range(10), description="Processing..."):
    time.sleep(5)

print("[bold green]Done![/bold green] :check_mark_button:")
