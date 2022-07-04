"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """stocked."""


if __name__ == "__main__":
    main(prog_name="stocked")  # pragma: no cover
