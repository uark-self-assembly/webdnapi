class Generation:
    def __init__(self, method=None, arguments = None, orig: 'Generation' = None, dictionary=None):
        if orig is not None:
            self.copy(orig)
        elif dictionary is not None:
            self.load(dictionary)
        else:
            self.method: str = method
            self.arguments = []
            self.files = []
            if method == 'generate-sa':
                self.files = ['sequence.txt']
                self.arguments = ['generate-sa.py'] + arguments + self.files
            elif method == 'generate-folded':
                self.files = ['sequence.txt']
                self.arguments = ['generate-folded.py'] + arguments + self.files
            elif method == 'cadnano-interface':
                self.files = ['cadnano-project.json']
                self.arguments = ['cadnano_interface.py'] + self.files + arguments

            if self.files is None:
                raise ValueError('Value of method argument not valid')

    def copy(self, orig: 'Generation'):
        self.method = orig.method
        self.files = orig.files
        self.arguments = orig.arguments

    def load(self, dictionary):
        self.method = dictionary['method']
        self.files = dictionary['files']
        self.arguments = dictionary['arguments']


class Force:
    def __init__(self, force_type=None, dictionary=None):
        self.force_type = force_type
        if dictionary is None:
            self.attributes = {}
        else:
            self.attributes = dictionary


class Configuration:
    def __init__(self, time_step=None,
                 box_length_x=None, box_length_y=None, box_length_z=None,
                 energy_total=None, energy_potential=None, energy_kinetic=None,
                 nucleotides=None):
        self.time_step = int(time_step)
        self.box_length_x = float(box_length_x)
        self.box_length_y = float(box_length_y)
        self.box_length_z = float(box_length_z)
        self.energy_total = float(energy_total)
        self.energy_potential = float(energy_potential)
        self.energy_kinetic = float(energy_kinetic)
        if nucleotides is None:
            self.nucleotides = []
        else:
            self.nucleotides = nucleotides


class Nucleotide:
    def __init__(self, pos_x=None, pos_y=None, pos_z=None,
                 base_v_x=None, base_v_y=None, base_v_z=None,
                 normal_v_x=None, normal_v_y=None, normal_v_z=None,
                 velocity_x=None, velocity_y=None, velocity_z=None,
                 ang_velocity_x=None, ang_velocity_y=None, ang_velocity_z=None):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.pos_z = float(pos_z)
        self.base_v_x = float(base_v_x)
        self.base_v_y = float(base_v_y)
        self.base_v_z = float(base_v_z)
        self.normal_v_x = float(normal_v_x)
        self.normal_v_y = float(normal_v_y)
        self.normal_v_z = float(normal_v_z)
        self.velocity_x = float(velocity_x)
        self.velocity_y = float(velocity_y)
        self.velocity_z = float(velocity_z)
        self.ang_velocity_x = float(ang_velocity_x)
        self.ang_velocity_y = float(ang_velocity_y)
        self.ang_velocity_z = float(ang_velocity_z)
