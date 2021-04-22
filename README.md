# python101

# Table of Contents
1. [Processes and streams](#processes-and-streams)
1. [Git](#git)
1. [Compilation vs interpretation](#compilation-vs-interpretation)
1. [Python infrastructure](#python-infrastructure)

## Processes and streams

                            arguments                   
                              | | |                   ┌────────┐
                              V V V          .------->│ STDOUT │
        ┌─────────┐        ┌──────────────┐ /         └────────┘
        │  STDIN  │------->│    Process   │                 
        └─────────┘        └──────────────┘ \         ┌────────┐
                              ^ ^ ^      |   °------->│ STDERR │
                             / / /       |            └────────┘
                         ~~~~~~~~~~~~~   °        
                        │ ENVIRONMENT │   \      
                         ~~~~~~~~~~~~~     ° -> EXIT CODE
- STDIN

```python
import sys

for line in sys.stdin:
    print(line)
print(f"INFO")
```  

- STDOUT

```python
print(f"INFO")
```  

- STDERR

```python
import sys

print(f"ERROR", file=sys.stderr)
```

- exit code

```python
exit(1)
```

- arguments

```python
import sys

arg = sys.argv[1]
```    

- environment

```python
import os

os.getenv("USER")
```    

## Git

1. *commit* - to save changes
2. *push* - load to the internet repository
3. *update project* - load from the repository
4. *show git log* - show history

## Compilation vs interpretation

                      compiler                    computer
C, C++:         code ------------> machine code ------------> output

                      interpreter
Python:         code ------------> output

                      compiler               virtual machine                computer
Java, Scala:    code ------------> bytecode ----------------> machine code ----------> output

## Python infrastructure

### Pip, venv and dependencies

- Python and pip
- Venv
  ```python3 -m venv venv```
  pip install -r requirements.txt
- Virtual env pip3 install virtualenv virtualenv venv Mac: source venv/bin/activate | Win: mypthon\Scripts\activate pip install -r requirements.txt
  deactivate

json.dumps json.loads

curl -s -u username:$token https://api.github.com/users/t0lia | jq .login
  
