from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent
config_path = f"{BASE_DIR}/config.yaml"

with open(config_path, "r") as file:
    app_config = yaml.safe_load(file)

with open(app_config["paths"]["logging_config"], "r") as file:
    logging_config = yaml.safe_load(file)
