import jsonpickle
from webdnapi import utils


def load_project_settings():
    with open('project.json', 'r') as settings:
        file_string = settings.read()

    loaded = jsonpickle.decode(file_string)
    project_settings = ProjectSettings(dictionary=loaded, file_string=file_string)
    return project_settings


class ProjectSettings:
    def __init__(self, dictionary, file_string):
        self.file_string = file_string
        self.name = dictionary['name']
        self.generation = utils.Generation(dictionary=dictionary['generation'])
        self.script_chain = dictionary['script_chain']
        self.execution_time = dictionary['execution_time']

