import sys

import click
import click_completion
from termcolor import colored

from ._version import __version__
from .core import list_available_resources

click_completion.init()


def install_callback(ctx, _, value):
    if not value or ctx.resilient_parsing:
        return value
    shell, path = click_completion.core.install()
    click.echo("%s completion installed in %s" % (shell, path))
    return sys.exit(0)


@click.group()
@click.option(
    "--install-completion",
    is_flag=True,
    callback=install_callback,
    expose_value=False,
    help="Install completion for the current shell.",
)
@click.version_option(prog_name=colored("gcplogs", "cyan"), version=__version__)
def cli():
    pass


@cli.group()
def list():
    pass


@list.command("resources")
@click.option("--project", "-p", default="", show_default=True)
def list_resources(project):
    print(list_available_resources(project))


@cli.command()
@click.option("--watch", "-w", default="", show_default=True)
@click.option("--filter-pattern", "-f", default="", show_default=True)
def logs(watch, filter_pattern):
    print(watch, filter_pattern)
