import docker 


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
            p[1] = int(p[1])
            p[2] = float(p[2])
            p[3] = float(p[3])
            d = [cid, cname]+p
            data.append(d)

    return data
