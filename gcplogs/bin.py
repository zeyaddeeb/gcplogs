import functools
import sys

import click
import click_completion
from termcolor import colored

from ._version import __version__
from .constants import available_resources
from .core import GCPLogs

click_completion.init()


def common_options(f):
    options = [
        click.option("--project", "-p", help="List of projects associated with logs",),
        click.option(
            "--credentials",
            "-c",
            type=click.Path(),
            help="Path of the credentials file",
        ),
    ]
    return functools.reduce(lambda x, opt: opt(x), options, f)


def install_callback(ctx, _, value):
    if not value or ctx.resilient_parsing:
        return value
    shell, path = click_completion.core.install()
    click.echo("%s completion installed in %s" % (shell, path))
    return sys.exit(0)


@click.group()
@click.version_option(prog_name=colored("gcplogs", "cyan"), version=__version__)
@click.option(
    "--install-completion",
    is_flag=True,
    callback=install_callback,
    expose_value=False,
    help="Install completion for the current shell.",
)
def cli():
    pass


@cli.command("get")
@click.argument("resources", nargs=-1, type=click.Choice(available_resources))
@click.option("--filter-pattern", "-f", default=None)
@click.option("--watch", "-w", is_flag=True)
@common_options
def get_logs(resources, watch, filter_pattern, **kwargs):
    logs = GCPLogs(**kwargs)
    logs.get_logs(resources, watch, filter_pattern)
