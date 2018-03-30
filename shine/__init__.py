import yaml
import os

CONFIG = {}

def debug(*args, **kwargs):
    print(*args, **kwargs)


# Load the configuration file
with open("moonshine.yml") as fil:
    CONFIG = yaml.load(fil)


# The main function to accept
def newProxy():
    i = {}
    i['user'] = os.environ['USER']
    i['ip'] = os.environ['SSH_CONNECTION']
    i['destination'] = os.environ['SSH_ORIGINAL_COMMAND']
    print(json.dumps(i, indent=2))
