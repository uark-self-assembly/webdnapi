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


class Topology:
    def __init__(self, file_string, nucleotide_count, strand_count, nucleotides):
        self.file_string = file_string
        self.nucleotide_count = nucleotide_count
        self.strand_count = strand_count
        self.nucleotides = nucleotides


def load_topology():
    with open('generated.top', 'r') as top:
        first_line = top.readline()
        top.seek(0)
        file_string = top.read()

    nucleotide_count = int(first_line.split()[0])
    strand_count = int(first_line.split()[1])
    nucleotides = file_string.splitlines()
    nucleotides.pop(0)
    loaded = Topology(file_string, nucleotide_count, strand_count, nucleotides)
    return loaded


class Energy:
    def __init__(self, file_string, time_steps):
        self.file_string = file_string
        self.time_steps = time_steps


def load_energy():
    with open('energy.dat', 'r') as energy:
        file_string = energy.read()

    time_steps = file_string.splitlines()
    loaded = Energy(file_string, time_steps)
    return loaded


class ExternalForces:
    def __init__(self, file_string, forces):
        self.file_string = file_string
        self.forces = forces


def load_external_forces():
    with open('external_forces.dat', 'r') as ext_forces:
        file_string = ext_forces.read()

    lines = file_string.splitlines()
    forces = []

    i = 0
    while i < len(lines):
        if lines[i] == '{':
            new_force = utils.Force()
            for j in range(i+1, len(lines), 1):
                if lines[j] == '}':
                    i = j
                    break
                attribute = lines[j].split(' = ')[0]
                value = lines[j].split(' = ')[1]
                new_force.attributes[attribute] = value
            forces.append(new_force)
        i += 1

    loaded = ExternalForces(file_string, forces)
    return loaded
