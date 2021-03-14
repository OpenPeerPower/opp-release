"""Main part of the Open Peer Power Release helper."""
import click

from .commands import cli
from .core import OppReleaseError


def main(*args):
    """Main part of the Open Peer Power Release helper."""
    try:
        cli()
    except OppReleaseError as err:
        click.secho("An error occurred: {}".format(err), fg="red")


if __name__ == "__main__":
    main()
