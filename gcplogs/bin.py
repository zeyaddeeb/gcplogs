import click

cli = click.Group()


@cli.group()
def list():
    """List resources"""
    pass
