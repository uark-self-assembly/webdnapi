import jsonpickle
from webdnapi import utils


class ProjectSettings:
    def __init__(self, dictionary, file_string):
        self.file_string = file_string
        self.name = dictionary.get('name', None)
        self.generation = utils.Generation(dictionary=dictionary['generation'])
        self.script_chain = dictionary['script_chain']
        self.execution_time = dictionary['execution_time']


def load_project_settings():
    with open('project.json', 'r') as settings:
        file_string = settings.read()

    loaded = jsonpickle.decode(file_string)
    project_settings = ProjectSettings(dictionary=loaded, file_string=file_string)
    return project_settings


def load_input():
    input_settings = {}
    with open('input.txt', 'r') as input:
        for line in input:
            (key, val) = line.split(' = ')
            input_settings[key] = val

    return input_settings


def load_log():
    with open('log.dat', 'r') as log:
        file_string = log.read()

    return file_string


class StdOut:
    def __init__(self, file_string):
        self.file_string = file_string
        self.steps = file_string.splitlines()


def load_stdout():
    with open('stdout.log', 'r') as stdout:
        file_string = stdout.read()

    output_file = StdOut(file_string)
    return output_file


class Sequence:
    def __init__(self, file_string):
        self.file_string = file_string
        self.strands = file_string.splitlines()


def load_sequence():
    with open('sequence.txt', 'r') as sequence:
        file_string = sequence.read()

    loaded = Sequence(file_string)
    return loaded
