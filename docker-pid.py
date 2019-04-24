import docker 
import click
from tabulate import tabulate

def truncate(text, width=15, placeholder='...'):
    w = width-len(placeholder)
    return (text[:w] + placeholder) if len(text) > width else text

HEADERS = [
        'Container ID',
        'Container Name',
        'User',
        'PID',
        '%CPU',
        '%Mem',
        'VSZ',
        'RSS',
        'TTY',
        'STAT',
        'START',
        'TIME',
        'CMD']
def docker_pids():
    client = docker.from_env()
    containers = client.containers.list()

    data = []
    for c in containers:
        cid = c.attrs['Id']
        cname = c.attrs['Name']
        procs = c.top(ps_args="aux")
        for p in procs['Processes']:
            #del p[4:10]
            p[1] = int(p[1])
            p[2] = float(p[2])
            p[3] = float(p[3])
            d = [cid, cname]+p
            data.append(d)

    return data

def modify_info(data):
    ret = []
    for r in data:
        del r[6:12]
        print(r)
        r[0] = truncate(r[0], 16,'') # container ID
        r[1] = truncate(r[1], 20) # container name
        r[6] = truncate(r[6], 20) # CMD
        ret.append(r)
    return ret

@click.command()
def show_docker_pids():
    data = docker_pids()

    headers = ['Container ID', 'Container Name', 'User', 'PID', '%CPU', '%Mem', 'CMD']
    data = modify_info(data)
    click.echo(tabulate(data, headers))

if __name__ == '__main__':
    show_docker_pids()
