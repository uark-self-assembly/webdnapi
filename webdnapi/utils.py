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
        self.time_step = time_step
        self.box_length_x = box_length_x
        self.box_length_y = box_length_y
        self.box_length_z = box_length_z
        self.energy_total = energy_total
        self.energy_potential = energy_potential
        self.energy_kinetic = energy_kinetic
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
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.base_v_x = base_v_x
        self.base_v_y = base_v_y
        self.base_v_z = base_v_z
        self.normal_v_x = normal_v_x
        self.normal_v_y = normal_v_y
        self.normal_v_z = normal_v_z
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z
        self.ang_velocity_x = ang_velocity_x
        self.ang_velocity_y = ang_velocity_y
        self.ang_velocity_z = ang_velocity_z
