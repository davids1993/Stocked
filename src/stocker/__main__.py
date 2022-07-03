"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Stocker."""


if __name__ == "__main__":
    main(prog_name="stocker")  # pragma: no cover
