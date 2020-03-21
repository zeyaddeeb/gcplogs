import click


@click.group()
def cli():
    pass


@cli.group()
def list():
    """List resources"""
    pass
