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
@click.option(
    "--event-start", "-e", default="1 min ago", help="Start time of event log"
)
@click.option(
    "--filter-pattern",
    "-f",
    default=None,
    help="""

    Filter pattern for event.

    Example:

    protoPayload:0.0.0.0/8

    For more advanced options see Google documentation:
    https://cloud.google.com/logging/docs/view/building-queries

    """,
)
@click.option("--watch", "-w", default=False, is_flag=True)
@common_options
def get_logs(resources, event_start, filter_pattern, watch, **kwargs):
    logs = GCPLogs(**kwargs)
    logs.get_logs(resources, event_start, filter_pattern, watch)
