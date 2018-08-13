import jsonpickle
import os.path
from webdnapi import utils


class ProjectSettings:
    def __init__(self, dictionary, file_string):
        self.file_string = file_string
        self.name = dictionary.get('name', None)
        self.generation = utils.Generation(dictionary=dictionary['generation'])
        self.script_chain = dictionary['script_chain']
        self.execution_time = dictionary['execution_time']


def load_project_settings():
    with open(os.path.join('..', 'project.json'), 'r') as settings:
        file_string = settings.read()

    loaded = jsonpickle.decode(file_string)
    project_settings = ProjectSettings(dictionary=loaded, file_string=file_string)
    return project_settings


class Input:
    def __init__(self, file_string, settings):
        self.file_string = file_string
        self.settings = settings


def load_input():
    input_settings = {}
    with open(os.path.join('..', 'input.txt'), 'r') as input_file:
        file_string = input_file.read()
        input_file.seek(0)
        for line in input_file:
            (key, val) = line.split(' = ')
            input_settings[key] = val

    loaded = Input(file_string, input_settings)
    return loaded


def load_log():
    with open(os.path.join('..', 'log.dat'), 'r') as log:
        file_string = log.read()

    return file_string


class StdOut:
    def __init__(self, file_string):
        self.file_string = file_string
        self.steps = file_string.splitlines()


def load_stdout():
    with open(os.path.join('..', 'stdout.log'), 'r') as stdout:
        file_string = stdout.read()

    output_file = StdOut(file_string)
    return output_file


class Sequence:
    def __init__(self, file_string):
        self.file_string = file_string
        self.strands = file_string.splitlines()


def load_sequence():
    with open(os.path.join('..', 'sequence.txt'), 'r') as sequence:
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
    with open(os.path.join('..', 'generated.top'), 'r') as top:
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
    with open(os.path.join('..', 'energy.dat'), 'r') as energy:
        file_string = energy.read()

    time_steps = file_string.splitlines()
    loaded = Energy(file_string, time_steps)
    return loaded


class ExternalForces:
    def __init__(self, file_string, forces):
        self.file_string = file_string
        self.forces = forces


def load_external_forces():
    with open(os.path.join('..', 'external_forces.dat'), 'r') as ext_forces:
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


class Trajectory:
    def __init__(self, file_string, configuration):
        self.file_string = file_string
        self.configuration = configuration


def load_trajectory_initial():
    return __load_given_trajectory('generated.dat')


def load_trajectory_last():
    return __load_given_trajectory('last_conf.dat')


def __load_given_trajectory(file_name):
    with open(os.path.join('..', file_name), 'r') as traj:
        time_step = traj.readline().split(' ')[2]
        box_length_tokens = traj.readline().split(' ')
        box_length_x = box_length_tokens[2]
        box_length_y = box_length_tokens[3]
        box_length_z = box_length_tokens[4]
        energy_tokens = traj.readline().split(' ')
        energy_total = energy_tokens[2]
        energy_potential = energy_tokens[3]
        energy_kinetic = energy_tokens[4]
        nucleotide_strings = traj.readlines()
        traj.seek(0)
        file_string = traj.read()

    nucleotides = []
    for line in nucleotide_strings:
        tokens = line.split(' ')
        nucleotide = utils.Nucleotide(pos_x=tokens[0], pos_y=tokens[1], pos_z=tokens[2],
                                      base_v_x=tokens[3], base_v_y=tokens[4], base_v_z=tokens[5],
                                      normal_v_x=tokens[6], normal_v_y=tokens[7], normal_v_z=tokens[8],
                                      velocity_x=tokens[9], velocity_y=tokens[10], velocity_z=tokens[11],
                                      ang_velocity_x=tokens[12], ang_velocity_y=tokens[13], ang_velocity_z=tokens[14])
        nucleotides.append(nucleotide)

    config = utils.Configuration(time_step, box_length_x, box_length_y, box_length_z,
                                 energy_total, energy_potential, energy_kinetic, nucleotides)
    loaded = Trajectory(file_string, config)
    return loaded