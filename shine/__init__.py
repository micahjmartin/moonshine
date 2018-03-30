import yaml

CONFIG = {}

def debug(*args, **kwargs):
    print(*args, **kwargs)


# Load the configuration file
with open("moonshine.yml") as fil:
    CONFIG = yaml.load(fil)
