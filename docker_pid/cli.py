#!/usr/bin/env python

import click
from tabulate import tabulate

def truncate(text, width=15, placeholder='...'):
    w = width-len(placeholder)
    return (text[:w] + placeholder) if len(text) > width else text

def modify_info(data):
    ret = []
    for r in data:
        del r[6:12]
        r[0] = truncate(r[0], 16,'') # container ID
        r[1] = truncate(r[1], 20) # container name
        r[6] = truncate(r[6], 20) # CMD
        ret.append(r)
    return ret

@click.command()
def main():
    from .core import docker_pids
    data = docker_pids()

    headers = ['Container ID', 'Container Name', 'User', 'PID', '%CPU', '%Mem', 'CMD']
    data = modify_info(data)
    click.echo(tabulate(data, headers))

if __name__ == '__main__':
    main()
