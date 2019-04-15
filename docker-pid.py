import textwrap

import docker 
from tabulate import tabulate

#  'Titles': ['USER',
#   'PID',
#   '%CPU',
#   '%MEM',
#   'VSZ',
#   'RSS',
#   'TTY',
#   'STAT',
#   'START',
#   'TIME',
#   'COMMAND']

def truncate(string, width=15, placeholder='..'):
    return textwrap.shorten(string, width, placeholder=placeholder)

def docker_pid():
    client = docker.from_env()
    containers = client.containers.list()
    data = []
    for c in containers:
        cid = str(c.attrs['Id'])
        cname = c.attrs['Name']
        procs = c.top(ps_args="aux")
        for p in procs['Processes']:
            del p[4:10]
            p[4]=truncate(p[4])
            p[4]=truncate(p[4])
            p[1] = int(p[1])
            p[2] = float(p[2])
            p[3] = float(p[3])
            cids = truncate(cid, width=12, placeholder='')
            d = [cids, cname]+p
            data.append(d)

    headers = ['container id', 'container name', 'user', 'pid', '%CPU', '%Mem', 'CMD']
    print(tabulate(data, headers))

if __name__ == '__main__':
    docker_pid()
