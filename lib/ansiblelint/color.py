"""Console coloring and terminal support."""
import sys

from rich.console import Console
from rich.theme import Theme

_theme = Theme({
    "info": "cyan",
    "warning": "dim yellow",
    "danger": "bold red",
    "title": "yellow",
    "error_code": "bright_red",
    "error_title": "red",
    "filename": "blue"
})
console = Console(theme=_theme, emoji=False)
console_stderr = Console(file=sys.stderr, theme=_theme)
