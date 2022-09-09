import yaml
import os

abspath = os.path.dirname(os.path.abspath(__file__))
print(abspath)

with open("config/config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)


ENV = cfg['ENV']  # PROD or DEV
LOG = cfg[ENV]['LOG']
RELAY = cfg[ENV]['RELAY']