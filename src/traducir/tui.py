"""Traducir, a TUI to make gdal_translate intuitive to use."""

from traducir.console import console


def tui() -> None:
    """TUI Entrypoint."""
    console.print("Hola Traducir!")


if __name__ == "__main__":
    tui()
