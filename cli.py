#!/usr/bin/env python
import click
from hello import add

@click.command()
@click.option('--first')
@click.option('--second')
def call_add(first,second):
    """This adds two numbers together"""

    result = add(first, second)
    print(result)
    #click.echo(click.style(f'{result}', bg='red'))

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    call_add()
