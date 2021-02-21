import pathlib
import yaml


root_path = pathlib.Path(__file__).parent.parent.absolute()

config_yaml_path = root_path.joinpath('config_file_example.yaml')
with open(config_yaml_path) as f:
    config_yaml = yaml.safe_load(f)


invoice_dictio = {
    'products': [],
    'vat_rate': 0.21, # Default value
}