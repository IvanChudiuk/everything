import yaml

with open("config/config.yaml", "r") as file:
    app_config = yaml.safe_load(file)