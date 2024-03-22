import inspect
import os
from pathlib import Path
from types import SimpleNamespace


class project_paths_class:

    this_file = Path(inspect.getfile(lambda: None)).resolve()
    project_name = "{{ cookiecutter.repo_name }}"

    def __init__(self, working_dir=None):
        if self.iam_on_cluster():
            working_dir = Path().home() / self.project_name

        if working_dir is None:
            working_dir = self.this_file.parents[1].resolve()

        self.working_dir = working_dir
        self._set_paths(working_dir=working_dir)
        return None

    def _set_paths(self, working_dir):
        self.data_path = working_dir / 'data'
        self.data = SimpleNamespace(data=self.data_path)
        self.data.raw = self.data_path / 'raw'
        self.data.external = self.data_path / 'external'
        self.data.interim = self.data_path / 'interim'
        self.data.processed = self.data_path / 'processed'

        self.models = working_dir / 'models'
        self.notebooks = working_dir / 'notebooks'
        self.references = working_dir / 'references'
        self.reports = working_dir / 'reports'
        self.figures = working_dir / 'reports' / 'figures'

        self.scripts_path = working_dir / self.project_name
        self.scripts = SimpleNamespace(scripts=self.scripts_path)
        self.scripts.data = self.scripts_path / 'data'
        self.scripts.utils = self.scripts_path / 'utils'
        self.scripts.models = self.scripts_path / 'models'
        self.scripts.features = self.scripts_path / 'features'
        self.scripts.workflow = self.scripts_path / 'workflow'
        self.scripts.visualization = self.scripts_path / 'visualization'
        return None

    def iam_on_cluster(self):
        return ('hpc' in os.popen('hostname').read())


project_paths = project_paths_class()
