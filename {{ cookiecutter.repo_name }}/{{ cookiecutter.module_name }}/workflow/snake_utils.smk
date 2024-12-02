from types import SimpleNamespace
from {{ cookiecutter.module_name }}.project_paths import project_paths

SCRIPTS = project_paths.scripts_path

configfile: project_paths.scripts.configs / 'config_data.yaml'
configfile: project_paths.scripts.configs / 'config_models.yaml'
configfile: project_paths.scripts.configs / 'config_workflow.yaml'
configfile: project_paths.scripts.configs / 'config_experiments.yaml'
config = SimpleNamespace(**config)

wildcard_constraints:
    model_name = '[a-zA-Z]+',

rule all:
    input:
        project_paths.reports / ...
