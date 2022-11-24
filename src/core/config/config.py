import os

import yaml

with open(os.getcwd()+'/src/core/config/application.yaml', 'r') as yaml_conf:
    conf = yaml.safe_load(yaml_conf)[os.environ.get('ENV', 'local')]


class Config:
    app_name = conf['app_name']
    mongodb_uri = conf['mongodb_uri']
