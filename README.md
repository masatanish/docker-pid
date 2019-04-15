# Docker pid
Listing process IDs which run in docker container.

## Reqirements
- Python > 3 
  - not confirmed on python 2.x

## Prepare
```
pip install -r requirements.txt
```

### Run
```
python docker-pid.py
```

### ToDo
- [] support command line options
  - sort by PID, %CPU, %Mem, Container ID
- [] run as command line tool
- [] register to pypi as pip package
